import React from 'react'
import ReactDOM from 'react-dom/client'
import Combinaciones from '../pages/PagePrincipal'
import {createBrowserRouter, RouterProvider} from 'react-router-dom'
import Welcome from '../pages/welcome'
import Agregar from '../pages/PageAgregar'
import Prendas from '../pages/Prendas'
import './main.css'

const index = createBrowserRouter([
  {
    path: "Combinaciones",
    element: <Combinaciones/>
  },
  {
    path:"/",
    element:<Welcome/>
  },
  {
    path:"Registrar",
    element:<Agregar/>
  },
  {
    path:"Prendas",
    element:<Prendas/>
  }
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={index} />
  </React.StrictMode>,
)
