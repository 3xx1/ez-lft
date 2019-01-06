import { fromJS } from 'immutable';

import {
  UPDATE_INDEX
} from './constants';

const initialState = fromJS({
  index: 0
});

function appReducer(state = initialState, action) {
  switch(action.type) {
    case UPDATE_INDEX:
      return state
        .set('index', action.index);
    default:
      return state;
  }
}

export default appReducer;
