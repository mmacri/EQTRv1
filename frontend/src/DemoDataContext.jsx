import { createContext, useState, useContext } from 'react';

const DemoDataContext = createContext();

export function DemoDataProvider({ children }) {
  const [useDemoData, setUseDemoData] = useState(true);
  const toggleDemoData = () => setUseDemoData(v => !v);

  return (
    <DemoDataContext.Provider value={{ useDemoData, toggleDemoData }}>
      {children}
    </DemoDataContext.Provider>
  );
}

export function useDemoData() {
  return useContext(DemoDataContext);
}
