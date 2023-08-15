import React, { useState } from "react"
import NavBar from "componentes/navegacion/navegacion/NavBar"
import Layout from "hocs/Layouts/Layout"
import Footer from "componentes/navegacion/navegacion/Footer"
//import 'bootstrap/dist/css/bootstrap.min.css'
//import { Dropdown, DropdownItem, DrpdownMenu, DropdownToggle } from 'reactstrap';

function Predicciones() {
    return (
        <Layout>
            <NavBar />
            {/* Espacio dentro de la barra de navegacion, debe estar entre 30-40 ya que sino se amontonan las letras*/}

            <div className='pt-60'>
                <select>
                    <option>PICAZON</option>
                    <option>ERUPCIONES CUTANEAS</option>
                    <option>ERUPCIONES NODALES EN LA PIEL</option>
                    <option>ESTORNUDOS CONTINUOS</option>
                    <option>TEMBLORES</option>
                    <option>ESCALOFRIOS</option>
                    <option>DOLOR ARTICULAR</option>
                    <option>DOLOR DE ESTOMAGO</option>
                    <option>ACIDEZ</option>
                    <option>ULCERAS EN LA LENGUA</option>
                    <option>DESGASTE MUSCULAR</option>
                    <option>VOMITOS</option>
                    <option>ARDOR MICCION</option>
                    <option>MANCHAS AL ORINAR</option>
                    <option>FATIGA</option>
                    <option>AUMETO DE PESO</option>
                    <option>ANSIEDAD</option>
                    <option>MANOS Y PIES FRIOS</option>
                    <option>CAMBIOS DE ANIMO</option>
                    <option>PERDIDA DE PESO</option>
                    <option>INQUIETUD</option>
                    <option>LETARGO</option>
                    <option>PARCHES EN LA GARGANTA</option>
                    <option>NIVEL DE AZUCAR IRREGULAR</option>
                    <option>TOS</option>
                    <option>FIEBRA ALTA</option>
                    <option>OJOS HUNDIDOS</option>
                    <option>FALTA DE ALIENTO</option>
                    <option>SUDORACION</option>
                    <option>DESHIDRATACION</option>
                    <option>INDIGESTION</option>
                    <option>DOLOR DE CABEZA </option>
                    <option>PIEL AMARILLENTA</option>
                    <option>ORINA OSCURA</option>
                    <option>NAUSEAS</option>
                    <option>PERDIDA DE APETITO</option>
                    <option>DOLOR DETRAS DE LOS OJOS</option>
                    <option>DOLOR DE ESPALDA</option>
                    <option>ESTRENIMIENTO</option>
                    <option>DOLOR ABDOMINAL</option>
                    <option>DIARREA</option>
                    <option>FIEBRE LEVE</option>
                    <option>ORINA AMARILLA</option>
                    <option>COLORACION AMARILLENATA DE LOS OJOS</option>
                    <option>INSUFICIENCIA HEPATICA AGUDA</option>
                    <option>SOBRECARGA DE LIQUIDOS</option>
                    <option>HINCHAZON DEL ESTOMAGO</option>
                    <option>GANGLIOS LINFATICOS HINCHADOS</option>
                    <option>MALESTAR GENERAL</option>
                    <option>VISION BORROSA Y DISTORSIONADA</option>
                    <option>FLEMA</option>
                    <option>IRRITACION DE LA GARGANTA</option>
                    <option>ENROJECIMIENTO DE OJOS</option>
                    <option>PRESION SINUSAL</option>
                    <option>SECRECION NASAL</option>
                    <option>CONGESTION</option>
                    <option>DOLOR DE PECHO</option>
                    <option>DEBILIDAD EN EXTREMIDADES</option>
                    <option>RITMO CARDIACO RAPIDO</option>
                    <option>DOLOR DURANTE LAS DEFECACIONES</option>
                    <option>DOLOR EN LA REGION ANAL</option>
                    <option>HECES CON SANGRE</option>
                    <option>IRRITACION DEL ANO</option>
                    <option>DOLOR DE CUELLO</option>
                    <option>MAREOS</option>
                    <option>CALAMBRES</option>
                    <option>HEMATOMAS</option>
                    <option>OBESIDAD</option>
                    <option>PIERNAS HINCHADAS</option>
                    <option>VASOS SANGUINEOS HINCHADOS</option>
                    <option>CARA Y OJOS HINCHADOS</option>
                    <option>TIROIDES AGRANDADA</option>
                    <option>UNAS QUEBRADIZAS</option>
                    <option>EXTREMIDADES HINCHADAS</option>
                    <option>HAMBRE EXCESIVA</option>
                    <option>CONTACTOS EXTRAMATRICIALES</option>
                    <option>SEQUEDAD Y HORMIGUEO EN LOS LABIOS</option>
                    <option>DIFICULTAD PARA HABLAR</option>
                    <option>DOLOR EN LAS RODILLAS</option>
                    <option>DOLOR EN LAS ARTICULACIONES DE LA CADERA</option>
                    <option>DEBILIDAD MUSCULAR</option>
                    <option>RIGIDEZ DE CUELLO</option>
                    <option>HINCHAZON DE ARTICULACIONES</option>
                    <option>RIGIDEZ DE MOVIMIENTO</option>
                    <option>MOVIMIENTOS GIRATORIOS</option>
                    <option>PERDIDA DE EQUILIBRIO</option>
                    <option>INESTABILIDAD</option>
                    <option>DEBILIDAD DE UN LADO DEL CUERPO</option>
                    <option>PERDIDA DE OLFATO</option>
                    <option>MALESTAR DE LA VEJIGA</option>
                    <option>MAL OLOR DE LA ORINA</option>
                    <option>MICCION FRECUENTE</option>
                    <option>PASO DE GASES</option>
                    <option>PICAZON INTERNA</option>
                    <option>ASPECTO TOXICO (TIFUS)</option>
                    <option>DEPRESION</option>
                    <option>IRRITABILIDAD</option>
                    <option>DOLOR MUSCULAR</option>
                    <option>SENSORIO ALTERADO</option>
                    <option>MANCHAS ROJAS EN EL CUERPO</option>
                    <option>DOLOR DE VIENTRE</option>
                    <option>MENSTRUACION ANORMAL</option>
                    <option>PARCHES DISCROMICOS</option>
                    <option>LAGRIMEO DE LOS OJOS</option>
                    <option>AUMENTO DEL APETITO</option>
                    <option>POLIURIA</option>
                    <option>ANTECEDENTES FAMILIARES</option>
                    <option>ESPUTO MUCOIDE</option>
                    <option>ESPUTO OXIDADO</option>
                    <option>FALTA DE CONCENTRACION</option>
                    <option>ALTERACIONES VISUALES</option>
                    <option>RECIBIR TRANSFUSION DE SANGRE</option>
                    <option>RECIBIR INYECCIONES NO ESTERILES</option>
                    <option>COMA</option>
                    <option>SANGRADO ESTOMAGO</option>
                    <option>DISTENSION DEL ABDOMEN</option>
                    <option>ANTECEDENTES DE CONSUMO DE ALCOHOL</option>
                    <option>SOBRECARGA DE FLUIDOS</option>
                    <option>SANGRE EN EL ESPUTO</option>
                    <option>VENAS PROMINENTES EN LA PANTORRILLA</option>
                    <option>PALPITACIONES</option>
                    <option>DOLOR AL CAMINAR</option>
                    <option>ESPINILLAS LLENAS DE PUS</option>
                    <option>PUNTOS NEGROS</option>
                    <option>ESCURRIMIENTO</option>
                    <option>DESCAMACION DE LA PIEL</option>
                    <option>POLVO SIMILAR A LA PLATA</option>
                    <option>PEQUENAS ABOLLADURAS EN LA PIEL</option>
                    <option>UNAS INFLAMADAS</option>
                    <option>AMPOLLAS</option>
                    <option>LLAGA ROJA ALREDEDOR DE LA NARIZ</option>
                    <option>EXUDADO COSTRA AMARILLA</option>
                </select>
            </div>
            <Footer />
        </Layout>
    )
}

export default Predicciones