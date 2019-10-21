import React, { useState } from 'react';
import { Map, GoogleApiWrapper, Marker, InfoWindow } from 'google-maps-react';
import dotenv from 'dotenv';
import CustomMarker from './CustomMarker';
dotenv.config();

const { REACT_APP_GOOGLE_API_KEY } = process.env;
const mapStyles = {
  width: '100%',
  height: '100%',
};

const GoogleMaps = props => {
  console.log(props);
  const onMouseoverMarker = e => {
    console.log('onMouseoverMarker');
    console.log(e);
  };
  const onClickMarker = e => {
    console.log('onClickMarker');
  };
  const [state, setState] = useState({
    showingInfoWindow: false,
    activeMarker: {},
    selectedPlace: {},
  });

  const onMarkerClick = (props, marker, e) => {
    setState({
      showingInfoWindow: true,
      activeMarker: marker,
      selectedPlace: props,
    });
  };
  const onMapClicked = props => {
    console.log(props.google);
    if (state.showingInfoWindow) {
      console.log('if showingInfoWindow');
      setState({
        showingInfoWindow: false,
        activeMarker: null,
      });
    }
  };

  return (
    <>
      <Map
        google={props.google}
        zoom={16}
        style={mapStyles}
        initialCenter={{ lat: 37.501, lng: 127.041 }}
        onClick={onMapClicked}
      >
        <Marker
          onMouseover={onMouseoverMarker}
          onClick={onClickMarker}
          title={'TEST_title'}
          name={'TEST_name'}
          position={{ lat: 37.5012, lng: 127.0396 }}
          icon={{
            url: 'https://image.flaticon.com/icons/png/512/57/57113.png',
            anchor: new props.google.maps.Point(32, 32),
            scaledSize: new props.google.maps.Size(32, 32),
            scale: 0.05,
          }}
        />
        <Marker onClick={onMarkerClick} name={'Current Location'} />
        <InfoWindow
          marker={state.activeMarker}
          visible={state.showingInfoWindow}
        >
          <div>
            <h1>{state.selectedPlace ? state.selectedPlace.name : ''}</h1>
          </div>
        </InfoWindow>
      </Map>
    </>
  );
};

export default GoogleApiWrapper({
  apiKey: REACT_APP_GOOGLE_API_KEY,
})(GoogleMaps);
