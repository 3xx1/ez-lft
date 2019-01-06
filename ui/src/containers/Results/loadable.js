import Loadable from 'react-loadable';

// Loading Placeholder just to fulfill Loadable module requirements
import React from 'react';
function Loading() {
  return <div>Loading...</div>;
}

export default Loadable({
  loader: () => import('./index.js'),
  loading: Loading
});
