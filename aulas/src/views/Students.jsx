import React from 'react'
import '../css/Students.css'
import StudentsTable from '../components/StudentsTable'
import StudentsGraphic from '../components/StudentsGraphic'

function Students() {
  return (
    <div>
      <h1>Estudiantes</h1>
      <StudentsGraphic />
      <StudentsTable />
    </div>
  )
}

export default Students
