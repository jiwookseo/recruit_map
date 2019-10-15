import React from 'react';
import { Map, GoogleApiWrapper } from 'google-maps-react'
import dotenv from 'dotenv'
dotenv.config();

const { REACT_APP_GOOGLE_API_KEY } = process.env
const mapStyles = {
  width: '100%',
  height: '100%',
};



const GoogleMaps = (props) => {
  return (
    <>
      <Map
        google={props.google}
        zoom={16}
        style={mapStyles}
        initialCenter={{ lat: 37.501, lng: 127.041}}
      />
    </>
  );
}

export default GoogleApiWrapper({
  apiKey: REACT_APP_GOOGLE_API_KEY
})(GoogleMaps)