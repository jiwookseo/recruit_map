import React from 'react';
import { Marker } from 'google-maps-react';

const CustomMarker = ({ marker, google }) => {
  return (
    <Marker
      key={marker.id}
      name={marker.name}
      position={{ lat: marker.lat, lng: marker.lng }}
      icon={{
        url: 'https://image.flaticon.com/icons/png/512/57/57113.png',
        anchor: new google.maps.Point(32, 32),
        scaledSize: new google.maps.Size(32, 32),
        scale: 0.05,
      }}
    />
  );
};

export default CustomMarker;
