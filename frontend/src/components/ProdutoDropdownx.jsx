// src/components/ProdutoDropdown.jsx
import { useEffect, useState } from 'react';
import { fetchProdutosPorMarca } from '../services/api';

export default function ProdutoDropdown({ marcaId }) {
  const [produtos, setProdutos] = useState([]);
  const [selected, setSelected] = useState('');
  const [loading, setLoading] = useState(false);
  const [erro, setErro] = useState(null);

  useEffect(() => {
    if (!marcaId) return;
    setLoading(true);
    fetchProdutosPorMarca(marcaId)
      .then(setProdutos)
      .catch((e) => setErro(e.message))
      .finally(() => setLoading(false));
  }, [marcaId]);

  if (!marcaId) return null;
  if (loading) return <p className="text-sm text-gray-500 animate-pulse">Carregando produtos...</p>;
  if (erro) return <p className="text-sm text-red-500">Erro: {erro}</p>;

  return (
    <div className="w-1/3 min-w-[280px] mx-auto mt-6">
      <select
        value={selected}
        onChange={(e) => setSelected(e.target.value)}
        className="appearance-none w-full pl-4 pr-10 py-2 border border-gray-300 rounded-full text-sm shadow-sm focus:outline-none focus:ring-2 focus:ring-black focus:border-black transition"
      >
        <option value="">Selecione um produto</option>
        {produtos.map((p) => (
          <option key={p.id} value={p.id}>
            {p.nome}
          </option>
        ))}
      </select>
    </div>
  );
}
