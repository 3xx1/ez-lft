import { fromJS } from 'immutable';

import {
  UPDATE_VALUE
} from './constants';

const initialState = fromJS({
  value: 30
});

function pageTwoReducer(state = initialState, action) {
  switch(action.type) {
    case UPDATE_VALUE:
      return state
        .set('value', action.value);

    default:
      return state;
  }
}

export default pageTwoReducer;
