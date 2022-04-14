
import React, {useContext, useState } from 'react'
import { InputContext } from './Context'

import Button from '@mui/material/Button';

const Output = () => {
    const [code, setCode] = useContext(InputContext)
    const [result, setResult] = useState('')
    const [error, setError] = useState('')


    const handleSubmit = async(e) => {
        e.preventDefault();

        try {
            let res = await fetch('http://127.0.0.1:5000/api/code', {
                method: 'POST',
                headers: {
                    'Content-type':'application/json'
                },
                body: JSON.stringify({
                    'code': code
                })
            });

            let resJSON = await res.json();
            let resArrays  = resJSON.split('\n')
            setResult(resArrays);
        }
        catch (error)
        {
            console.log(error);
        }    
    };

    return (
        <>  
            <Button className = 'mui-btn' variant="contained" onClick= { handleSubmit }>Run</Button>
            <br />

            { 
                Object.values(result).map((val, index) => {
                    return <h3 key= {index}>{val}</h3>
               })
            }
            
        </>
    )
}

export default Output;

