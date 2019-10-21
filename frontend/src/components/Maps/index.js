import React, { useState } from 'react';
import { Map, GoogleApiWrapper, Marker, InfoWindow } from 'google-maps-react'
import CustomMarker from '../Marker';
import dotenv from 'dotenv'
dotenv.config();

const { REACT_APP_GOOGLE_API_KEY } = process.env
const mapStyles = {
  width: '100%',
  height: '100%',
};


const GoogleMaps = (props) => {
  const [state, setState] = useState({
    markers: [
      {
        id: 1,
        lat: 37.51,
        lng: 127.08,
        name: 'marker1'
      },
      {
        id: 2,
        lat: 37.55,
        lng: 127,
        name: 'marker2'
      },
      {
        id: 3,
        lat: 37.58,
        lng: 127.02,
        name: 'marker3'
      },
    ],
  });

  const markers = (
    state.markers.map(marker => {
      return (
        <CustomMarker marker={marker} google={props.google} />
      )
    })
  )

  return (
    <>
      <Map
        google={props.google}
        zoom={16}
        style={mapStyles}
        initialCenter={{ lat: 37.501, lng: 127.041}}
      >
        {markers}
      </Map>
    </>
  );
}

export default GoogleApiWrapper({
  apiKey: REACT_APP_GOOGLE_API_KEY
})(GoogleMaps)