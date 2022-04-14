import React , { useState } from "react";

import NavBar from "./NavBar";
import Input from "./Input";
import Output from './Output';

import '../css/CodeArea.css';

import {InputProvider} from './Context';


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