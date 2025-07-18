import { useEffect, useState } from 'react';
import api from '../../api';
import { useDemoData } from '../../DemoDataContext';

const demoHorses = [
  { id: '1', name: 'Demo Horse 1', breed: 'Thoroughbred' },
  { id: '2', name: 'Demo Horse 2', breed: 'Arabian' },
];

export default function AdminHorses() {
  const { useDemoData: demoEnabled } = useDemoData();
  const [horses, setHorses] = useState([]);
  const [name, setName] = useState('');
  const [breed, setBreed] = useState('');

  useEffect(() => {
    if (demoEnabled) {
      setHorses(demoHorses);
    } else {
      api.get('/horses').then((res) => setHorses(res.data)).catch(() => setHorses([]));
    }
  }, [demoEnabled]);

  const addHorse = () => {
    api.post('/horses', { name, breed }).then((res) => setHorses((h) => [...h, res.data]));
  };

  const delHorse = (id) => {
    api.delete(`/horses/${id}`).then(() => setHorses((h) => h.filter((x) => x.id !== id)));
  };

  return (
    <div>
      <h2>Manage Horses</h2>
      <ul>
        {horses.map((h) => (
          <li key={h.id}>
            {h.name} - {h.breed}{' '}
            {!demoEnabled && <button onClick={() => delHorse(h.id)}>Delete</button>}
          </li>
        ))}
      </ul>
      {!demoEnabled && (
        <div style={{ marginTop: '1rem' }}>
          <input placeholder="Name" value={name} onChange={(e) => setName(e.target.value)} />
          <input placeholder="Breed" value={breed} onChange={(e) => setBreed(e.target.value)} />
          <button onClick={addHorse}>Add</button>
        </div>
      )}
    </div>
  );
}
