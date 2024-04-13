import GetCombinaciones from '../components/Combinacion'
import { useNavigate } from 'react-router-dom';
import './styles/PagePrincipal.css'


const reload = () => {window.location.reload()};

function Guardar(){

    const data = localStorage.getItem("Datos");

    console.log(data)
    fetch("http://192.168.1.30:5000/Combinaciones/",{
        method:"POST",
        body:data,
        headers:{
            "Content-Type": "application/json",
          }
    }).then(response => response.json()).then(mensaje => console.log(mensaje))
};

export default function Combinaciones(){   
    
    const redirect = useNavigate();
    const Registrar = () => redirect("/Registrar");
    const Prendas = () => redirect("/Prendas")

    return(
        <div className='Contenedor'>
            <h1>COMBINACION</h1>
            <GetCombinaciones />
            <div className='Botones'>
                <button onClick={reload} className='siguiente'>Siguiente</button>
                <button onClick={Guardar} className='megusta'>Me gusta</button>
                <button onClick={Registrar} className='agregarmirar'>Agreagar Ropa</button>
                <button onClick={Prendas} className='agregarmirar'>Mirar Prendas</button>
            </div>
        </div>
    )
}