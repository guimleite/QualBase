import MarcaDropdown from './components/MarcaDropdown';

function App() {
  return (
    <div className="min-h-screen bg-white text-gray-800 font-sans flex flex-col">
      {/* Cabeçalho */}
      <header className="flex justify-between items-center px-6 py-8">
        <h2 className="text-sm font-bold">qual é a cor da base?</h2>
        <button className="bg-black text-white px-4 py-2 rounded hover:opacity-90 transition font-medium text-sm">
          Descobrir meu tom de base
        </button>
      </header>

      {/* Conteúdo centralizado */}
      <main className="flex-grow flex flex-col items-center justify-start pt-[12vh] px-4">
        <div className="max-w-xl w-full text-center">
          <h1 className="text-4xl font-bold mb-6 leading-tight">
            Descubra como <br /> encontrar sua cor de base
          </h1>
          <p className="text-gray-500 text-base md:text-lg leading-relaxed mb-14 max-w-xl mx-auto">
            Escolhendo seu tom aproximado nos seus produtos favoritos, você pode
            descobrir qual é o seu match perfeito em produtos similares! <br />
            Descubra como encontrar seu tom e cor de base ou corretivo ideal.
          </p>

          <div className="text-center max-w-md mx-auto">
            <h2 className="font-semibold text-lg mb-2">Passo 1</h2>
            <p className="text-gray-600 text-sm mb-4">
              Escolha uma marca de maquiagem que você já usa:
            </p>
            <div className="flex justify-center">
              <MarcaDropdown />
            </div>
          </div>

        </div>
      </main>
    </div>
  );
}

export default App;
