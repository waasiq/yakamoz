<img src = 'https://socialify.git.ci/waasiq/yakamoz/image?font=Raleway&forks=1&logo=https%3A%2F%2Fi0.wp.com%2Fstorage.googleapis.com%2Fstateless-tasmaniangeographic%2F2015%2F05%2FSea-Sparkle-3-By-Leena-Wisby.jpg%3Ffit%3D1024%252C631%26ssl%3D1&name=1&owner=1&pattern=Solid&stargazers=1&theme=Dark' 
style = 'width:100%; height:400px;'>

<br />
<br />

# Yakamoz

<!-- TABLE OF CONTENTS -->
## Table of Contents
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
      <ul>
        <li><a href="#motivation">Motivation</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#links">Links</a></li>
    <li>
      <a href="#documentation">Documentation</a>
      <ul>
        <li><a href="#data-types">Data Types</a></li>
        <li><a href="#variables">Variables</a></li>
        <li><a href="#arithmetic-operators">Arithmetic Operators</a></li>
        <li><a href="#comparison-operators">Comparison Operators</a></li>
        <li><a href="#logical-operators">Logical Operators</a></li>
        <li><a href="#conditional-statements">Conditional Statements</a></li>
        <li><a href="#for-loop">For Loop</a></li>
        <li><a href="#while-loop">While Loop</a></li>
        <li><a href="#functions">Built-In Functions</a></li>
        <li><a href="#functions">Functions</a></li>
      </ul>
    </li>
    <li>
      <a href="#examples">Code Examples</a>
    </li>
    <li><a href="#future-plans">Future Plans</a></li>
  </ol>


<!-- ABOUT THE PROJECT -->
<section id = 'about-the-project'>
<h2> About The Project </h2>

<p> Yakamoz is an small scale interpreted language that was mainly built in older to help Turkish speakers learn programming on a relative easier scale. </p>

</section>

<section id = 'motivation'>

<h3> Motivation </h3>

<p> The motivation behind building yakamoz was to teach my roomate programming and also learn how interpreted languages work behind the scene. It may also be used to teach children about programming in Turkish schools. Yakamoz is in it's early stage so there are still a lot of things to implement and a lot of errors to correct. Due to my full time studies I can't dedicate a lot of time to it's development, please feel free to contact me or fork this project for help. </p>
</section>


<section id = 'built-with'>
<h3> Built With </h3>
<p>Source code for Yakamoz is solely built with Python: </p>
<li><a href='https://www.python.org/'>Python</a></li>

<p>Online compiler is built with: </p>
<li><a href='https://flask.palletsprojects.com/en/2.0.x/'>Flask</a></li>
<li><a href='https://reactjs.org/'>React JS</a></li>

</section>

<!-- GETTING STARTED -->
<section id = 'getting-started'>

## Getting Started
<section id = 'prerequisites'>
<h3> Prerequisites </h3>
<li><a href='https://www.python.org/'>Python</a></li>
<li><a href='https://flask.palletsprojects.com/en/2.0.x/'>Flask</a></li>
<li><a href='https://reactjs.org/'>React JS</a></li>
</section>

<section id = 'installation'>

### Installation

For running offline version of compiler: 

1. Clone the repo
   ```sh
   git clone https://github.com/waasiq/yakamoz.git
   ```
2. Run the shell.py file inside the ./src folder.
    ```
    python ./src/shell.py
    ```
3. Use  the run command inside to read from a file or write the code.
   ```
    yakamoz >>> run('app.ykmz')
   ```
</section>


<section id = 'license'>
<!-- LICENSE -->
<h2>License</h2>

[![MIT License][license-logo]][license-url]<br>
Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->
<section id = 'links'>

## Links
* Project repo: [https://github.com/waasiq/yakamoz.git](https://github.com/waasiq/yakamoz.git)
</section> 

<section id = 'documentation'>

## Documentation

 <section id = 'data-types'>

  #### Data types

  - Data types in Yakamoz for now are:
    * Number (int, float)
    * String
    * List
  
  <section id = 'variables'>

  #### Variables

    Variable syntax:
        oyleki variable_name  = expression
    
    Example: 
        oyleki x = 99 
  </section>

  <section id = 'arithmetic-operators'>

  #### Arithmetic Operators 
  Following operations have been added in yakamoz: 

    Syntax :
      Addition          : (Number + Number) or (String + String) or (List + Number -> appends to list)
      Subtraction       : (Number - Number)
      Mutliplication    : (Number * Number) or (List * List) or (String * Number) 
      Division          : (Number / Number) or (List / Number -> Gives index of list)
      Mod               : (Number % Number)
      Power of          : (Number ^ Number)
  
  </section>
    
  <section id = 'comparison-operators'>

  #### Comparison Operators 
  Following comparison operators have been added in yakamoz:
    Syntax :
    
    (==) : (dataype == datatype)
    (!=) : (datatype != datatype)
    
    (<) : (Number < Number) 
    (>) : (Number > Number) 
    (<=) : (Number <= Number)
    (>=) : (Number >= Number)

  </section>

  <section id = 'logical-operators'>
   
  #### Logical Operators
  not, and, or operetors are available .
    
    Syntax :
    
    yoket          : (! expression)
    and (ve)       : expression ve expression
    or  (veya)     : expression veya expression
    
  </section>

  <section id = 'if-statements'>

  #### if-elseif- else statements
     Syntax :  if condition then expression elseif condition then expression else expression
  </section>

  <section id = 'for-loop'>

  #### For Loop 
  for loop syntax:    
    Syntax :

    for count_variable = start_value to end_value then expression 
    for count_variable = start_value to end_value step step_value then expression 
  </section>

  <section id = 'while-loop'>

  #### While Loop
   
    Syntax : while condition then expression ;
  </section>

  <section id = 'built-in-functions'>

  #### Built-in Functions 
  Following are the built-In functions which have been added to yakamoz:

    Syntax:

    yazdir(expression) 
    ekle(list, number)   -> Adds a number to a list
    isDatatype(datatype) -> returns true if a datatype is a datatype 
    input(string)        -> takes string input from user 
    input_int(int)       -> takes int input from user
 </section>

 <section id = 'functions'>

 #### Functions
 Functions are defined using func keyword followed by the name. Syntax is as follows:
 ```
  func function_name(parameter_list)
    expressions
    return expression
  end 
 ```

 </section>



<section id = 'future-plans'>

## Future Plans
  * Making an online compiler for the language
  * Add code documentation

</section>


[license-logo]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/waasiq/yakamoz/blob/main/LICENSE