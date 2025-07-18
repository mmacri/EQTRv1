import { useParams } from 'react-router-dom';

export default function HorseProfile() {
  const { id } = useParams();
  return <div>Horse Profile {id}</div>;
}
