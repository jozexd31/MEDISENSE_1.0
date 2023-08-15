import { connect } from "react-redux"

function Layout ({children}){
    return(
        <div>
            {children}
        </div>
    )
}
//podemos llamar a cualquier funcion desde donde sea
const mapStateToProp =state => ({

})

export default connect(mapStateToProp,{

}) (Layout)