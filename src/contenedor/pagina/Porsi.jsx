import NavBar from "componentes/navegacion/navegacion/NavBar"
import Layout from "hocs/Layouts/Layout"
import Footer from "componentes/navegacion/navegacion/Footer"

function Porsi() {
    return (
        <Layout>
            <NavBar/>
            {/* Espacio dentro de la barra de navegacion, debe estar entre 30-40 ya que sino se amontonan las letras*/}
            <div className='pt-40'> 
                Porsi
            </div>
            <Footer/>
        </Layout>
    )
}

export default Porsi