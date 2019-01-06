// Dependencies
import React from 'react';
import PropTypes from 'prop-types';

// Components
import Slider from '../../components/Slider';

// Styles
import './style.scss';

// Class
export default class PageTwo extends React.PureComponent {
  render() {
    return (
      <div className="page-two-container">
        <p>Page 2 Container</p>
        <p>Value 1: {this.props.value1}</p>
        <p>Value 2: {this.props.value2}</p>
        <Slider
          value={this.props.value2}
          onChange={this.props.onUpdateValue}
          min={0}
          max={100}>
        </Slider>
      </div>
    );
  }
}

// Class Prop
PageTwo.propTypes = {
  sliderValue: PropTypes.number,
  value1: PropTypes.number,
  value2: PropTypes.number,
  onUpdateValue: PropTypes.func
};
