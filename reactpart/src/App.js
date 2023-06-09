import Index from './components/Index';
import './App.css';
import { Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Signup from './components/Signup';
import AddProduct from './components/AddProduct';
import Profile from './components/Profile';
import Store from './components/Store';
import Cart from './components/Cart';
import Order from './components/Order';

function App() {
  return (
    <div className="App">
      <Index />
      <Routes>
        
        <Route path='/store' element={<Store />}></Route>
        <Route path='/login' element={<Login />}></Route>
        <Route path='/Signup' element={<Signup />}></Route>
        <Route path='/AddProduct' element={<AddProduct />}></Route>
        <Route path='/Profile' element={<Profile />}></Route>
        <Route path='/cart' element={<Cart />}></Route>
        <Route path='/order' element={<Order />}></Route>
      </Routes>

    </div>
  );
}

export default App;
