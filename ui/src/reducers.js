// Dependencies
import { fromJS } from 'immutable';
import { combineReducers } from 'redux-immutable';
import { LOCATION_CHANGE } from 'react-router-redux';

// Children Reducers
import globalReducer from './containers/_App/redux/reducer';
import pageOneReducer from './containers/PageOne/redux/reducer';
import pageTwoReducer from './containers/PageTwo/redux/reducer';

// Initial routing state
const routeInitialState = fromJS({
  location: null,
});

// Route Reducer
function routeReducer(state = routeInitialState, action) {
  switch (action.type) {
    case LOCATION_CHANGE:
      return state.merge({
        location: action.payload,
      });
    default:
      return state;
  }
}

export default function createReducer(injectedReducers) {
  return combineReducers({
    route: routeReducer,
    global: globalReducer,
    pageOne: pageOneReducer,
    pageTwo: pageTwoReducer,
    ...injectedReducers
  });
}
