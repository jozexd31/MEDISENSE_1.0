import React from "react"
import Home from "contenedor/pagina/Home";
import {Link} from "react-router-dom"

function Login() { 
    return (
        <div className="container" style={{background:"lightgray", marginTop:20, padding:20}}>
        
            <form id="form_login">
                <div>
                    <h1 style={{color:"blue", textalign:"center"}}>LOGIN</h1>
                    <label htmlFor="txtusu"><strong>NOMBRE DE USUARIO</strong></label>
                    <input type="text" id="txtusu" style={{textAlign:"center"}} className="form-control"  required/>
                </div>
                <div>
                    <label htmlFor="txtpas"><strong>CONTRASEÑA</strong></label>
                    <input type="password" id="txtpas" style={{textAlign:"center"}} className="form-control"  required/>
                </div><br/>
                <Link to ="/Home" className="btn btn-primary">INGRESAR</Link>
            </form>

        </div>
    )

}
export default Login