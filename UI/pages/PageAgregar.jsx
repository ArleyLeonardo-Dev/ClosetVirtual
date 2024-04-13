import { useState } from "react";
import {useNavigate} from "react-router-dom";
import './styles/PageAgregar.css'



export default function Agregar(){

    const [nombre, setNombre] = useState('');
    const [color, setColor] = useState('');
    const redirect = useNavigate();
    const Combinaciones = () => redirect("/Combinaciones");

    function GuardarDB(nombre, color, tipo){

        const dato = JSON.stringify({"nombre":nombre, "color":color})
        const url = "http://192.168.1.30:5000/" + tipo + "/"

        fetch(url,{
            method:'POST',
            body: dato,
            headers:{
                "Content-Type": "application/json",
            }
        }).then(response => response.json()).then(response => {setNombre(''),setColor('')});
    };

    return(
        <div className="contenedor">
            <h1 className="titulo">AGREGAR ROPA</h1>
            <form onSubmit={e => {
                e.preventDefault();
                GuardarDB(e.target.Nombre.value, e.target.Color.value, e.target.Tipo.value)
            }} className="Formulario">
                <label htmlFor="Nombre">Nombre:</label>
                <input type="text" id="Nombre" value={nombre} onChange={e => setNombre(e.target.value)}/>
                <label htmlFor="Color">Color:</label>
                <input type="text" id="Color" value={color} onChange={e => setColor(e.target.value)} />
                <label htmlFor="Tipo">Tipo De Ropa:</label>
                <select name="" id="Tipo">
                    <option value="Camisas">Camisa</option>
                    <option value="pantalonesFaldas">Pantalon</option>
                    <option value="Zapatos">Zapato</option>
                    <option value="Vestidos">Vestido</option>
                </select>
                <button type="onSubmmit">Enviar</button>
            </form>

            <button onClick={Combinaciones} className="Ver">Ver Combinaciones</button>
        </div>
    )
}