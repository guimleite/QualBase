// src/services/api.js
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const fetchMarcas = async () => {
  const response = await fetch(`${API_URL}/api/v1/marcas`);
  if (!response.ok) {
    throw new Error('Erro ao buscar marcas');
  }
  return response.json();
};
