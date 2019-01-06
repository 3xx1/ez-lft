import { fromJS } from 'immutable';

import {
  INCREMENT,
  DECREMENT
} from './constants';

const initialState = fromJS({
  value: 0
});

function pageOneReducer(state = initialState, action) {
  switch(action.type) {
    case INCREMENT:
      return state
        .set('value', state.get('value') + 1);

    case DECREMENT:
      return state
        .set('value', state.get('value') - 1);

    default:
      return state;
  }
}

export default pageOneReducer;
