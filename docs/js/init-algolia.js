const PRODUCT_ABBREVIATIONS = {
  pxb: 'Percona XtraBackup',
  pxc: 'Percona XtraDB Cluster',
  psmdb: 'Percona Server for MongoDB',
  pbm: 'Percona Backup for MongoDB',
  pmm: 'Percona Monitoring and Management',
  pt: 'Percona Toolkit',
};

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

function splitTitle(title) {
  title = title || '';
  const i = title.lastIndexOf(' - ');
  return i > 0
    ? [title.slice(0, i), title.slice(i + 3)]
    : [title, 'Percona Documentation'];
}

function highlight(value) {
  return { value, matchLevel: 'full', matchedWords: [] };
}

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
  appId: 'QPF6EL892Z',
  apiKey: '72ae01e59f74373372979e09001708fb',
  indices: [
    {
      name: 'percona_docs_pages',
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
      search: async (...args) => {
        const response = await searchClient.search(...args);
        response.results = response.results.map((result) =>
          result.hits ? { ...result, hits: result.hits.map(toDocSearchHit) } : result
        );
        return response;
      },
    };
  },
  transformItems(items) {
    return items.filter(
      (item) => item.url && item.url.startsWith('https://docs.percona.com/')
    );
  },
});
