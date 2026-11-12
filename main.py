import streamlit as st
st.title('Health Checkup')
h=st.number_input('Enter your height in m')
a=st.number_input('Enter your weight in kg')
o=st.number_input('Enter your oxygen level')
bp=st.number_input('Enter your Blood Pressure')
                   

bmi =round(h/(a*a), 2)
st.write('your bmi is',bmi)


