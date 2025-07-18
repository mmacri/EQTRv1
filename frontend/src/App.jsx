import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import Horses from './pages/Horses';
import HorseProfile from './pages/HorseProfile';
import Races from './pages/Races';
import DataGrid from './pages/DataGrid';
import Problems from './pages/Problems';

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/horses" element={<Horses />} />
        <Route path="/horses/:id" element={<HorseProfile />} />
        <Route path="/races" element={<Races />} />
        <Route path="/grid" element={<DataGrid />} />
        <Route path="/problems" element={<Problems />} />
      </Routes>
    </BrowserRouter>
  );
}
