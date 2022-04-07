
import React, {useContext } from 'react'
import { InputContext } from './Context'

const Output = () => {
    const [code, setCode] = useContext(InputContext)
    const [result, setResult] = useContext(InputContext)

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
            setResult(resJSON);
            console.log('Output is: ' + resJSON);
        }
        catch (error)
        {
            console.log(error);
        }    
    };

    return (
        <> 
            <h3> This is a header</h3>
            <button type="button" onClick = { handleSubmit } > Submit</button>
        </>
    )
}

export default Output;

