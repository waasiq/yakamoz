
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link,
} from "react-router-dom";

import '../css/NavBar.css';

const NavBar = () => {
    return (
        <div className="navbar">
            <div className="logo">
                <img src='https://i0.wp.com/storage.googleapis.com/stateless-tasmaniangeographic/2015/05/Sea-Sparkle-3-By-Leena-Wisby.jpg?fit=1024%2C631&ssl=1' 
                alt="logo" />                
            </div>
            <div className="name">
                <h2>Yakamoz</h2>
            </div>
            <div className="nav-links">
                <Link to="/" className="link">Home</Link>
                <Link to="/docs" className="link">Docs</Link>
                <Link to="/examples" className="link">Examples</Link>
                <Link to="/docstr" className="link">Doküman </Link>
                <a href='https://github.com/waasiq/yakamoz' target='_blank' className="link">Code</a>                
            </div>  
        </div>
    )
};

export default NavBar;