import NavBar from "componentes/navegacion/navegacion/NavBar"

import Layout from "hocs/Layouts/Layout"

import Footer from "componentes/navegacion/navegacion/Footer"

 

function Colabora() {
return (

        <Layout>

            <NavBar />

            {/* Espacio dentro de la barra de navegacion, debe estar entre 30-40 ya que sino se amontonan las letras*/}

            <div className='pt-40'>

                <h1 class="fg-blue text"><strong>COLABORADORES</strong></h1>

                <p><strong>Jose Pillajo: </strong>Jefe de grupo</p>

                <br></br>

                <p><strong>Silvia Janeta: </strong>Analista de datos</p>

                <br></br>

                <p><strong>Cristian Vasco: </strong>Desarrollador</p>

                <br></br>

                <p><strong>Maria Belen Tasiguano: </strong>Desarrolladora</p>

                <br></br>

                <img />

            </div>

            <Footer />

        </Layout>

    )

}

 

export default Colabora