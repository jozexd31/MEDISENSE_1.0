//es lo que organiza todas las rutas
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Error404 from "contenedor/paginaerror/Error404";
import Home from "contenedor/pagina/Home";
import Predicciones from "contenedor/pagina/Predicciones";
import Blog from "contenedor/pagina/Blog";
import Historial from "contenedor/pagina/Historial";
import Porsi from "contenedor/pagina/Porsi";
import store from "store";
import { Provider } from "react-redux";
import Login from "componentes/Login/Login"
import Acerca_de_nostros from 'contenedor/pagina/Acerca_de_nostros';
import Contactos from 'contenedor/pagina/Contacto';
import Colabora from 'contenedor/pagina/Colabora';
import Vision_futuro from 'contenedor/pagina/Vision_futuro';


function App() {
  return (
    <Provider store={store}>
      <Router>
        <Routes>
            <Route exact path ="/" element={<Login/>}/>
            {/* PAGINA ERROR */}
            <Route path="*" element={<Error404/>} />
            {/* PAGINA HOME*/}
            <Route path="/Home" element={<Home/>} />
            <Route path="/Predicciones" element={<Predicciones />} />
            <Route path="/Blog" element={<Blog />} />
            <Route path="/Historial" element={<Historial />} />
            <Route path="/Porsi" element={<Porsi />} />
            <Route path="/Acerca_de_nostros" element={<Acerca_de_nostros />} />
            <Route path="/Contactos" element={< Contactos />}/>
            <Route path="/Colabora" element={<Colabora/>}/>
            <Route path="/Vision_futuro" element={<Vision_futuro/>}/>
        </Routes>
      </Router>
    </Provider>
  );
}

export default App;
