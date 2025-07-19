import { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../api';

export default function Horses() {
  const [horses, setHorses] = useState([]);
  const [form, setForm] = useState({ name: '', breed: '', age: '' });
  const [editingId, setEditingId] = useState(null);

  useEffect(() => {
    fetchHorses();
  }, []);

  async function fetchHorses() {
    const res = await api.get('/horses');
    setHorses(res.data);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    if (editingId) {
      await api.put(`/horses/${editingId}`, form);
    } else {
      await api.post('/horses', form);
    }
    setForm({ name: '', breed: '', age: '' });
    setEditingId(null);
    fetchHorses();
  }

  function startEdit(horse) {
    setEditingId(horse.id);
    setForm({
      name: horse.name || '',
      breed: horse.breed || '',
      age: horse.age || '',
    });
  }

  async function deleteHorse(id) {
    await api.delete(`/horses/${id}`);
    fetchHorses();
  }

  return (
    <div>
      <h2>Horses</h2>
      <form onSubmit={handleSubmit} style={{ marginBottom: '1rem' }}>
        <input
          placeholder="Name"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />
        <input
          placeholder="Breed"
          value={form.breed}
          onChange={(e) => setForm({ ...form, breed: e.target.value })}
        />
        <input
          type="number"
          placeholder="Age"
          value={form.age}
          onChange={(e) => setForm({ ...form, age: e.target.value })}
        />
        <button type="submit">{editingId ? 'Update' : 'Add'}</button>
      </form>

      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Breed</th>
            <th>Age</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          {horses.map((h) => (
            <tr key={h.id}>
              <td>
                <Link to={`/horses/${h.id}`}>{h.name}</Link>
              </td>
              <td>{h.breed}</td>
              <td>{h.age}</td>
              <td>
                <button type="button" onClick={() => startEdit(h)}>
                  Edit
                </button>
                <button type="button" onClick={() => deleteHorse(h.id)}>
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
