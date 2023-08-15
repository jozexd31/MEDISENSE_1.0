import NavBar from "componentes/navegacion/navegacion/NavBar"
import Layout from "hocs/Layouts/Layout"
import Footer from "componentes/navegacion/navegacion/Footer"
import Casa from "componentes/navegacion/navegacion/princip/Casa"

function Home() {
    return (
        <Layout>
            <NavBar/>
            {/* Espacio dentro de la barra de navegacion, debe estar entre 30-40 ya que sino se amontonan las letras*/}
            <div className='pt-32'> 
                <Casa/>
            </div>
            <Footer/>
        </Layout>
    )
}

export default Home