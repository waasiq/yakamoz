import './css/App.css';

import CodeArea from './Components/CodeArea';
import Docs from "./Components/Doc";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
} from "react-router-dom";

function App() {    
  return (
    <>
        <Router>
              <Routes>   
                <Route path='/' element={<CodeArea/>} />               
                <Route path='/docs' element={<Docs/>} />                
              </Routes>
        </Router>
    </>
  );
}

export default App;
