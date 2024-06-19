import React, { useState, useEffect } from 'react';

function StudentsInfo() {
    const token = localStorage.getItem('token');
    const [students, setStudents] = useState([]);

    useEffect(() => {
      fetch('/apps/BOTIQI/students', { 
        method: 'GET',
        headers: {
          'Authorization': 'Bearer ' + token,
        }
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setStudents(data.students);
      })
      .catch(error => {
        console.error(error);
      });
    }, [token]);
  
    return (
      <div>
      {students.map((student, index) => (
        <div key={index}>
          <p>Name: {student.name}</p>
          <p>Age: {student.age}</p>
          <p>App ID: {student.app_id}</p>
          <p>Session: {student.session}</p>
          <hr />
        </div>
      ))}
    </div>
    );
  }

export default StudentsInfo;