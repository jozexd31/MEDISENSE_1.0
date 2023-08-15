import NavBar from "componentes/navegacion/navegacion/NavBar"

import Layout from "hocs/Layouts/Layout"

import Footer from "componentes/navegacion/navegacion/Footer"

 

function Contactos() {

    return (

        <Layout>

            <NavBar />

            {/* Espacio dentro de la barra de navegacion, debe estar entre 30-40 ya que sino se amontonan las letras*/}

            <div className='pt-40'>

                <h1 class="fg-blue text">Contactos</h1>

                <p>Estamos emocionados de compartir nuestra historia contigo. Si tienes preguntas, comentarios o simplemente quieres conectarte, no dudes en llamar al número: 0976325610 o al correo: juan@uce.edu.ec.</p>

                <br></br>

            </div>

            <Footer />

        </Layout>

    )

}

 

export default Contactos