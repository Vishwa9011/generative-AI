import { } from 'react'
import './App.css'
import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import { Orders } from './pages/Orders'
import Dishes from './pages/Dishes'
function App() {

  return (
    <>
      <Navbar />
      <Routes>
        <Route path='/' element={<Dishes />} />
        <Route path='/orders' element={<Orders />} />
      </Routes>
    </>
  )
}

export default App
