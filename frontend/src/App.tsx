import { useEffect, useState } from 'react';

function App() {
  const [config, setConfig] = useState<any>(null);
  const [inputValue, setInputValue] = useState('');
  const [postResponse, setPostResponse] = useState('');
  const API_URL = import.meta.env.VITE_API_URL;

  useEffect(() => {
    fetch(`${API_URL}/api/config`)
      .then(res => res.json())
      .then(data => setConfig(data));
  }, []);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const response = await fetch(`${API_URL}/api/config`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ userText: inputValue })
    });
    const result = await response.json();
    setPostResponse(result.message);
    setInputValue(''); // 입력창 초기화
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>공정 설정 정보</h1>
      {config ? (
        <pre>{JSON.stringify(config, null, 2)}</pre>
      ) : (
        <p>로딩 중...</p>
      )}

      <h2>사용자 입력</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="설정을 입력하세요"
        />
        <button type="submit">서버에 보내기</button>
      </form>
      {postResponse && <p style={{ color: "green" }}>{postResponse}</p>}

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
