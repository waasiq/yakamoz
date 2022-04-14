

import NavBar from "./NavBar"
import '../css/Docs.css'

const Examples = ()  => {
    return (
        <>
            <NavBar />
            <div className = 'docs'>
                <h1>Examples</h1>

                <h3>Hello World</h3> 
                <div className="code-area">                    
                    <p>                       
                        yazdir('Hello World')
                    </p>
                </div>

                <h4>Note: Split statement if, for and while loop are still in development for 
                    online compiler. Although they may work but they might not be 100% correct.</h4>
                <h2> Online Compiler Code Examples </h2>
                <p>Some examples which can be run on the online compiler:</p>
              
                <h3>Positif ve ya Negatif Sayi</h3> 
                <div className="code-area">                    
                    <p>                       
                    oyleki b = 20 <br /> <br />

                    eger b {'<'} 0 ise yazdir('Negatif sayi girdiniz') yoksaeger b {'>'} 0 ise 
                    yazdir('Pozitif sayi girdiniz')
                    </p>
                </div>
          
                <h3>10 ile 10 kere çarpma</h3> 
                <div className="code-area">                    
                    <p>                       
                    oyleki sayi = 10 <br /> <br />

                    for i = 0 den 10 kadar <br />
                        <div className='expr'>oyleki sayi = sayi * 10 </div>
                    son <br />

                    yazdir(sayi)
                    </p>
                </div>

                <h2> Offline Code Examples</h2>
                <p>Some multiline examples which can be run on the offline source code. 
                    You may edit the app.ykmz file inside the src to start coding. {':)'} </p>
                <h3>Positif ve ya Negatif Sayi</h3> 
                <div className="code-area">                    
                    <p>                       
                    oyleki b = 20 <br /> <br />

                    eger b {'<'} 0 ise
                    <div className="expr">yazdir('Negatif sayi girdiniz')</div>
                    
                    yoksaeger b {'>'} 0 ise 
                    <div className="expr">yazdir('Pozitif sayi girdiniz')</div>
                    son
                    </p>
                </div>

            
                
                <h3>Liste Ekrana Yazdir</h3> 
                <div className="code-area">                    
                    <p>                       
                        fonk diziYazdir(liste) <br />
                            <div className="expr">for i = 0 den uzunluk(liste) kadar 
                            <div className="expr"> yazdir(liste/i)</div>
                            son</div>
                        son<br /><br />

                        oyleki a = [2,7,11,15]<br />
                        diziYazdir(a)
                    </p>
                </div>

                <h3>Celsius {'<->'} Farenheit</h3> 
                <p> Do notice that the input_int() function has not been implemented in the online version
                    of the language. 
                </p>
                <div className="code-area big-example">                    
                    <p>                       
                        yazdir('Celsius den farenHeit secmek icin 1, farenheit den Celsius secmek icin 2 giriniz:') <br />
                        <br /> oyleki secenek = input_int() <br /> <br />

                        eger secenek == 1 ise <br />
                            <div className="expr">
                                yazdir('Celsius degerini giriniz:')<br />
                                oyleki celsius = input_int()<br />
                                oyleki farenheit = celsius * 1.8 + 32<br />
                                yazdir('Farenheit degeri: ')<br />
                                yazdir(farenheit)<br />
                            </div>
                        yoksaeger secenek == 2 ise <br />
                            <div className="expr">
                                yazdir('Farenheit degerini giriniz:')<br />
                                oyleki farenheit = input_int()<br />
                                oyleki celsius = (farenheit - 32) / 1.8<br />
                                yazdir('Celsius degeri: ')<br />
                                yazdir(celsius)<br />
                            </div>
                        son<br />
                    </p>
                </div>
            </div>
        </>
    )
}

export default Examples 