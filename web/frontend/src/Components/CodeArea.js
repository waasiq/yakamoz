import React , { useState } from "react";

import NavBar from "./NavBar";
import Input from "./Input";
import Output from './Output';

import '../css/CodeArea.css';

import {InputProvider} from './Context';

//TODO: Code the left part of the form first and then the right part later on thats
//TODO: thats all there is on the UI side. Look into the python backend then :) 

const CodeArea = () => {
    return (
        <>
            <NavBar />
            <InputProvider >
                <div className="container">
                    <div className="input">
                        <Input />
                    </div>
                    <div className="output">
                        <Output />
                    </div>
                </div>
            </InputProvider>
        </>
    );
};  

export default CodeArea