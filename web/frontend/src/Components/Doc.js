
import NavBar from './NavBar'

import '../css/Docs.css'

const Docs = () => {
    return (
        <>
        <NavBar /> 
        <div className = 'docs'>
            <h1> Documentation </h1>
            
            <section id = 'about-the-project'>
                <h2> About The Project </h2>
                <p> Yakamoz is an small scale interpreted language that was mainly built in older to help Turkish speakers learn programming on a relative easier scale. </p>
            </section>

            <section id = 'motivation'>
                <h3> Motivation </h3>
                <p> 
                    The motivation behind building yakamoz was to teach my roomate programming and also learn how interpreted languages work behind the scene.
                    Yakamoz can also be used to teach children in Turkish schools about basics of programming.
                    Yakamoz is in it's early stage so there are still a lot of things to implement and a lot of errors to correct. 
                </p>
            </section>
           
            <section id = 'installation'>
                    <h3> Installation of project on local machine</h3>
                    <p> 
                        To install the project and run it on your own local development environment you can do the following:
                    </p>

                    <div className="code-area">
                        <ul>
                            <li>  Clone the repo git clone https://github.com/waasiq/yakamoz.git</li>
                            <li>
                                Run the shell.py file inside the ./src folder. python ./src/shell.py
                            </li>
                            <li> Use the run command inside to read from a file.  </li>
                            <li> yakamoz {'>>>'} run(' folder_name.ykmz') </li>
                            <li> Alternatively code can also be run inside the shell. </li>
                        </ul>
                    </div>
                    
                </section>

                <h2>Documentation</h2>

                <section id = 'data-types'>

           
                <h3> Data types </h3>

                Data types in Yakamoz for now are:
                    <ul>
                        <li>Number (int, float)</li>
                        <li>String</li>
                        <li>List</li>
                    </ul>
      
                </section>

                <section id = 'variables'>
                    <h3> Variables </h3>
                    <div className="code-area">
                        <p>                        
                            Variable syntax:
                                oyleki variable_name  = expression
                            <br />
                            Example: <br />
                                oyleki x = 99 <br />
                                oyleki adi = 'Waasiq Masood' <br />
                                oyleki list = [1,2,3,4,5] <br />
                        </p>
                    </div>
                </section>

            <section id = 'arithmetic-operators'>
               <h3>
                    Arithmetic Operators 
               </h3>
               Following operations have been added in yakamoz: 
               <div className="code-area">
                   <ul>
                        <li>Addition          : (Number + Number) or (String + String) or (List + Number {'->'} appends to list) </li>
                        <li>Subtraction       : (Number - Number)</li>
                        <li>Multiplication    : (Number * Number)  or (List * List) or (String * Number) </li>
                        <li>Division          : (Number / Number) or (List / Number - Gives index of list)</li> 
                        <li>Mod               : (Number % Number) </li>
                        <li>Power of          : (Number ^ Number) </li>
                    </ul>                   
                </div>    

            </section>
        
            <section id = 'comparison-operators'>
                <h3> Comparison Operators </h3>
                <div className="code-area">
                    <ul>
                        <li>(==) : (dataype == datatype)</li>
                        <li>(!=) : (datatype != datatype)</li>
                        <li>{'<'} : (Number {'<'} Number) </li>
                        <li>{'>'} : (Number {'>'}Number) </li>
                        <li>{'<='} : (Number {'<='} Number) </li>
                        <li>{'>='} : (Number {'>='} Number)  </li>
                    </ul>                 
                </div>
            </section>

            <section id = 'logical-operators'>
    
                <h3>Logical Operators</h3>
                not, and, or operetors are available in yakamoz.
                <div className="code-area">
                    <ul>
                        <li> yoket          : (! expression)            </li>
                        <li> and (ve)       : expression ve expression  </li>
                        <li> or  (veya)     : expression veya expression</li>
                    </ul>   
                </div>
            </section>

            <section id = 'if-statements'>
                <h3> if - elseif- else statements </h3>
                <p>If statements in yakamoz are as shown below: </p>
                <div className="code-area">
                    <p>
                        <strong>eger </strong>condition <strong>sonra</strong> expression <strong>yoksaeger</strong> condition <strong>ise</strong> expression <strong>yoksa</strong> expression <br />
                        <br />
                        Multi-line if statements are as follows:
                        <br />
                        <br /> <strong>eger </strong>condition <strong>sonra</strong> <br />
                             <span className='expr'>expression </span><br />
                        <strong>yoksaeger </strong> condition <strong>ise</strong> <br />
                            <span className='expr'>expression </span><br />
                        <strong>yoksa</strong> <br />
                            <span className='expr'>expression</span> <br />
                        <strong>son</strong> 
                    </p>
                </div>
                
            </section>

            <section id = 'for-loop'>
                <h3>For Loop </h3>
                <div className="code-area">
                    <p>
                        <strong>for</strong> count_variable = start_value to end_value <strong>kadar</strong> expression <strong>son</strong> <br />
                        <strong>for</strong> count_variable = start_value adim step_value to end_value <strong>kadar</strong> expression <strong>son</strong> <br />
                    </p>
                </div>
            </section>

            <section id = 'while-loop'>
                <h3>While Loop</h3>

                <div className="code-area">
                    <p>
                        Syntax : while condition then expression 
                    </p>
                </div>
            </section>

            <section id = 'built-in-functions'>
                <h3> Built-in Functions </h3>
                             
                    Following are the built-In functions which have been added to yakamoz:

                    <div className="code-area">
                        <ul>
                            <li>yazdir(expression) </li>
                            <li>ekle(list, number)   -  Adds a number to a list</li>
                            <li>isDatatype(datatype) - returns true if a datatype is a datatype </li>
                            <li>input(string)        - takes string input from user </li>
                            <li>input_int(int)       - takes int input from user</li>
                        </ul> 
                    </div>            
                
            </section>

            <section id = 'functions'>
                <h3> Functions</h3>
                            
                    Functions are defined using func keyword followed by the name. Syntax is as follows:
                    <div className="code-area">
                        <p>
                            <strong>fonk</strong> function_name(parameter_list) <br />
                                <span className='expr'> expressions       </span> <br />
                                <span className='expr'> <strong>dondur</strong> expression </span> <br />
                            <strong>son</strong> 
                        </p>
                    </div>
        
            </section>

        </div>
        </>
    )
}

export default Docs