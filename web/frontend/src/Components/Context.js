import React, { createContext , useState } from "react";

export const InputContext = createContext();

export const  InputProvider = (props) => {
    const [code, setCode] = useState("yazdir('Hello World')")  

    return (
       <InputContext.Provider value = {[code , setCode]}>
           {props.children}
       </InputContext.Provider>
    )
}