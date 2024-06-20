import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Login from './views/Login';
import Students from './views/Students';
import ProtectedRoute from './components/ProtectedRoute';
import EachStudent from './views/EachStudent';
import './App.css';

function App() {
  
  return (
    <div>
      <BrowserRouter>

        <Routes>
          <Route path="/login" element={< Login />} />
          <Route path="/students" element={ <ProtectedRoute> <Students /> </ProtectedRoute> } />
          <Route path="/students/:studentId/scores" element={<ProtectedRoute><EachStudent /></ProtectedRoute>} />
        </Routes>

      </BrowserRouter>

      
    </div>
  );
}

export default App;
