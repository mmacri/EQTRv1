import { useEffect, useState } from 'react';
import api from '../api';

export default function DataGrid() {
  const [horses, setHorses] = useState([]);

  useEffect(() => {
    api.get('/horses').then((res) => setHorses(res.data));
  }, []);

  const updateField = (id, field, value) => {
    setHorses((hs) => hs.map((h) => (h.id === id ? { ...h, [field]: value } : h)));
  };

  const save = () => {
    api
      .post('/horses/bulk_update', horses)
      .then(() => alert('Saved'))
      .catch(() => alert('Error'));
  };

  return (
    <div>
      <h2>Horse Data Grid</h2>
      <table border="1" cellPadding="4">
        <thead>
          <tr>
            <th>Name</th>
            <th>Breed</th>
            <th>Location</th>
          </tr>
        </thead>
        <tbody>
          {horses.map((h) => (
            <tr key={h.id}>
              <td>
                <input value={h.name} onChange={(e) => updateField(h.id, 'name', e.target.value)} />
              </td>
              <td>
                <input value={h.breed || ''} onChange={(e) => updateField(h.id, 'breed', e.target.value)} />
              </td>
              <td>
                <input value={h.location || ''} onChange={(e) => updateField(h.id, 'location', e.target.value)} />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={save}>Save</button>
    </div>
  );
}
