// src/components/MarcaDropdown.jsx
import { useEffect, useState } from 'react';
import { fetchMarcas } from '../services/api';

export default function MarcaDropdown({ onChange }) {
  const [marcas, setMarcas] = useState([]);
  const [selected, setSelected] = useState('');
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    fetchMarcas()
      .then(setMarcas)
      .catch((e) => setErro(e.message))
      .finally(() => setLoading(false));
  }, []);

  const handleChange = (e) => {
    const value = e.target.value;
    setSelected(value);
    onChange && onChange(value); // passa o id da marca pro componente pai
  };

  if (loading) return <p className="text-sm text-gray-500 animate-pulse">Carregando marcas...</p>;
  if (erro) return <p className="text-sm text-red-500">Erro: {erro}</p>;

  return (
    <div className="w-1/3 min-w-[280px] mx-auto">
      <div className="relative">
        <select
          value={selected}
          onChange={handleChange}
          className="appearance-none w-full pl-4 pr-10 py-2 border border-gray-300 rounded-full text-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-black focus:border-black transition"
        >
          <option value="">Selecione uma marca</option>
          {marcas.map((marca) => (
            <option key={marca.id} value={marca.id}>
              {marca.nome}
            </option>
          ))}
        </select>
      </div>
    </div>
  );
}
