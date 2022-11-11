import streamlit as st
import time
my_bar = st.progress(0)
for percent_complete in range(100):
    time.sleep(0.1)
    my_bar.progress(percent_complete + 1)
st.title('Comenzando con una buena alimentación')
st.sidebar.header('¿En qué consiste una buena alimentación?')
st.sidebar.write('Una alimentación saludable es aquella que proporciona los nutrientes que el cuerpo necesita para mantener el buen funcionamiento del organismo, conservar o restablecer la salud y minimizar el riesgo de enfermedades')
st.subheader('La jarra del buen beber')
st.text('Es una guía informativa para la población mexicana que muestra las bebidas')
st.text('saludables y la cantidad de líquidos que se recomienda consumir al día.')
st.image('https://cdn.foodandwineespanol.com/2020/09/Jarra_del_buen_Beber.jpg')
st.latex(r'''
Vasos=\frac{Peso}{7}
''')
Peso=st.number_input("Ingresa tu peso en kilos",50)
Vasos=Peso/7
st.write(Vasos)
st.text('El resultado de esta división es la cantidad de vasos de agua(250ml)')
st.text('que debe consumir por día')
st.subheader('El plato el buen comer')
st.text('Es una guía diseñada por mexicanos para mexicanos con la finalidad de orientar ')
st.text('a la población hacia una alimentación saludable,')
st.text('adecuada a nuestra cultura, costumbres,necesidades y posibilidades personales.')
st.image('https://www.gob.mx/cms/uploads/image/file/489745/plato_bien_comer_2.jpg')
