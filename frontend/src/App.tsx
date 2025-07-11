import { useEffect, useState } from 'react';

function App() {
  const [config, setConfig] = useState(null);
  const API_URL = import.meta.env.VITE_API_URL;

  console.log(API_URL)

  useEffect(() => {
    fetch(`${API_URL}/api/config`)
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setConfig(data);
      });
  }, []);

  return (
    <div>
      <h1>공정 설정 정보</h1>
      {config ? (
        <pre>{JSON.stringify(config, null, 2)}</pre>
      ) : (
        <p>로딩 중...</p>
      )}

      <h2>📊 Dash 그래프</h2>
      <iframe
        src={`${API_URL}/dash/`}
        width="100%"
        height="600"
        style={{ border: '1px solid #ccc', borderRadius: '8px' }}
        title="Dash Graph"
      />
    </div>
  );
}

export default App;
