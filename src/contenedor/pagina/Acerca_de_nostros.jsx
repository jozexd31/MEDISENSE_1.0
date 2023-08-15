import NavBar from "componentes/navegacion/navegacion/NavBar"

import Layout from "hocs/Layouts/Layout"

import Footer from "componentes/navegacion/navegacion/Footer"

function Acerca_de_nostros() {

    return (

        <Layout>

            <NavBar />

            {/* Espacio dentro de la barra de navegacion, debe estar entre 30-40 ya que sino se amontonan las letras*/}

            <h1 class="fg-blue text"><strong>ACERCA DE NOSOTROS</strong></h1>

            <div className='pt-40'>

                <h2 class="fg-blue text">Nuestra misión</h2>

                <p>En nuestra aplicación Health is life se encuentra nuestra misión: Un proyecto que ayude en la mejora en el area de la salud. Cada día, nos esforzamos por mejorar y obtener datos muchos más exactos y ayudar a dar mejores resultados. Creemos firmemente en que nuestra aplicación va a ser de mucha utilidad y trabajamos incansablemente para que nuestros usuarios cuenten con el mejor servicio.</p>

                <br></br>

                <h3 class="fg-blue text">Nuestro compromiso</h3>

                <p>En Health is life, estamos dedicados a la atencion del usuario. Creemos que la dedicación de nuestro equipo es esencial para dar la mejor atención a nuestros usuarios y dar un servicio de calidad.</p>

                <br></br>

                <h4 class="fg-blue text">Nuestro impacto</h4>

                <p>No solo estamos comprometidos con el éxito comercial, sino también con la satisfacción del cliente. A través de nuestra aplicación , buscamos ayudar de mejor manera a que nuestros clientes puedan detectar una posible enfermedad dando los sintomas previos.</p>

                <br></br>

                <h5 class="fg-blue text">Contactos</h5>

                <p>Estamos emocionados de compartir nuestra historia contigo. Si tienes preguntas, comentarios o simplemente quieres conectarte, no dudes en llamar al número: 0976325610 o al correo: juan@uce.edu.ec.</p>

                <br></br>

            </div>

            <Footer />

        </Layout>

    )

}

 

export default Acerca_de_nostros