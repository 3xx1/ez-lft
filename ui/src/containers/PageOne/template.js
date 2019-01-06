// Dependencies
import React from 'react';
import PropTypes from 'prop-types';

// Styles
import './style.scss';

// Class
export default class PageOne extends React.PureComponent {
  render() {
    return (
      <div className="page-one-container">
        <p>Page 1 Container</p>
        <p>Value 1: {this.props.value1}</p>
        <p>Value 2: {this.props.value2}</p>
        <button onClick={this.props.onIncrement}>Increment</button>
        <button onClick={this.props.onDecrement}>Decrement</button>
      </div>
    );
  }
}

// Class Prop
PageOne.propTypes = {
  value1: PropTypes.number,
  value2: PropTypes.number,
  onIncrement: PropTypes.func,
  onDecrement: PropTypes.func
};
