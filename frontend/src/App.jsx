import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Horses from './pages/Horses';
import HorseProfile from './pages/HorseProfile';
import Races from './pages/Races';
import DataGrid from './pages/DataGrid';
import Problems from './pages/Problems';
import AdminLayout from './pages/admin/AdminLayout';
import AdminDashboard from './pages/admin/Dashboard';
import AdminHorses from './pages/admin/Horses';
import AdminOwners from './pages/admin/Owners';
import AdminRaces from './pages/admin/Races';
import AdminSeasons from './pages/admin/Seasons';
import { DemoDataProvider } from './DemoDataContext';

export default function App() {
  return (
    <DemoDataProvider>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/horses" element={<Horses />} />
        <Route path="/horses/:id" element={<HorseProfile />} />
        <Route path="/races" element={<Races />} />
        <Route path="/grid" element={<DataGrid />} />
        <Route path="/problems" element={<Problems />} />
        <Route path="/admin" element={<AdminLayout />}> 
          <Route index element={<AdminDashboard />} />
          <Route path="dashboard" element={<AdminDashboard />} />
          <Route path="horses" element={<AdminHorses />} />
          <Route path="owners" element={<AdminOwners />} />
          <Route path="races" element={<AdminRaces />} />
          <Route path="seasons" element={<AdminSeasons />} />
        </Route>
      </Routes>
    </BrowserRouter>
    </DemoDataProvider>
  );
}
