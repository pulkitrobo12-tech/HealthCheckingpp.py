import streamlit as st
st.title('Health Checkup')
h=st.number_input('Enter your height in m')
a=st.number_input('Enter your weight in kg')

bmi=round(a/(h*h))
st.write('your bmi is',bmi)


