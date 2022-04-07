
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
                <img src='https://tigres.com.tr/wp-content/uploads/2016/11/orionthemes-placeholder-image-1.png' alt="logo" />
            </div>
            <div className="nav-links">
                <Link to="/" className="link">Home</Link>
                <Link to="/docs" className="link">Docs</Link>
                <a href='https://github.com/waasiq/yakamoz' target='_blank' className="link">Code</a>
                
            </div>  
        </div>
    )
};

export default NavBar;