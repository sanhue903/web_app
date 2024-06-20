import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid } from 'recharts';

const StudentsGraphic = () => {
    const token = localStorage.getItem('token');
    const [chapter, setChapter] = useState(1);
    const [data, setData] = useState([]);


    const fetchScores = async (chapter) => {
        try {
            const response = await fetch(`/apps/BOTIQI/students/scores?chapter=${chapter}`, {
                method: 'GET',
                headers: {
                    'Authorization': 'Bearer ' + token,
                }
            });
            const result = await response.json();
            return result.scores;
        } catch (error) {
            console.error('Error fetching scores:', error);
            return [];
        }
    };


    const calculateCorrectPercentage = (scores) => {
        const questionCorrectCounts = {};
        const questionTotalCounts = {};

        scores.forEach(score => {
            const question = score.question;
            const questionNumber = question.slice(-1);
            const questionLabel = `Pregunta ${questionNumber}`;

            if (!questionTotalCounts[questionLabel]) {
                questionTotalCounts[questionLabel] = 0;
                questionCorrectCounts[questionLabel] = 0;
            }
            questionTotalCounts[questionLabel]++;
            if (score.is_correct) {
                questionCorrectCounts[questionLabel]++;
            }
        });

        const data = Object.keys(questionTotalCounts).map(questionLabel => ({
            question: questionLabel,
            correct: Math.round((questionCorrectCounts[questionLabel] / questionTotalCounts[questionLabel]) * 100)
        }));

        return data;
    };


    useEffect(() => {
        const fetchData = async () => {
            const scores = await fetchScores(chapter);
            const data = calculateCorrectPercentage(scores);
            setData(data);
        };

        fetchData();
    }, [chapter]);


    const handleChapterChange = (event) => {
        setChapter(Number(event.target.value));
    };


    const CustomTooltip = ({ active, payload }) => {
        if (active && payload && payload.length) {
            return (
                <div className="custom-tooltip">
                    <p>{`Porcentaje de aciertos: ${payload[0].value}%`}</p>
                </div>
            );
        }

        return null;
    };

    return (
        <div>
            <div className='graphic'>
                <BarChart width={800} height={300} data={data}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="question" />
                    <YAxis />
                    <Tooltip content={<CustomTooltip />} />
                    <Bar dataKey='correct' fill='#8884d8' />
                </BarChart>
            </div>
            <div className="chaptersBar">
                {Array.from({ length: 4 }, (_, index) => (
                    <button
                        key={index + 1}
                        className={`chapter ${chapter === index + 1 ? 'active' : ''}`}
                        onClick={() => handleChapterChange({ target: { value: index + 1 } })}
                    >
                        Capítulo {index + 1}
                    </button>
                ))}
            </div>
        </div>
    );
}

export default StudentsGraphic;