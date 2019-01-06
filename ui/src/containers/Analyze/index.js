import { connect } from 'react-redux';

import { store } from '../../index';

import Analyze from './template';

// For reducers... later..
const mapStateToProps = (state) => {
  return {

  }
};

const mapDispatchToProps = (dispatch) => ({

});

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Analyze);
