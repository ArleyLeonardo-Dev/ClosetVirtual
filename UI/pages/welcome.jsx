import {useNavigate} from "react-router-dom"
import './styles/welcome.css'

export default function Welcome(){

    const redirect = useNavigate()
    const Combinaciones = () => redirect("/Combinaciones")
    const Registrar = () => redirect("/Registrar")

    return(
        <div className="Bienvenida">
            <h1>Closet Virtual</h1>
            <button onClick={Combinaciones} className="Boton">Ver Combinaciones</button>
            <button onClick={Registrar} className="Boton">Registrar Ropa</button>
        </div>
    )
}