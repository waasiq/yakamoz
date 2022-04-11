import CodeMirror from '@uiw/react-codemirror';
//import { oneDark } from '@codemirror/theme-one-dark';

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
                onChange={ setCode }
            />
           
        </>
    )
}

export default Input;