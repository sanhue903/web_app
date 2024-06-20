import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import '../css/Students.css';

function EachStudent() {
  const token = localStorage.getItem('token');
  const { studentId } = useParams();
  const [scores, setScores] = useState([]);

  useEffect(() => {
    const fetchStudentScores = async () => {
      try {
        const response = await fetch(`/apps/BOTIQI/students/${studentId}/scores`, {
          method: 'GET',
          headers: {
            'Authorization': 'Bearer ' + token,
          }
        });
        const data = await response.json();

        data.scores.forEach(score => {
          const questionNumber = score.question.slice(-1);
            score.question = `Pregunta ${questionNumber}`;
        });
        setScores(data.scores);
      } catch (error) {
        console.error('Error fetching student scores:', error);
        setScores([]);
      }
    };

    fetchStudentScores();
  }, [studentId, token]);

  return (
    <div>
      <h2>Scores del Estudiante {studentId}</h2>
      <div className="table">
        <table>
          <thead>
            <tr>
              <th>Sesión</th>
              <th>Capítulo</th>
              <th>Pregunta</th>
              <th>Respuesta</th>
              <th>Segundos</th>
              <th>Intentos</th>
              <th>Correcto</th>
            </tr>
          </thead>
          <tbody>
            {scores.map((score, index) => (
              <tr key={index}>
                <td>{score.session}</td>
                <td>{score.chapter}</td>
                <td>{score.question}</td>
                <td>{score.answer}</td>
                <td>{score.seconds}</td>
                <td>{score.attempt}</td>
                <td>{score.is_correct ? 'Sí' : 'No'}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default EachStudent
