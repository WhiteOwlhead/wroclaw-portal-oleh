import React from 'react';
//import { Wrapper, Status } from '@googlemaps/react-wrapper';
import { GoogleMap, LoadScript } from '@react-google-maps/api';

const containerStyle = {
  width: '700px',
  height: '600px',
};
const center = {
  lat: 49.5612723349586,
  lng: 25.603162164347435,
};

const GoogleMapComponent = () => {
  return (
    <center>
      {' '}
      <br /> <br />
      <div>
        <LoadScript googleMapsApiKey="AIzaSyBr6cQlTB8LQ1Rwf9ZZqIFfc7vl-2gxduk">
          <GoogleMap
            mapContainerStyle={containerStyle}
            center={center}
            zoom={10}
          >
            {/* Child components, such as markers, info windows, etc. */}
            <></>
          </GoogleMap>
        </LoadScript>
      </div>
    </center>
  );
};

export default GoogleMapComponent;
