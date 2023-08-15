import { connect } from 'react-redux'
import { NavLink } from 'react-router-dom'
import logo from 'assets/img/logo.png'
import loadyes from 'assets/img/loadyes.gif'

function NavBar() {
    return (
        //CABECERA, TAMANIO Y POSICION
        //CENTRADO, POSICION IZQUIERDA, DERECHA EJE X Y EJE Y 
        //ANCHO DE BARRA PY-2 SE CAMBIA
        <nav className='w-full py-1 shadow-md fixed'>
            <div className=" bg-white px-4 py-5 sm:px-6">
            <div className="-ml-4 -mt-2 flex flex-wrap items-center justify-between sm:flex-nowrap">
                {/* TEXTO IZQUIERDA  */}
                <div className="ml-10 mt-2">
                {/* INSERTAMOS LOGO EN CABECERA, CAMBIAMOS TAMANIO */}
                <img
                src={logo} 
                width={70}
                height={60}
                className=""/>
                </div>
                <div className="ml-4 mt-2 flex-shrink-0">
                {/* MENU DE LA CABECERA  */}
                    <NavLink to ="/Predicciones" className="text-lg inline-flex font-medium leading-6 text-gray-900 hover:underline hover:underline-offset-2 mx-4">PREDICCIONES</NavLink>
                    <NavLink to ="/Blog" className="text-lg inline-flex font-medium leading-6 text-gray-900 hover:underline hover:underline-offset-2 mx-4">BLOG</NavLink>
                    <NavLink to ="/Historial" className="text-lg inline-flex font-medium leading-6 text-gray-900 hover:underline hover:underline-offset-2 mx-4">HISTORIAL</NavLink>
                    <NavLink to ="/Porsi" className="text-lg inline-flex font-medium leading-6 text-gray-900 hover:underline hover:underline-offset-2 mx-4">POR SI ACASO</NavLink>
                        {/*BOTON DE LA DERECHA DE LA CABECERA PARA INGRESO AL SISTEMA */}
                        <button
                            type="button"
                            //TODAS LAS CONFIGURACIONES DEL BOTON
                            className="relative inline-flex items-center rounded-md border border-transparent bg-blue-400 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                        >
                            INGRESAR
                            <img
                            src={loadyes} 
                            className='w-9 h-6 mt-1 ml-2'
                            />
                        </button>
                    </div>
                </div>
            </div>
        </nav>

    )
}

const mapStateToProps = state => ({

})

export default connect(mapStateToProps, {

})(NavBar)