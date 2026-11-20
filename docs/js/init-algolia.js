/*
 * Algolia search for the Percona documentation, styled like the search on
 * www.percona.com: a search icon that expands into a search field, a results
 * popup with a "See all N results" button, and a full results page.
 *
 * - Searches the docs index on the Percona Algolia account.
 * - Shows only pages under ALGOLIA_CONFIG.urlPrefix
 *   (the whole docs set on the home page; a project's own path in a project).
 * - The full results page is any page containing <div id="algolia-results"></div>.
 */

const ALGOLIA_CONFIG = {
  appId: 'QPF6EL892Z',
  apiKey: '72ae01e59f74373372979e09001708fb',
  indexName: 'percona_docs_pages',
  urlPrefix: 'https://docs.percona.com/',
  scopeLabel: 'Documentation',
  placeholder: 'Search documentation...',
  resultsPage: '/search-results/',
  popupResults: 10,
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

const SEARCH_ICON =
  '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" ' +
  'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
  '<circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>';

/* ---------- Search helpers ---------- */

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

// "Page title - Product name" -> "Product name"
function productOf(title) {
  const i = (title || '').lastIndexOf(' - ');
  return i > 0 ? title.slice(i + 3) : '';
}

function isInScope(hit) {
  return Boolean(hit.url) && hit.url.startsWith(ALGOLIA_CONFIG.urlPrefix);
}

function resultsPageUrl(query, page) {
  const params = new URLSearchParams({ q: query });
  if (page > 0) params.set('p', String(page + 1));
  return `${ALGOLIA_CONFIG.resultsPage}?${params}`;
}

async function searchDocs(query, { page = 0, hitsPerPage = 20 } = {}) {
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
        hitsPerPage,
        attributesToRetrieve: ['title', 'url', 'description', 'image'],
        attributesToHighlight: ['title'],
        attributesToSnippet: ['description:40'],
        highlightPreTag: '<mark>',
        highlightPostTag: '</mark>',
      }),
    }
  );
  if (!response.ok) throw new Error(`Algolia returned ${response.status}`);
  const data = await response.json();

  let hits = data.hits.filter(isInScope);
  if (product) {
    hits = [
      ...hits.filter((hit) => productOf(hit.title) === product),
      ...hits.filter((hit) => productOf(hit.title) !== product),
    ];
  }
  return { hits, nbHits: data.nbHits, nbPages: data.nbPages };
}

/* ---------- Result card (same markup as www.percona.com) ---------- */

function renderHit(hit) {
  const item = document.createElement('li');
  item.className = 'ais-Hits-item';

  const link = document.createElement('a');
  link.className = 'hit-link';
  link.href = hit.url;

  if (hit.image) {
    const imgWrap = document.createElement('div');
    imgWrap.className = 'c_img';
    const img = document.createElement('img');
    img.src = hit.image;
    img.alt = '';
    img.loading = 'lazy';
    img.addEventListener('error', () => imgWrap.remove());
    imgWrap.append(img);
    link.append(imgWrap);
  }

  const body = document.createElement('div');
  body.className = 'c_body';

  const title = document.createElement('div');
  title.className = 'row1';
  // Algolia escapes the record text; only its <mark> tags are HTML.
  title.innerHTML = hit._highlightResult?.title?.value || hit.title || hit.url;

  const desc = document.createElement('div');
  desc.className = 'c_desc';
  desc.innerHTML = hit._snippetResult?.description?.value || '';

  body.append(title, desc);
  link.append(body);
  item.append(link);
  return item;
}

function renderHitList(hits) {
  const list = document.createElement('ol');
  list.className = 'ais-Hits-list';
  hits.forEach((hit) => list.append(renderHit(hit)));
  const wrap = document.createElement('div');
  wrap.className = 'ais-Hits';
  wrap.append(list);
  return wrap;
}

function plural(n) {
  return `${n} result${n === 1 ? '' : 's'}`;
}

/* ---------- Header search (icon, search field, popup) ---------- */

function initHeaderSearch() {
  const container = document.getElementById('docsearch');
  if (!container) return;

  const root = document.createElement('div');
  root.className = 'topbar-search';
  root.innerHTML = `
    <button type="button" class="search-icon-btn" aria-label="Open search">${SEARCH_ICON}</button>
    <div class="search-input-wrap">
      <form class="ais-SearchBox-form" role="search" novalidate>
        <input class="ais-SearchBox-input" type="search" name="q"
          autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" maxlength="512"
          role="combobox" aria-expanded="false" aria-controls="search-popup" aria-autocomplete="list">
      </form>
      <button type="button" class="search-collapse-btn" aria-label="Close search">×</button>
    </div>
    <div class="sr-only" aria-live="polite"></div>
    <div id="search-popup" class="search-popup" role="region" aria-label="Search suggestions">
      <div class="tabs" role="tablist" aria-label="Search sources">
        <button type="button" class="tab active" role="tab" aria-selected="true" tabindex="-1"></button>
      </div>
      <div class="results active" role="tabpanel"><div class="hits"></div></div>
      <div class="popup-footer">
        <span class="popup-summary"></span>
        <a class="see-all-link" href="#"></a>
      </div>
    </div>`;
  container.prepend(root);

  const iconBtn = root.querySelector('.search-icon-btn');
  const inputWrap = root.querySelector('.search-input-wrap');
  const form = root.querySelector('form');
  const input = root.querySelector('.ais-SearchBox-input');
  const closeBtn = root.querySelector('.search-collapse-btn');
  const live = root.querySelector('[aria-live]');
  const popup = root.querySelector('.search-popup');
  const tab = root.querySelector('.tab');
  const results = root.querySelector('.results');
  const hitsEl = root.querySelector('.hits');
  const summary = root.querySelector('.popup-summary');
  const seeAll = root.querySelector('.see-all-link');

  input.placeholder = ALGOLIA_CONFIG.placeholder;
  input.setAttribute('aria-label', ALGOLIA_CONFIG.placeholder.replace(/\.+$/, ''));

  let lastQuery = '';
  let requestId = 0;
  let debounce = null;
  let activeIndex = -1;

  // Below 1560px the field and popup open as a floating panel under the header.
  function updatePositions() {
    const header = document.querySelector('.md-header') || container;
    const headerBottom = header.getBoundingClientRect().bottom;
    root.style.setProperty('--search-drop-top', `${headerBottom + 8}px`);
    const wrapBottom = inputWrap.getBoundingClientRect().bottom;
    root.style.setProperty('--search-popup-top', `${wrapBottom + 8}px`);
  }

  function expand() {
    if (root.classList.contains('expanded')) {
      input.focus();
      return;
    }
    root.classList.add('expanded');
    updatePositions();
    input.focus();
    if (input.value.trim()) openPopup();
  }

  function collapse() {
    closePopup();
    root.classList.remove('expanded');
    iconBtn.focus();
  }

  function openPopup() {
    updatePositions();
    popup.classList.add('open');
    input.setAttribute('aria-expanded', 'true');
  }

  function closePopup() {
    popup.classList.remove('open');
    input.setAttribute('aria-expanded', 'false');
    setActive(-1);
  }

  function links() {
    return [...hitsEl.querySelectorAll('.hit-link')];
  }

  function setActive(index) {
    const all = links();
    all.forEach((link) => link.classList.remove('is-active'));
    activeIndex = index;
    if (index >= 0 && all[index]) {
      all[index].classList.add('is-active');
      all[index].scrollIntoView({ block: 'nearest' });
    }
  }

  async function runSearch(query) {
    const id = ++requestId;
    try {
      const data = await searchDocs(query, { hitsPerPage: 50 });
      if (id !== requestId) return;

      const hits = data.hits.slice(0, ALGOLIA_CONFIG.popupResults);
      const total = data.nbHits;

      tab.innerHTML = '';
      tab.append(ALGOLIA_CONFIG.scopeLabel + ' ');
      const count = document.createElement('span');
      count.className = 'tab-count';
      count.textContent = `(${total})`;
      tab.append(count);

      hitsEl.innerHTML = '';
      results.classList.toggle('no-results', hits.length === 0);
      if (hits.length) hitsEl.append(renderHitList(hits));
      results.scrollTop = 0;
      activeIndex = -1;

      summary.textContent = `${plural(total)} in ${ALGOLIA_CONFIG.scopeLabel}`;
      seeAll.textContent = `See all ${plural(total)} →`;
      seeAll.href = resultsPageUrl(query, 0);
      seeAll.hidden = total === 0;
      live.textContent = `${plural(total)} in ${ALGOLIA_CONFIG.scopeLabel}.`;

      openPopup();
    } catch (error) {
      if (id !== requestId) return;
      hitsEl.innerHTML = '';
      results.classList.add('no-results');
      summary.textContent = 'Search is not available right now.';
      seeAll.hidden = true;
      openPopup();
      console.error(error);
    }
  }

  input.addEventListener('input', () => {
    const query = input.value.trim();
    clearTimeout(debounce);
    if (!query) {
      lastQuery = '';
      requestId++;
      closePopup();
      return;
    }
    debounce = setTimeout(() => {
      if (query === lastQuery && popup.classList.contains('open')) return;
      lastQuery = query;
      runSearch(query);
    }, 200);
  });

  input.addEventListener('focus', () => {
    if (input.value.trim() && hitsEl.childElementCount) openPopup();
  });

  input.addEventListener('keydown', (event) => {
    const all = links();
    if (event.key === 'ArrowDown' && all.length) {
      event.preventDefault();
      if (!popup.classList.contains('open')) openPopup();
      setActive(Math.min(activeIndex + 1, all.length - 1));
    } else if (event.key === 'ArrowUp' && all.length) {
      event.preventDefault();
      setActive(Math.max(activeIndex - 1, -1));
    } else if (event.key === 'Escape') {
      event.preventDefault();
      if (popup.classList.contains('open')) closePopup();
      else collapse();
    }
  });

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const all = links();
    if (activeIndex >= 0 && all[activeIndex]) {
      window.location.href = all[activeIndex].href;
      return;
    }
    const query = input.value.trim();
    if (query) window.location.href = resultsPageUrl(query, 0);
  });

  iconBtn.addEventListener('click', (event) => {
    event.stopPropagation();
    if (root.classList.contains('expanded')) input.focus();
    else expand();
  });

  closeBtn.addEventListener('click', (event) => {
    event.stopPropagation();
    input.value = '';
    lastQuery = '';
    requestId++;
    hitsEl.innerHTML = '';
    collapse();
  });

  document.addEventListener('click', (event) => {
    if (!root.contains(event.target)) closePopup();
  });

  document.addEventListener('keydown', (event) => {
    const isShortcut = (event.metaKey || event.ctrlKey) && event.key.toLowerCase() === 'k';
    if (isShortcut) {
      event.preventDefault();
      expand();
    }
  });

  window.addEventListener('resize', () => {
    if (root.classList.contains('expanded')) updatePositions();
  });
  window.addEventListener('scroll', () => {
    if (root.classList.contains('expanded')) updatePositions();
  }, { passive: true });
}

/* ---------- Full results page ---------- */

function renderPagination(query, page, nbPages) {
  const nav = document.createElement('nav');
  nav.className = 'search-page-pagination';
  nav.setAttribute('aria-label', 'Search results pages');
  if (nbPages <= 1) return nav;

  const addLink = (label, target, current) => {
    if (current) {
      const span = document.createElement('span');
      span.className = 'page current';
      span.setAttribute('aria-current', 'page');
      span.textContent = label;
      nav.append(span);
      return;
    }
    const link = document.createElement('a');
    link.className = 'page';
    link.href = resultsPageUrl(query, target);
    link.textContent = label;
    nav.append(link);
  };

  if (page > 0) addLink('← Previous', page - 1, false);

  const first = Math.max(0, Math.min(page - 2, nbPages - 5));
  const last = Math.min(nbPages - 1, first + 4);
  for (let p = first; p <= last; p += 1) addLink(String(p + 1), p, p === page);

  if (page < nbPages - 1) addLink('Next →', page + 1, false);
  return nav;
}

async function initResultsPage() {
  const container = document.getElementById('algolia-results');
  if (!container) return;

  const params = new URLSearchParams(window.location.search);
  const query = (params.get('q') || '').trim();
  const page = Math.max(0, (parseInt(params.get('p'), 10) || 1) - 1);

  container.classList.add('search-page');
  container.innerHTML = `
    <form class="search-page-form" role="search" action="${ALGOLIA_CONFIG.resultsPage}" method="get">
      <input class="ais-SearchBox-input" type="search" name="q"
        autocomplete="off" spellcheck="false" maxlength="512">
      <button type="submit" class="search-page-submit">Search</button>
    </form>
    <div class="tabs" role="tablist" aria-label="Search sources">
      <span class="tab active" role="tab" aria-selected="true"></span>
    </div>
    <p class="search-page-summary" aria-live="polite"></p>
    <div class="search-page-results"></div>`;

  const input = container.querySelector('input');
  const tab = container.querySelector('.tab');
  const status = container.querySelector('.search-page-summary');
  const resultsEl = container.querySelector('.search-page-results');

  input.value = query;
  input.placeholder = ALGOLIA_CONFIG.placeholder;
  input.setAttribute('aria-label', ALGOLIA_CONFIG.placeholder.replace(/\.+$/, ''));
  tab.textContent = ALGOLIA_CONFIG.scopeLabel;

  if (!query) {
    status.textContent = 'Type a search term to see results.';
    input.focus();
    return;
  }

  status.textContent = 'Searching…';

  try {
    const data = await searchDocs(query, { page, hitsPerPage: ALGOLIA_CONFIG.resultsPerPage });

    const count = document.createElement('span');
    count.className = 'tab-count';
    count.textContent = ` (${data.nbHits})`;
    tab.append(count);

    status.textContent = `${plural(data.nbHits)} for “${query}” in ${ALGOLIA_CONFIG.scopeLabel}`;

    if (!data.hits.length) {
      resultsEl.classList.add('no-results');
      return;
    }
    resultsEl.append(renderHitList(data.hits), renderPagination(query, page, data.nbPages));
  } catch (error) {
    status.textContent = 'Search is not available right now. Please try again later.';
    console.error(error);
  }
}

initHeaderSearch();
initResultsPage();
