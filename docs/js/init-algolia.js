/*
 * Algolia DocSearch for the Percona documentation home page.
 *
 * - Searches the docs index on the Percona Algolia account.
 * - Shows only pages under ALGOLIA_CONFIG.urlPrefix
 *   (the whole docs set on the home page; a project's own path in a project).
 * - Adds a "See all N results" link to the dropdown that opens the full
 *   results page (any page containing <div id="algolia-results"></div>).
 */

const ALGOLIA_CONFIG = {
  appId: 'QPF6EL892Z',
  apiKey: '72ae01e59f74373372979e09001708fb',
  indexName: 'percona_docs_pages',
  urlPrefix: 'https://docs.percona.com/',
  resultsPage: '/search-results/',
  resultsPerPage: 20,
};

const PRODUCT_ABBREVIATIONS = {
  pxb: 'Percona XtraBackup',
  pxc: 'Percona XtraDB Cluster',
  psmdb: 'Percona Server for MongoDB',
  pbm: 'Percona Backup for MongoDB',
  pmm: 'Percona Monitoring and Management',
  pt: 'Percona Toolkit',
};

/* ---------- Shared helpers ---------- */

// Replaces known abbreviations (pxb, pmm, ...) with the product name,
// and returns the product so its pages can be ranked first.
function expandQuery(query) {
  let product = null;
  const expanded = (query || '')
    .split(/\s+/)
    .map((word) => {
      const fullName = PRODUCT_ABBREVIATIONS[word.toLowerCase()];
      if (fullName) {
        product = fullName;
        return fullName;
      }
      return word;
    })
    .join(' ');
  return { expanded, product };
}

// "Page title - Product name" -> ["Page title", "Product name"]
function splitTitle(title) {
  title = title || '';
  const i = title.lastIndexOf(' - ');
  return i > 0
    ? [title.slice(0, i), title.slice(i + 3)]
    : [title, 'Percona Documentation'];
}

function productFirst(hits, product, getProduct) {
  if (!product) return hits;
  return [
    ...hits.filter((hit) => getProduct(hit) === product),
    ...hits.filter((hit) => getProduct(hit) !== product),
  ];
}

function isInScope(hit) {
  return Boolean(hit.url) && hit.url.startsWith(ALGOLIA_CONFIG.urlPrefix);
}

function resultsPageUrl(query, page) {
  const params = new URLSearchParams({ q: query });
  if (page > 0) params.set('p', String(page + 1));
  return `${ALGOLIA_CONFIG.resultsPage}?${params}`;
}

/* ---------- Search dropdown (DocSearch) ---------- */

function highlight(value) {
  return { value, matchLevel: 'full', matchedWords: [] };
}

// The index has page-level records without DocSearch's "hierarchy" field,
// so build it from the page title: product = group, page = result.
function toDocSearchHit(hit) {
  const [page, product] = splitTitle(hit.title);
  const pageHighlighted = splitTitle(hit._highlightResult?.title?.value || hit.title)[0];
  const description = hit._snippetResult?.description?.value || hit.description || '';

  return {
    ...hit,
    type: 'lvl1',
    content: null,
    hierarchy: {
      lvl0: product,
      lvl1: page,
      lvl2: null,
      lvl3: null,
      lvl4: null,
      lvl5: null,
      lvl6: null,
    },
    _highlightResult: {
      hierarchy: {
        lvl0: highlight(product),
        lvl1: highlight(pageHighlighted),
      },
    },
    _snippetResult: {
      hierarchy: { lvl1: highlight(pageHighlighted) },
      content: highlight(description),
    },
  };
}

docsearch({
  container: '#docsearch',
  appId: ALGOLIA_CONFIG.appId,
  apiKey: ALGOLIA_CONFIG.apiKey,
  indices: [
    {
      name: ALGOLIA_CONFIG.indexName,
      searchParameters: {
        hitsPerPage: 50,
        attributesToRetrieve: ['*'],
        attributesToHighlight: ['title'],
        attributesToSnippet: ['description:20'],
      },
    },
  ],
  maxResultsPerGroup: 10,
  transformSearchClient(searchClient) {
    return {
      ...searchClient,
      search: async (arg, ...rest) => {
        const requests = Array.isArray(arg) ? arg : arg.requests;
        let product = null;

        const newRequests = requests.map((request) => {
          const params = request.params || request;
          const { expanded, product: matched } = expandQuery(params.query);
          product = product || matched;
          return request.params
            ? { ...request, params: { ...request.params, query: expanded } }
            : { ...request, query: expanded };
        });

        const response = await searchClient.search(
          Array.isArray(arg) ? newRequests : { ...arg, requests: newRequests },
          ...rest
        );

        response.results = response.results.map((result) => {
          if (!result.hits) return result;
          const hits = productFirst(
            result.hits.map(toDocSearchHit),
            product,
            (hit) => hit.hierarchy.lvl0
          );
          return { ...result, hits };
        });

        return response;
      },
    };
  },
  transformItems(items) {
    return items.filter(isInScope);
  },
  resultsFooterComponent({ state }, { html }) {
    const total = state.context.nbHits;
    if (!total) return null;
    return html`<a class="DocSearch-SeeAll" href=${resultsPageUrl(state.query, 0)}>
      See all ${total} results →
    </a>`;
  },
});

/* ---------- Full results page ---------- */

async function searchAllResults(query, page) {
  const { expanded, product } = expandQuery(query);
  const response = await fetch(
    `https://${ALGOLIA_CONFIG.appId}-dsn.algolia.net/1/indexes/${encodeURIComponent(ALGOLIA_CONFIG.indexName)}/query`,
    {
      method: 'POST',
      headers: {
        'X-Algolia-Application-Id': ALGOLIA_CONFIG.appId,
        'X-Algolia-API-Key': ALGOLIA_CONFIG.apiKey,
      },
      body: JSON.stringify({
        query: expanded,
        page,
        hitsPerPage: ALGOLIA_CONFIG.resultsPerPage,
        attributesToRetrieve: ['title', 'url', 'description'],
        attributesToHighlight: ['title'],
        attributesToSnippet: ['description:30'],
        highlightPreTag: '<mark>',
        highlightPostTag: '</mark>',
      }),
    }
  );
  if (!response.ok) throw new Error(`Algolia returned ${response.status}`);
  const data = await response.json();
  data.hits = productFirst(
    data.hits.filter(isInScope),
    product,
    (hit) => splitTitle(hit.title)[1]
  );
  return data;
}

function renderResultItem(hit) {
  const [, product] = splitTitle(hit.title);
  const titleHtml = splitTitle(hit._highlightResult?.title?.value || hit.title)[0];
  const snippetHtml = hit._snippetResult?.description?.value || '';

  const item = document.createElement('li');
  item.className = 'algolia-result';

  const link = document.createElement('a');
  link.className = 'algolia-result-title';
  link.href = hit.url;
  link.innerHTML = titleHtml;

  const productEl = document.createElement('div');
  productEl.className = 'algolia-result-product';
  productEl.textContent = product;

  item.append(link, productEl);

  if (snippetHtml) {
    const snippet = document.createElement('p');
    snippet.className = 'algolia-result-snippet';
    snippet.innerHTML = snippetHtml;
    item.append(snippet);
  }

  const urlEl = document.createElement('div');
  urlEl.className = 'algolia-result-url';
  urlEl.textContent = hit.url;
  item.append(urlEl);

  return item;
}

function renderPagination(query, page, nbPages) {
  const nav = document.createElement('nav');
  nav.className = 'algolia-results-pagination';
  if (nbPages <= 1) return nav;

  if (page > 0) {
    const prev = document.createElement('a');
    prev.href = resultsPageUrl(query, page - 1);
    prev.textContent = '← Previous';
    nav.append(prev);
  }

  const info = document.createElement('span');
  info.textContent = `Page ${page + 1} of ${nbPages}`;
  nav.append(info);

  if (page < nbPages - 1) {
    const next = document.createElement('a');
    next.href = resultsPageUrl(query, page + 1);
    next.textContent = 'Next →';
    nav.append(next);
  }

  return nav;
}

async function initResultsPage() {
  const container = document.getElementById('algolia-results');
  if (!container) return;

  const params = new URLSearchParams(window.location.search);
  const query = (params.get('q') || '').trim();
  const page = Math.max(0, (parseInt(params.get('p'), 10) || 1) - 1);

  container.innerHTML = '';

  const form = document.createElement('form');
  form.className = 'algolia-results-form';
  form.action = ALGOLIA_CONFIG.resultsPage;
  form.method = 'get';
  const input = document.createElement('input');
  input.type = 'search';
  input.name = 'q';
  input.value = query;
  input.placeholder = 'Search the documentation';
  input.setAttribute('aria-label', 'Search the documentation');
  const button = document.createElement('button');
  button.type = 'submit';
  button.textContent = 'Search';
  form.append(input, button);
  container.append(form);

  const status = document.createElement('p');
  status.className = 'algolia-results-count';
  container.append(status);

  if (!query) {
    status.textContent = 'Type a search term to see results.';
    return;
  }

  status.textContent = 'Searching…';

  try {
    const data = await searchAllResults(query, page);
    status.textContent = `${data.nbHits} results for “${query}”`;

    if (data.hits.length === 0) return;

    const list = document.createElement('ol');
    list.className = 'algolia-results-list';
    list.start = page * ALGOLIA_CONFIG.resultsPerPage + 1;
    data.hits.forEach((hit) => list.append(renderResultItem(hit)));
    container.append(list, renderPagination(query, page, data.nbPages));
  } catch (error) {
    status.textContent = 'Search is not available right now. Please try again later.';
    console.error(error);
  }
}

initResultsPage();
