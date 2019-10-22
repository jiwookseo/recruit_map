import React, { useState } from 'react';
import { Map, InfoWindow, GoogleApiWrapper } from 'google-maps-react';
import CustomMarker from '../Marker';
import dotenv from 'dotenv';
dotenv.config();

const { REACT_APP_GOOGLE_API_KEY } = process.env;
const mapStyles = {
  width: '100%',
  height: '100%',
};

const GoogleMaps = props => {
  const [state, setState] = useState({
    markers: [
      {
        id: 1,
        lat: 37.505,
        lng: 127.0598,
        name: 'marker1',
      },
      {
        id: 2,
        lat: 37.507,
        lng: 127.0598,
        name: 'marker2',
      },
      {
        id: 3,
        lat: 37.509,
        lng: 127.0611,
        name: 'marker3',
      },
    ],
  });

  const markers = state.markers.map(marker => {
    return CustomMarker({ marker, google: props.google });
  });

  const handleClose = e => {
    console.log('HANDLE CLOSE', e);
  };
  return (
    <>
      <Map
        google={props.google}
        zoom={16}
        style={mapStyles}
        initialCenter={{ lat: 37.501, lng: 127.041 }}
      >
        {markers.map(v => v)}
        <InfoWindow onClose={handleClose}>
          <div>
            <h1>{this.state.selectedPlace.name}</h1>
          </div>
        </InfoWindow>
      </Map>
    </>
  );
};

export default GoogleApiWrapper({
  apiKey: REACT_APP_GOOGLE_API_KEY,
})(GoogleMaps);
