import Head from 'next/head';
import { useState } from 'react';

export default function HomePage() {
  const [firstName, setFirstName] = useState('');
  const [lastName, setLastName] = useState('');
  const [middleInitial, setMiddleInitial] = useState('');
  const [formattedName, setFormattedName] = useState('');
  const [isError, setIsError] = useState(false);

  const handleSubmit = async () => {
    setIsError(false); // Reset error state on new submission
    setFormattedName(''); // Clear previous message

    // Basic validation: ensure first and last names are provided
    if (!firstName.trim() || !lastName.trim()) {
      setFormattedName('First and Last names are required.');
      setIsError(true);
      return;
    }

    const params = new URLSearchParams();
    params.append('first_name', firstName);
    params.append('last_name', lastName);
    if (middleInitial.trim()) {
      params.append('middle_initial', middleInitial.trim());
    }

    try {
      const response = await fetch(`http://localhost:5000/api/format_name?${params.toString()}`);
      if (!response.ok) {
        let errorMessage = `Error: ${response.status} ${response.statusText}`;
        try {
            const errorData = await response.json();
            if (errorData && errorData.error) { // Assuming backend sends { "error": "message" }
                errorMessage = errorData.error;
            }
        } catch (e) {
            // If response is not JSON or another error occurs parsing it, stick with status text
        }
        setIsError(true);
        throw new Error(errorMessage);
      }
      const data = await response.json();
      if (data.formatted_name) {
        setFormattedName(data.formatted_name);
        setIsError(false);
      } else {
        setFormattedName('Received an unexpected response from the server.');
        setIsError(true);
      }
    } catch (error) {
      console.error('Failed to format name:', error);
      setFormattedName(`${error.message}`); // Display error message directly
      setIsError(true);
    }
  };

  return (
    <>
      <Head>
        <title>Name Formatter</title>
        <meta name="description" content="Format names easily" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <main>
        <h1>Name Formatter</h1>
        <div className="form-group">
          <label htmlFor="firstName">First Name:</label>
          <input
            type="text"
            id="firstName"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            placeholder="e.g., John"
          />
        </div>
        <div className="form-group">
          <label htmlFor="middleInitial">Middle Initial (optional):</label>
          <input
            type="text"
            id="middleInitial"
            value={middleInitial}
            onChange={(e) => setMiddleInitial(e.target.value)}
            placeholder="e.g., B"
            maxLength="1"
          />
        </div>
        <div className="form-group">
          <label htmlFor="lastName">Last Name:</label>
          <input
            type="text"
            id="lastName"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            placeholder="e.g., Doe"
          />
        </div>
        <button onClick={handleSubmit}>Format Name</button>

        {formattedName && (
          <div className="result-container">
            <h2>Result:</h2>
            <p style={{ color: isError ? 'red' : 'black' }}>
              {formattedName}
            </p>
          </div>
        )}
      </main>
      <style jsx>{`
        main {
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          padding: 2em;
          max-width: 450px;
          margin: 2em auto;
          background-color: #ffffff;
          border-radius: 8px;
          box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
          text-align: center;
          color: #333;
          margin-bottom: 1.5em;
        }
        .form-group {
          margin-bottom: 1.2em;
        }
        label {
          display: block;
          margin-bottom: 0.4em;
          color: #444;
          font-weight: 600;
        }
        input[type="text"] {
          width: calc(100% - 20px); // Adjust for padding
          padding: 10px;
          border: 1px solid #ccc;
          border-radius: 4px;
          font-size: 1em;
          box-sizing: border-box; /* Ensures padding doesn't add to width */
        }
        input[type="text"]:focus {
          border-color: #0070f3;
          outline: none;
          box-shadow: 0 0 0 2px rgba(0, 112, 243, 0.2);
        }
        button {
          background-color: #0070f3;
          color: white;
          padding: 12px 18px;
          border: none;
          border-radius: 4px;
          font-size: 1.05em;
          cursor: pointer;
          display: block;
          width: 100%;
          margin-top: 1.5em;
          transition: background-color 0.2s ease-in-out;
        }
        button:hover {
          background-color: #005bb5;
        }
        .result-container {
          margin-top: 2em;
          padding: 1em;
          background-color: #f9f9f9;
          border: 1px solid #eee;
          border-radius: 4px;
          text-align: center;
        }
        .result-container h2 {
          font-size: 1.2em;
          color: #333;
          margin-bottom: 0.5em;
        }
        .result-container p {
          font-size: 1.1em;
          white-space: pre-wrap; /* To respect newlines if any in message */
          margin: 0;
        }
      `}</style>
    </>
  );
}
