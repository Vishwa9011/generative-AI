import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import { Orders } from './pages/Orders'
import Dishes from './pages/Dishes'
import './App.css'

import axios from 'axios';
import ChatAssistance from './components/ChatAssitance/ChatAssistance'

axios.defaults.baseURL = 'http://127.0.0.1:8000'

function App() {

  return (
    <>
      <Navbar />
      <Routes>
        <Route path='/' element={<Dishes />} />
        <Route path='/orders' element={<Orders />} />
      </Routes>
      <ChatAssistance />
    </>
  )
}

export default App
