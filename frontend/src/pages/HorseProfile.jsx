import { useParams, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import api from '../api';

export default function HorseProfile() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [horse, setHorse] = useState(null);

  useEffect(() => {
    async function fetchHorse() {
      const res = await api.get(`/horses/${id}`);
      setHorse(res.data);
    }
    fetchHorse();
  }, [id]);

  async function handleSubmit(e) {
    e.preventDefault();
    await api.put(`/horses/${id}`, horse);
    navigate('/horses');
  }

  if (!horse) return <div>Loading...</div>;

  return (
    <div>
      <h2>Edit Horse</h2>
      <form onSubmit={handleSubmit}>
        <input
          placeholder="Name"
          value={horse.name}
          onChange={(e) => setHorse({ ...horse, name: e.target.value })}
        />
        <input
          placeholder="Breed"
          value={horse.breed || ''}
          onChange={(e) => setHorse({ ...horse, breed: e.target.value })}
        />
        <input
          type="number"
          placeholder="Age"
          value={horse.age || ''}
          onChange={(e) => setHorse({ ...horse, age: e.target.value })}
        />
        <button type="submit">Save</button>
      </form>
    </div>
  );
}
