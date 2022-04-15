
import NavBar from './NavBar'

import '../css/Docs.css'

const DocsTR = () => {
    return (
        <>
        <NavBar /> 
        <div className = 'docs'>
            <h1> Dokümantasyon </h1>
            
            <section id = 'about-the-project'>
                <h2> Proje Hakkında </h2>
                <p> Yakamoz Türkçe arayüzlü yorumlanmış bir programlama dilidir. </p>
            </section>

            <section id = 'motivation'>
                <h3> Motivasyon </h3>
                <p> 
                Oda arkadaşımla programla öğretmek amacıyla başladığımız bu proje ilk başlarda basitti ama 
                ilerledikçe karmaşık bir hal aldı. Genel hatlarıyla kolay bir programlama dili olduğu için 
                çocuklara kodlama öğretilirken kullanılabilir. Değişkenler, döngüler ve fonksiyonları kapsayan 
                bu dil küçük ölçekli programlar için çalışır. 
                </p>
            </section>
           
            <section id = 'installation'>
                    <h3> Indirmeli Teknolojiler</h3>
                    <p> 
                       Projeyı çalıştırmak için aşağıda verilmiş Teknolojiler gerekmektedir.
                    </p>

                    <div className="code-area">
                        <ul>
                            <li> Repoyu klon et: https://github.com/waasiq/yakamoz.git</li>
                            <li>
                                ./src/ dosyasında shell.py python dosyayı çalıştır.
                            </li>
                            <li> Run komut ile dosyalardan veri okunabilir.  </li>
                            <li> yakamoz {'>>>'} run(' folder_name.ykmz') </li>
                            <li> Diğer türlü CLI'da kod da yazılabiir. </li>
                        </ul>
                    </div>
                    
                </section>

                <h2>Dokümantasyon</h2>

                <section id = 'data-types'>

           
                <h3> Data türler </h3>

                Data types in Yakamoz for now are:
                    <ul>
                        <li>Numarayalar (int, float)</li>
                        <li>String</li>
                        <li>Liste</li>
                    </ul>
      
                </section>

                <section id = 'variables'>
                    <h3> Değişkenler </h3>
                    <div className="code-area">
                        <p>                        
                                Değişkenler syntax:
                                oyleki variable_name  = expression
                            <br />
                            Örnek: <br />
                                oyleki x = 99 <br />
                                oyleki adi = 'Waasiq Masood' <br />
                                oyleki list = [1,2,3,4,5] <br />
                        </p>
                    </div>
                </section>

            <section id = 'arithmetic-operators'>
               <h3>
                    Matematiksal öperatör
               </h3>
               Aşağıda verilmiş: 
               <div className="code-area">
                   <ul>
                        <li>Toplama        : (Number + Number) or (String + String) or (List + Number {'->'} appends to list) </li>
                        <li>Çıkarma        : (Number - Number)</li>
                        <li>Çarpma         : (Number * Number)  or (List * List) or (String * Number) </li>
                        <li>Bölme          : (Number / Number) or (List / Number - Gives index of list)</li> 
                        <li>Mod            : (Number % Number) </li>
                        <li>Küvvet         : (Number ^ Number) </li>
                    </ul>                   
                </div>    

            </section>
        
            <section id = 'comparison-operators'>
                <h3> Eşitleme Öperators </h3>
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
    
                <h3>Lojik Öperatör</h3>
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
                <p>If else statements: </p>
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
                    <strong>while</strong> count_variable expression <strong>ise</strong> expression <strong>son</strong> <br />
                    </p>
                </div>
            </section>

            <section id = 'built-in-functions'>
                <h3> Hazır fonksiyonlar </h3>
                             
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
                <h3> Fonksiyonlar</h3>
                            
                    Fonksiyonlaın syntax aşağıda verilmiş:
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

export default DocsTR