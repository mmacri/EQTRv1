import { useEffect, useState } from 'react';
import api from '../api';

export default function Dashboard() {
  const [stats, setStats] = useState({ horses: 0, races: 0, tests: 0 });

  useEffect(() => {
    async function load() {
      const [h, r, t] = await Promise.all([
        api.get('/horses'),
        api.get('/races'),
        api.get('/drug-tests'),
      ]);
      setStats({ horses: h.data.length, races: r.data.length, tests: t.data.length });
    }

    load();
  }, []);

  return (
    <div>
      <h2>Dashboard</h2>
      <p>Horses: {stats.horses}</p>
      <p>Races: {stats.races}</p>
      <p>Drug Tests: {stats.tests}</p>
    </div>
  );
}
