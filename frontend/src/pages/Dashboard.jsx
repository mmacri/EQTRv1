import { useEffect, useState } from 'react';
import api from '../api';

export default function Dashboard() {
  const [counts, setCounts] = useState({ red: 0, yellow: 0, green: 0, grey: 0 });

  const load = () => {
    api.get('/horses').then((res) => {
      const c = { red: 0, yellow: 0, green: 0, grey: 0 };
      res.data.forEach((h) => {
        if (h.status === 'inactive') c.grey += 1;
        else if (!h.location) c.yellow += 1;
        else c.green += 1;
      });
      setCounts(c);
    });
  };

  useEffect(() => {
    load();
    const ws = new WebSocket(`ws://${window.location.host}/api/v1/ws/status`);
    ws.onmessage = load;
    return () => ws.close();
  }, []);

  return (
    <div>
      <h2>Horse Status Overview</h2>
      <ul style={{ listStyle: 'none', padding: 0, display: 'flex', gap: '1rem' }}>
        <li style={{ color: 'red' }}>Red: {counts.red}</li>
        <li style={{ color: 'orange' }}>Yellow: {counts.yellow}</li>
        <li style={{ color: 'green' }}>Green: {counts.green}</li>
        <li style={{ color: 'gray' }}>Grey: {counts.grey}</li>
      </ul>
    </div>
  );
}
