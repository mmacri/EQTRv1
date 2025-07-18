import { Link, Outlet } from 'react-router-dom';
import { useDemoData } from '../../DemoDataContext';

export default function AdminLayout() {
  const { useDemoData: demoEnabled, toggleDemoData } = useDemoData();
  return (
    <div>
      <nav>
        <ul style={{display: 'flex', gap: '1rem'}}>
          <li><Link to="dashboard">Dashboard</Link></li>
          <li><Link to="horses">Horses</Link></li>
          <li><Link to="owners">Owners</Link></li>
          <li><Link to="races">Races</Link></li>
          <li><Link to="seasons">Seasons</Link></li>
        </ul>
        <label style={{marginLeft: 'auto'}}>
          <input type="checkbox" checked={demoEnabled} onChange={toggleDemoData} />
          Use demo data
        </label>
      </nav>
      <Outlet />
    </div>
  );
}
