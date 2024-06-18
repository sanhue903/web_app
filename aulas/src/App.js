import StudentsInfo from './components/StudentsInfo';
import './App.css';

function App() {


  fetch('/test')
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error(error);
    });
  return (
    <div>
      <h1 className="titulo">Bienvenid@ al botiquín de las emociones</h1>
      <div className="login-form">
        <h2>Inicio de sesión</h2>
        <input type="text" placeholder="Email" />
        <input type="password" placeholder="Contraseña" />
        <button>Ingresar</button>
      </div>

      <StudentsInfo />
    </div>
  );
}

export default App;
