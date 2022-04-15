<img src="https://socialify.git.ci/waasiq/yakamoz/image?font=Source%20Code%20Pro&forks=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2Fwaasiq%2Fyakamoz%2Fmain%2Fdocs%2Fyakamoz-logo-modified.png&name=1&owner=1&pattern=Solid&pulls=1&stargazers=1&theme=Dark" alt="yakamoz" width="100%;" height="400px;" />

<br />
<br />

# Yakamoz

<!-- TABLE OF CONTENTS -->
## Table of Contents
  <summary>
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
    <li>
      <a href="#documentation">Documentation</a>
    </li>
    <li><a href="#future-plans">Future Plans</a></li>
  </ol>
  </summary>

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

For running online version of compiler: 

1. Clone the repo
   ```sh
     git clone https://github.com/waasiq/yakamoz.git
   ```
2. Install the python dependencies using pip in web/backend.
    ```
      pip install -r requirements.txt
    ```
3. Install the npm  dependencies using npm in web/frontend.
    ```
      npm install 
    ```
4. Run both the backend and frontend and do change the API link in package.json as well as Output   Component to https://127.0.0.1:5000/api/code


</section>


<section id = 'license'>
<!-- LICENSE -->
<h2>License</h2>

[![MIT License][license-logo]][license-url]<br>
Distributed under the MIT License. See `LICENSE` for more information.

<section id = 'documentation'>

## Documentation

<p>Documentation can be found on the <a href='https://yakamoz.netlify.app/'>website</a>. Click on Docs to access Documentation there.</p>

<section id = 'future-plans'>

## Future Plans
  * Improve the documentation and improve the compiler.

</section>


[license-logo]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/waasiq/yakamoz/blob/main/LICENSE