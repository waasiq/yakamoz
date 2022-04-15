import CodeArea from './Components/CodeArea';
import Docs from "./Components/Doc";
import Examples from './Components/Examples';
import DocsTR from './Components/DocsTR';

import {
  BrowserRouter as Router,
  Routes,
  Route,
} from "react-router-dom";

function App() {    
  return (
    <>
        <Router>
              <Routes>   
                <Route path='/' element={<CodeArea/>} />               
                <Route path='/docs' element={<Docs/>} />        
                <Route path='/examples' element={<Examples/>} />
                <Route path='/docstr' element={<DocsTR/>} />                
              </Routes>
        </Router>
    </>
  );
}

export default App;
