import React from 'react';
import useBaseUrl from '@docusaurus/useBaseUrl';

const PIN_DEFS = [
  { label: 'Grayhaven',         path: '/world/grayhaven-area/locations/grayhaven',         x: 18, y: 56 },
  { label: 'Stonefast',         path: '/world/highland-reaches/locations/stonefast',        x: 22, y: 30 },
  { label: 'Slew',              path: '/world/northern-wetlands/locations/slew',            x: 45, y: 70 },
  { label: 'Thile',             path: '/world/general/locations/thile',                     x: 68, y: 54 },
  { label: 'Alabaster Academy', path: '/world/general/locations/alabaster-academy',         x: 57, y: 65 },
  { label: 'Fort Pratchett',    path: '/world/the-barrens/locations/fort-pratchett',        x: 42, y: 78 },
  { label: 'Fort Prefect',      path: '/world/the-barrens/locations/fort-prefect',          x: 58, y: 78 },
  { label: 'Fort Ohmu',         path: '/world/the-barrens/locations/fort-ohmu',             x: 74, y: 79 },
  { label: 'Marsh Land',        path: '/world/starless-mire/locations/marsh-land',          x: 44, y: 83 },
];

function PinMarker({ label, path, x, y }) {
  const href = useBaseUrl(path);
  return (
    <div className="map-pin" style={{ left: `${x}%`, top: `${y}%` }}>
      <a href={href} className="pin-dot" aria-label={label} />
      <span className="pin-label">{label}</span>
    </div>
  );
}

export default function WorldMap() {
  const imgSrc = useBaseUrl('/img/greenwold-map.jpg');
  return (
    <div className="world-map-container">
      <img src={imgSrc} alt="Map of the Greenwold" />
      {PIN_DEFS.map((pin) => (
        <PinMarker key={pin.label} {...pin} />
      ))}
    </div>
  );
}
