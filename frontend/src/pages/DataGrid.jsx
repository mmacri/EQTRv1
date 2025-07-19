import { useState, useEffect, useCallback } from 'react';
import api from '../api';

const resources = {
  horses: ['name', 'breed', 'age'],
  races: ['name', 'date', 'location'],
  'drug-tests': ['horse_id', 'race_id', 'result', 'date'],
};

export default function DataGrid() {
  const [resource, setResource] = useState('horses');
  const [items, setItems] = useState([]);
  const [form, setForm] = useState({});
  const [editingId, setEditingId] = useState(null);

  const fetchItems = useCallback(async () => {
    const res = await api.get(`/${resource}`);
    setItems(res.data);
  }, [resource]);

  const resetForm = useCallback(() => {
    const obj = {};
    resources[resource].forEach((f) => {
      obj[f] = '';
    });
    setForm(obj);
  }, [resource]);

  useEffect(() => {
    fetchItems();
    resetForm();
  }, [resource, fetchItems, resetForm]);

  async function handleSubmit(e) {
    e.preventDefault();
    if (editingId) {
      await api.put(`/${resource}/${editingId}`, form);
    } else {
      await api.post(`/${resource}`, form);
    }
    setEditingId(null);
    resetForm();
    fetchItems();
  }

  function startEdit(item) {
    setEditingId(item.id);
    const obj = {};
    resources[resource].forEach((f) => {
      obj[f] = item[f] || '';
    });
    setForm(obj);
  }

  async function deleteItem(id) {
    await api.delete(`/${resource}/${id}`);
    fetchItems();
  }

  return (
    <div>
      <h2>Admin Data Grid</h2>
      <select value={resource} onChange={(e) => setResource(e.target.value)}>
        {Object.keys(resources).map((r) => (
          <option key={r} value={r}>
            {r}
          </option>
        ))}
      </select>

      <form onSubmit={handleSubmit} style={{ margin: '1rem 0' }}>
        {resources[resource].map((f) => (
          <input
            key={f}
            placeholder={f}
            value={form[f]}
            onChange={(e) => setForm({ ...form, [f]: e.target.value })}
          />
        ))}
        <button type="submit">{editingId ? 'Update' : 'Add'}</button>
      </form>

      <table>
        <thead>
          <tr>
            {resources[resource].map((f) => (
              <th key={f}>{f}</th>
            ))}
            <th></th>
          </tr>
        </thead>
        <tbody>
          {items.map((item) => (
            <tr key={item.id}>
              {resources[resource].map((f) => (
                <td key={f}>{item[f]}</td>
              ))}
              <td>
                <button type="button" onClick={() => startEdit(item)}>
                  Edit
                </button>
                <button type="button" onClick={() => deleteItem(item.id)}>
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
