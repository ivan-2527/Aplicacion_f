import streamlit as st
import pandas as pd
import numpy as np

st.image('./mc1.png')

# Texto:
st.title('Juguemos con las conversiones para Termofluidos')
st.header('En esta pagina se contendrá algunos factores de conversión basicos relacionados a las áreas de Mecánica de Fluidos, Termodinámica, y cómo estos pueden ser realizados por medio de comandos de linea de python')

st.subheader('Escala de temperatura')

st.write('Las escalas de temperatura que usualmente se utilizan en la Física son: Celsius, Fahrenheit y Kelvin. Para poder determinar una escala se necesitan dos puntos de referencia, es decir dos lecturas de temperatura que puedan ser medibles, estas pueden estar relacionadas al punto de fusión y ebullición, tomando en base al agua, considerando la presión del fluido a 1atm') 

st.image('./Escalatemp.png')

st.subheader('Escala Celsius')

st.write('Para este tipo de escala se utiliza como parametro a el valor 0°C con respecto al agua destilada, se relaciona al proceso de fusión, y para el caso 100°C se refiere al proceso de ebullición.')

st.write('A continuación se muestran las ecuaciones para realizar el proceso de conversión a escala Celsius cuando concemos la lectura de la temperatura en escala Farenheit y Kelvin respectivamente son las siguientes:')

st.markdown('_CUANDO SE CONOCE LA LECTURA DE LA TEMPERATURA EN ESCALA FAHRENHEIT_') 

st.latex(r''' T_c=\frac{5}{9}(T_f-32)''')

st.markdown('_CUANDO SE CONOCE LA LECTURA DE LA TEMPERATURA EN ESCALA KELVIN_') 

st.latex(r''' T_c=T_k-273.15''')

st.subheader('Escala Fahrenheit')

st.write('Para este tipo de escala se utiliza como parametro a el valor 32°F con respecto al agua destilada, se relaciona al proceso de fusión, y para el caso 212°F se refiere al proceso de ebullición.')

st.write('A continuación se muestran las ecuaciones para realizar el proceso de conversión a escala Fahrenheit cuando concemos la lectura de la temperatura en escala Celsius y Kelvin respectivamente son las siguientes:')

st.markdown('_CUANDO SE CONOCE LA LECTURA DE LA TEMPERATURA EN ESCALA FAHRENHEIT_') 

st.latex(r''' T_f=\frac{9}{5}T_c+32 ''')

st.markdown('_CUANDO SE CONOCE LA LECTURA DE LA TEMPERATURA EN ESCALA KELVIN_') 

st.latex(r''' T_f=\frac{9}{5}(T_k-273.15)+32''')

st.subheader('Escala Kelvin')

st.write('Para este tipo de escala se utiliza como parametro a el valor 273.15K con respecto al agua destilada, se relaciona al proceso de fusión, y para el caso 373.15K se refiere al proceso de ebullición, es la escala que tiene como tal un 0 absoluto.')

st.write('A continuación se muestran las ecuaciones para realizar el proceso de conversión a escala Kelvin cuando concemos la lectura de la temperatura en escala Celsius y Fahrenheit respectivamente son las siguientes:')

st.markdown('_CUANDO SE CONOCE LA LECTURA DE LA TEMPERATURA EN ESCALA CELSIUS_') 

st.latex(r'''  T_k=T_c+273.15''')

st.markdown('_CUANDO SE CONOCE LA LECTURA DE LA TEMPERATURA EN ESCALA FAHRENHEIT_') 

st.latex(r''' T_k=\frac{5}{9}(T_f-32)+273.15''')
#}

st.markdown('A continuación se muestra ejemplos de forma teórica de cómo realizar la conversión entre escalas de temperatura.')

st.subheader('Convertir 45°C a escala Fahrenheit y Kelvin respectivamente')

st.markdown('Primero se debe establecer cuales son las expresiones matemáticas a utilizar para realizar los cálculos de las respectivas, para ello se identifica la que contiene el la variable Tc para Tk y Tf')

st.latex(r''' T_f=\frac{9}{5}T_c+32 ''')

st.latex(r'''  T_k=T_c+273.15''')

st.markdown('Ya que se identifico las ecuaciones a emplear en cada una de la mismas en la expresión Tc se cambiará por el valor que se quiere realizar la conversión es decir 45°C y ser realiza las operaciones aritméticas correspondientes')

st.markdown('_DE ESCALA CELSIUS A FAHRENHEIT_')

st.latex(r''' T_f=\frac{9}{5}(45)+32 ''')
st.latex(r''' T_f=9(9)+32 ''')
st.latex(r''' T_f=81+32 ''')
st.latex(r''' T_f=113°F ''')

st.markdown('_DE ESCALA CELSIUS A KELVIN_')

st.latex(r'''  T_k=(45)+273.15''')
st.latex(r'''  T_k=318.15K''')

st.write('Ahora que ya se conoce cómo es realizar la conversión entre escalas de temperatura utilizando comando de python.')

st.write('Para ello se utilizará la función lambda, y por medio de una función definida. Primero empezaremos a realizar el ejercicio por medio de la función lamba el cuál tendra la siguiente estructura')

st.markdown('_DE ESCALA CELSIUS A FAHRENHEIT_')
st.code('t_f=(lambda t_c:t_c*1.8+32)(45)')
st.code('print(El resultado de convertir 45°C a escala Fahrenheit es:)')

st.write('Con respecto a las lineas de codigo anterior, se colocará la imagen que representa el codigo y el resultado obtenido')

st.image('./cf.png')

st.markdown('_DE ESCALA CELSIUS A KELVIN_')
st.code('t_k=(lambda t_c:t_c+273.15)(45)')
st.code('print(El resultado de convertir 45°C a escala Kelvin es:)')

st.write('Con respecto al ejemplo anterior , se colocará la imagen que representa el codigo y el resultado obtenido')

st.image('./ck.png')

st.write('Se realizará el cálculo por medio de la definición de una función es decir, por medio del comando def')
st.markdown('_DE ESCALA CELSIUS A FAHRENHEIT_')
st.code('t_f=(lambda t_c:t_c*1.8+32)(45)')
st.code('print(el resultado de convertir 45°C a escala Fahrenheit es:)')

st.latex(r''' T_f=\frac{9}{5}T_c+32 ''')
T_c=st.number_input('Indica la tempereatura que desea convertir')
T_f=1.8*T_c+32
st.write(T_f)

'''
st.text('Muestra de texto sencillo')
st.write('Otra muestra de texto sencillo') 
st.text('Así se ve una lista de 3 elementos:')
st.write(['st', 'is <', 3])
st.text(['st', 'is <', 3])

st.text('Así se ve un recuadro de código:')
st.code('for i in range(8): hola!')

datos = {'Nombre': ['Tomás', 'Jose', 'Cristian', 'John'], 'Edad': [20, 21, 19, 18]}  
'''

'''
# Create DataFrame  
mi_tabla = pd.DataFrame(datos)

# Datos:
st.text('Vista de un dataframe:')
st.dataframe(mi_tabla)
st.text('Vista de una tabla:')
st.table(mi_tabla.iloc[0:4])
st.text('Un json:')
st.json({'a':'1','b':'2', 'c':'3'})
st.text('Una métrica:')
st.metric('Mi métrica', 42, 2)

# Columnas:
col1, col2, col3 = st.columns(3)
col1.write("Esta es la columna 1")
col2.write("Esta es la columna 2")
col3.write("Esta es la columna 3")

# Imágenes:
st.write('Una muestra de una imágen:')
st.image('./imagen_1.png')

# Barra lateral:
a = st.sidebar.radio('Selecciona un número:', [1, 2, 3, 4, 5])
b = st.sidebar.radio('Selecciona un día:', ['lunes', 'martes', 'miercoles', 'jueves', 'viernes'])

# Formulario
st.write("Así se ve un formulario:")
with st.form(key='my_form'):
   username = st.text_input('Nombre')
   password = st.text_input('Correo')
   st.form_submit_button('Registrar')



# Widgets interactivos:
st.write("Esto es un botón")
st.button('Click!')
st.checkbox('Aceptar')
st.radio('Escoge tu favorito', ['gatos', 'perros', 'tacos', 'cerveza'])
st.selectbox('Selecciona uno:', ['gatos', 'perros', 'tacos', 'cerveza'])
st.multiselect('Lista de compras:', ['leche', 'manzanas', 'carne', 'cerveza'])
st.slider('Selecciona un número', 0, 100)
st.select_slider('Escoge una talla', ['S', 'M', 'L'])
st.text_input('Ingresa tu nombre')
st.number_input('Ingresa un número de 1 a 10:', 0, 10)
st.text_area('Cuadro de texto')
st.date_input('Calendario')
st.time_input('Selecciona una hora:')
st.file_uploader('Cargar un archivo')
st.color_picker('Tu color favorito!')

# Interactuando con el usuario:
st.title('Interactuando con el usuario:')
for i in range(int(st.number_input('Ingresa un número:'))):
   st.write(i)
if st.sidebar.selectbox('Selecciona una letra:',['a','b','c','d','e','f']) == 'f':
   st.write('seleccionaste la letra f')
seleccion_de_edad = st.slider('Edad del Usuario', 1, 88)
try:
    st.write("tu edad es: ", seleccion_de_edad, "años.")
except:
    st.write('todo va bien')
    '''
