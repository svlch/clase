import streamlit as st
st.title('Comenzando con una buena alimentación')
st.sidebar.header('¿En qué consiste una buena alimentación?')
st.sidebar.write('Una alimentación saludable es aquella que proporciona los nutrientes que el cuerpo necesita para mantener el buen funcionamiento del organismo, conservar o restablecer la salud y minimizar el riesgo de enfermedades.')
opciones=['si','no']
saludable=st.sidebar.radio('Tienes una alimentación saludable?',opciones)
if saludable=='si':
    st.sidebar.image('https://img.freepik.com/vector-gratis/personas-sanas-llevando-diferentes-iconos_53876-43069.jpg?w=2000')
if saludable=='no':
    st.sidebar.image('https://thumbs.dreamstime.com/b/persona-deprimida-triste-d-51186816.jpg')
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
st.text('que debe consumir por día.')
st.subheader('El plato el buen comer')
st.text('Es una guía diseñada por mexicanos para mexicanos con la finalidad de orientar ')
st.text('a la población hacia una alimentación saludable,')
st.text('adecuada a nuestra cultura, costumbres,necesidades y posibilidades personales.')
st.image('https://www.gob.mx/cms/uploads/image/file/489745/plato_bien_comer_2.jpg')
st.markdown('**_¿Cuántas calorías debo consumir al día?_**')
st.latex(r'''
Mujeres=655+(9.6*peso)+(1.8*altura)-(4.7*edad)
''')
peso=st.number_input("Ingresa tu peso en kg",40)
altura=st.number_input("Ingresa tu estatura en metros",1.4)
edad=st.number_input('Ingresa tu edad',15)
Calorías=655+(9.6*peso)+(1.8*altura)-(4.7*edad)
st.write(Calorías)
st.text('El resultado es la cantidad de calorías promedio que necesita el cuerpo para')
st.text('cumplir las funciones básicas.(Estando en reposo)')
estilo=st.radio('¿Qué estilo de vida llevas?',('Sedentario','Ligeramente activo','Moderadamente activo','Muy activo'))
if estilo=='Sedentario':
    multi=Calorías*1.40
    st.write(multi)
if estilo=='Ligeramente activo':
    multi=Calorías*1.69
    st.write(multi)
if estilo=='Moderadamente activo':
    multi=Calorías*1.80
    st.write(multi)
if estilo=='Muy activo':
    multi=Calorías*2
    st.write(multi)
st.text('Cantidad de calorias (aproximadas) que gasta el cuerpo dependiendo el estilo de vida seleccionado.')
st.latex(r'''
Hombres=66+(13.7*peso)+(5*altura)-(6.8*edad)
''')
masa=st.number_input("Ingresa tu peso en kg",50)
estatura=st.number_input("Ingresa tu estatura en metros",1.60)
edad=st.number_input('Ingresa tu edad',16)
cals=66+(13.7*masa)+(5*estatura)-(6.8*edad)
st.write(cals)
st.text('El resultado es la cantidad de calorías promedio que necesita el cuerpo para')
st.text('cumplir las funciones básicas.(Estando en reposo)')
esti=st.radio('¿Qué estilo de vida llevas?',('sedentario','ligeramente activo','moderadamente activo','muy activo'))
if esti=='sedentario':
    mult=cals*1.40
    st.write(mult)
if esti=='ligeramente activo':
    mult=cals*1.69
    st.write(mult)
if esti=='moderadamente activo':
    mult=cals*1.80
    st.write(mult)
if esti=='muy activo':
    mult=cals*2
    st.write(mult)
st.text('Cantidad de calorias (aproximadas) que gasta el cuerpo dependiendo el estilo de vida seleccionado.')
st.subheader('¿Qué platillo elegírias?')
plato=['Pollo, frijoles, arroz, lechuga, tomate y tortillas de maíz', 'Huevo, frijoles, tortillas de maiz','Pescado, arroz, lechuga, tomate']
opcioness=st.selectbox('Escoge los alimentos que desees',('Pollo, frijoles, arroz, lechuga, tomate y tortillas de maíz', 'Huevo, frijoles, tortillas de maiz','Pescado, arroz, lechuga, tomate' ))
if opcioness=='Pollo, frijoles, arroz, lechuga, tomate y tortillas de maíz':
    st.text('Este platillo contiene 383 calorías')
if opcioness=='Huevo, frijoles, tortillas de maiz':
     st.text('Este platillo contiene 400 calorías')
if opcioness=='Pescado, arroz, lechuga, tomate':
    st.text('Este platillo contiene 138 calorías')
st.subheader('¿Para qué tener una buena alimentación?')
st.text('El tener una buena alimentación nos proporciona los nutrientes y vitaminas necesarios')
st.text('para que nuestro organismo logre tener un buen funcionamiento, lograr mantenerlo')
st.text('sano y fortalecer el sistema inmune.')

st.caption('Elaborado por: Paulina Cano, Valentina López, Luis Luna y Mariana Silva del grupo 4O')
st.text('Universidad Autónoma de Chihuahua, FCQ')
