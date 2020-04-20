#Ramazan AYDIN
#180401040
#GİTHUB LİNKİ: https://github.com/52ramazanaydin/programlama-lab./blob/master/odev3_hafta2_sympy_vs_klasik_pdf_grafigi.py
from sympy import Symbol, Piecewise ,pprint
import sympy as sym
import sympy.plotting as syp
import matplotlib.pyplot as plt
import math
%matplotlib inline
num = 180401040
mod = sym.Mod(num, 4) #sympy kütüphanesinde mod almak için kullanılır
#print(mod)
#Uniform Distrubution olduğu anlamına gelir.

      
#Uniform Distribution  (Tekdüze Dağılım) = Olasılık uzayındaki olayların herbirinin gerçekleşme 
#olasılıklarının eşit olduğu, yani tüm olasılıkların tekdüze dağılım gösterdiği bir olasılık dağılımı türüdür.
#Bu dağılım için olasılık yoğunluk fonksiyonu(probability density function) şu şekilde ifade edilir:
#            |1 / (b - a)   ,  a <= x <= b
#    f(x)=   
#            |     0        ,  x < a veya x > b
#



a = Symbol('a')
b = Symbol('b')
x = Symbol('x')
f = 1 / abs(a-b)

print("formul aşağıdaki gibidir...")
pprint(f)


def uniform_sympy_graph(alt_deger, ust_deger):
    if alt_deger > ust_deger:
        alt_deger, ust_deger = ust_deger, alt_deger #alt deger ile üst degerin degerlerini birbirleriyle degistiriyoruz.
    syp.plot(Piecewise((0, (x < alt_deger) | (x > ust_deger)), (f.subs({a: alt_deger, b: ust_deger}), (x >= alt_deger) & 
        (x <= ust_deger))), (x, -10, 10), title="Uniform Distribution sympy")
    
def uniform_matpltlib_graph(alt_deger, ust_deger):
    if alt_deger > ust_deger:
        alt_deger, ust_deger = ust_deger, alt_deger #alt deger ile üst degerin degerlerini birbirleriyle degistiriyoruz.
    x_value=[]
    y_value=[]
    function = Piecewise((0, (x < alt_deger) | (x > ust_deger)), (f.subs({a:alt_deger, b:ust_deger}), (x >= alt_deger) & (x <= ust_deger)))
    value = float(0)
    while value < 10.0:
        y=function.subs({x:value}).evalf()
        y_value.append(y)
        x_value.append(value)
        plt.title('Uniform Distribution matplotlib')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.plot(x_value,y_value)#plt.plot içinde ise fonksiyondaki x değerlerine karşılık gelen f(x)=y değerlerini buluyor ve bu veriler baz alınarak fonksiyon çizimi yapıyoruz. 
        value += 0.1 #Burada grafiği idealine daha yakın yapmak için x in artış değerlerini olabildiğince azalttık.

print("\n")
uniform_sympy_graph(3,9)
print("\n")
uniform_matpltlib_graph(3, 9)

""" Piecewise methodu ile koşullu fonksiyonumuzu oluşturuyoruz.   syp.plot ile fonksiyonun grafiğini çizdiriyoruz."""
