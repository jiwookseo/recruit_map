import React from 'react';
import { Marker } from 'google-maps-react';

const CustomMarker = () => {
  return (
    <Marker
      title={'Marker Component'}
      name={'Marker Component'}
      position={{ lat: 37.5018, lng: 127.0399 }}
    />
  );
};
export default CustomMarker;
