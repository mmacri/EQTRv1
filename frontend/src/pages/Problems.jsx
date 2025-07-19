import { useEffect, useState } from 'react';
import api from '../api';

export default function Problems() {
  const [failedTests, setFailedTests] = useState([]);

  useEffect(() => {
    fetchProblems();
  }, []);

  async function fetchProblems() {
    const res = await api.get('/drug-tests');
    setFailedTests(res.data.filter((d) => d.result === 'fail'));
  }

  return (
    <div>
      <h2>Failed Drug Tests</h2>
      <table>
        <thead>
          <tr>
            <th>Horse</th>
            <th>Race</th>
            <th>Date</th>
            <th>Result</th>
          </tr>
        </thead>
        <tbody>
          {failedTests.map((t) => (
            <tr key={t.id}>
              <td>{t.horse_id}</td>
              <td>{t.race_id}</td>
              <td>{t.date}</td>
              <td>{t.result}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
