import GetApi from "../components/Apis"

const camisas = "http://192.168.1.30:5000/Camisas/"
const pantalones = "http://192.168.1.30:5000/pantalonesFaldas/"
const vestidos = "http://192.168.1.30:5000/Vestidos/"
const zapatos = "http://192.168.1.30:5000/Zapatos/"

export default function Prendas(){
    return(
        <>
            <h1 className="titulo">Camisas</h1>
            <GetApi url = {camisas}/>
            <h1 className="titulo">Pantalones / Faldas</h1>
            <GetApi url = {pantalones}/>
            <h1 className="titulo">Vestidos</h1>
            <GetApi url = {vestidos}/>
            <h1 className="titulo">Zapatos</h1>
            <GetApi url = {zapatos}/>
        </>
    )
};