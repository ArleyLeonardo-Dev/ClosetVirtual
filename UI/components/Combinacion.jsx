import { useEffect, useState } from "react";
import "./styles/Combinacion.css"

export default function GetCombinaciones(){

    const [Datos, setDatos] = useState([])

    useEffect(() => {
        fetch("http://192.168.1.30:5000/Combinaciones/")
        .then(response => response.json())
        .then(datos => setDatos(datos))
    },[])

    window.localStorage.setItem("Datos", JSON.stringify(Datos))

    if(Datos.Vestidos){
        
        return(
            <div className="Combinacion">
                <h1>Vestidos:</h1>
                <p>{Datos.Vestidos}</p>
                <h1>Zapatos:</h1>
                <p>{Datos.Zapatos}</p>
            </div>
        )
    }else{

        return(
            <div className="Combinacion">
                <h1>Camisa:</h1>
                <p>{Datos.Camisas}</p>
                <h1>Pantalon:</h1>
                <p>{Datos.PantalonesFaldas}</p>
                <h1>Zapatos:</h1>
                <p>{Datos.Zapatos}</p>
            </div>
        )
    }
 
}