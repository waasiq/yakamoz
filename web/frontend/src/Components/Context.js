import React, { createContext , useState } from "react";

export const InputContext = createContext();

export const  InputProvider = (props) => {
    const [code, setCode] = useState('')  
    const [result, setResult] = useState('')

    return (
       <InputContext.Provider value = {[code , setCode, result, setResult]}>
           {props.children}
       </InputContext.Provider>
    )
}