import { useEffect, useState } from "react";
import './styles/Apis.css'

export default function GetApi(url){

    const [Datos, setDatos] = useState([])

    useEffect(() => {
        fetch(url.url)
        .then(response => response.json())
        .then(datos => setDatos(datos))
    },[])

    const datos = Datos.map(dat => <p key={dat.id}> {dat.nombre} {dat.color}</p>)

    return(
        <div className="datos">
            {datos}
        </div>
    )
}