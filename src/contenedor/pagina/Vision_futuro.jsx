import NavBar from "componentes/navegacion/navegacion/NavBar"

import Layout from "hocs/Layouts/Layout"

import Footer from "componentes/navegacion/navegacion/Footer"

 

function Vision_futuro() {

    return (

        <Layout>

            <NavBar />

            {/* Espacio dentro de la barra de navegacion, debe estar entre 30-40 ya que sino se amontonan las letras*/}

            <div className='pt-40'>

                <h1 class="fg-blue text"><strong>VISIÓN A FUTURO</strong></h1>

                <h2 class="fg-blue text">Alcance</h2>

                <p>Desarrollar un software que utilice datos epidemiológicos, patrones de propagación de enfermedades y otros factores relevantes para predecir y alertar sobre posibles enfermedades futuras</p>

                <br></br>

                <h3 class="fg-blue text">Dentro del alcance</h3>

                <p>Recopilar y almacenar datos epidemiológicos históricos de e nfermedades, incluyendo casos confirmados, ubicaciones geográficas y factores de riesgo asociados.</p>

                <br></br>

                <p>Analizar patrones y tendencias de propagación de enfermedades utilizando algoritmos de análisis de datos y aprendizaje automático.</p>

                <br></br>

                <p>Generar modelos predictiv os basados en los datos recopilados y los algoritmos de análisis</p>

                <br></br>

            </div>

            <Footer />

        </Layout>

    )

}

 

export default Vision_futuro