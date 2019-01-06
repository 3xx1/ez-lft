import { connect } from 'react-redux';

import { store } from '../../index';

import PageOne from './template';
import * as PageOneActions from './redux/actions';

const mapStateToProps = (state) => {
  return {
    value1: state.get('pageOne').get('value'),
    value2: state.get('pageTwo').get('value')
  }
};

const mapDispatchToProps = (dispatch) => ({
  onIncrement: () => store.dispatch(PageOneActions.increment()),
  onDecrement: () => store.dispatch(PageOneActions.decrement())
});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(PageOne);
