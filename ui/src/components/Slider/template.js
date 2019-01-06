import React from 'react';
import PropTypes from 'prop-types';
import './style.scss';

const Slider = (props) => {
  return (
    <div className="slider-component">
      <input type="range" min={props.min} max={props.max} value={props.value} onChange={props.onChange} />
    </div>
  );
};

Slider.propTypes = {
  value: PropTypes.number,
  max: PropTypes.number,
  min: PropTypes.number
}

export default Slider;
