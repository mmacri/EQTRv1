import { useState, useEffect } from 'react';
import api from '../api';

export default function Races() {
  const [races, setRaces] = useState([]);
  const [form, setForm] = useState({ name: '', date: '', location: '' });
  const [editingId, setEditingId] = useState(null);

  useEffect(() => {
    fetchRaces();
  }, []);

  async function fetchRaces() {
    const res = await api.get('/races');
    setRaces(res.data);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (editingId) {
      await api.put(`/races/${editingId}`, form);
    } else {
      await api.post('/races', form);
    }
    setForm({ name: '', date: '', location: '' });
    setEditingId(null);
    fetchRaces();
  }

  function startEdit(race) {
    setEditingId(race.id);
    setForm({
      name: race.name || '',
      date: race.date || '',
      location: race.location || '',
    });
  }

  async function deleteRace(id) {
    await api.delete(`/races/${id}`);
    fetchRaces();
  }

  return (
    <div>
      <h2>Races</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: '1rem' }}>
        <input
          placeholder="Name"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />
        <input
          type="date"
          value={form.date}
          onChange={(e) => setForm({ ...form, date: e.target.value })}
        />
        <input
          placeholder="Location"
          value={form.location}
          onChange={(e) => setForm({ ...form, location: e.target.value })}
        />
        <button type="submit">{editingId ? 'Update' : 'Add'}</button>
      </form>

      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Date</th>
            <th>Location</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {races.map((r) => (
            <tr key={r.id}>
              <td>{r.name}</td>
              <td>{r.date}</td>
              <td>{r.location}</td>
              <td>
                <button type="button" onClick={() => startEdit(r)}>
                  Edit
                </button>
                <button type="button" onClick={() => deleteRace(r.id)}>
                  Delete
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
