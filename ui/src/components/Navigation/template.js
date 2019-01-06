import React from 'react';
import PropTypes from 'prop-types';
import './style.scss';

const Navigation = (props) => {
  return (
    <div className="navigation-component">
      <div className="row">
        <div className="col-sm-2">
          <p>Analyze</p>
        </div>
        <div className="col-sm-2">
          <p>Results</p>
        </div>
      </div>
    </div>
  );
};

Navigation.propTypes = {
}

export default Navigation;
