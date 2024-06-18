import React, { useState, useEffect } from 'react';

function StudentsInfo() {
    const [data, setData] = useState(null);
  
    useEffect(() => {
        fetch('/')
          .then((response) => {
            if (!response.ok) {
              throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
          })
          .then((data) => setData(data.message))
          .catch((error) => {
            console.error('Error:', error);
          });
      }, []);
  
    return (
      <div>
        {data ? <p>{ data }</p> : 'Cargando...'}
      </div>
    );
  }

export default StudentsInfo;