import React, { useState } from 'react';
import axios from 'axios';
import './styles.css'; // Import the CSS file

function App() {
  const [Gender, setGender] = useState('');
  const [Age, setAge] = useState('');
  const [Occupation, setOccupation] = useState('');
  const [StressLevel, setStressLevel] = useState('');
  const [output, setOutput] = useState('');

  const handleInputChange = (e, setInputFunction) => {
    setInputFunction(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/', {
        Gender,
        Age,
        Occupation,
        StressLevel
      });
      setOutput(response.data.output);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="container">
      <h1>Quality Of Sleep Predictor</h1> {/* Updated text */}
      <form onSubmit={handleSubmit} className="form">
        <div className="input-group">
          <label>Gender:</label>
          <input type="text" value={Gender} onChange={(e) => handleInputChange(e, setGender)} />
        </div>
        <div className="input-group">
          <label>Age:</label>
          <input type="text" value={Age} onChange={(e) => handleInputChange(e, setAge)} />
        </div>
        <div className="input-group">
          <label>Occupation:</label>
          <input type="text" value={Occupation} onChange={(e) => handleInputChange(e, setOccupation)} />
        </div>
        <div className="input-group">
          <label>Stress Level:</label>
          <input type="text" value={StressLevel} onChange={(e) => handleInputChange(e, setStressLevel)} />
        </div>
        <button type="submit" className="button">Submit</button>
      </form>
      {output && <div style={{ marginTop: '20px' }}>{output}</div>}
    </div>
  );
}

export default App;
