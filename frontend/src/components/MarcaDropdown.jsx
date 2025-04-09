// src/components/MarcaDropdown.jsx
import { useEffect, useState } from 'react';
import { fetchMarcas } from '../services/api';

export default function MarcaDropdown() {
  const [marcas, setMarcas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [erro, setErro] = useState(null);
  const [selected, setSelected] = useState('');

  useEffect(() => {
    const carregarMarcas = async () => {
      try {
        const data = await fetchMarcas();
        setMarcas(data);
      } catch (e) {
        setErro(e.message);
      } finally {
        setLoading(false);
      }
    };

    carregarMarcas();
  }, []);

  if (loading) return <p className="text-sm text-gray-500 animate-pulse">Carregando marcas...</p>;
  if (erro) return <p className="text-sm text-red-500">Erro: {erro}</p>;

  return (
    <div className="w-1/3 min-w-[280px] mx-auto">
      <div className="relative">
        <select
          value={selected}
          onChange={(e) => setSelected(e.target.value)}
          className="appearance-none w-full pl-4 pr-10 py-2 border border-gray-300 rounded-full text-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-black focus:border-black transition"
        >
          <option value="">Selecione uma marca</option>
          {marcas.map((marca) => (
            <option key={marca.id} value={marca.id}>
              {marca.nome}
            </option>
          ))}
        </select>

        {/* Ícone de lupa no canto direito */}
        <div className="pointer-events-none absolute inset-y-0 right-4 flex items-center">
          <svg
            className="w-4 h-4 text-gray-400"
            fill="none"
            stroke="currentColor"
            strokeWidth="2"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M21 21l-4.35-4.35m0 0A7 7 0 1110 3a7 7 0 016.65 9.65z"
            />
          </svg>
        </div>
      </div>
    </div>
  );
}
