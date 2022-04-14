import CodeMirror from '@uiw/react-codemirror';
import '../css/CodeArea.css';

import { useContext } from 'react';
import { InputContext } from './Context';

const Input = () =>
{
    const [ code , setCode ] = useContext(InputContext)
           
    return (
        <>
            <CodeMirror
                value="yazdir('Hello World')"
                height="630px"
                width="100%"
                className='input-area'
                onChange={ setCode }
            />
           
        </>
    )
}

export default Input;