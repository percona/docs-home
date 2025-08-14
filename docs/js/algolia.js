import docsearch from '@docsearch/js';
import '@docsearch/css';  // You can skip this if already linked via CDN

docsearch({
  container: '#docsearch',
  appId: 'QDKRBCAI99',
  indexName: 'Percona documentation',
  apiKey: 'a5222c0ed6e9e6c67a77cfd2e26000e1'
});
