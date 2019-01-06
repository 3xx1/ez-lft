import {
  UPDATE_INDEX
} from './constants';

// Example Action
export function updateIndex(index) {
  return {
    type: UPDATE_INDEX,
    index
  };
}
