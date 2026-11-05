import streamlit as st
st.title('Health Checkup')
h=st.text_input('Enter your height in m')
a=st.text_input('Enter your weight in kg')

bmi=a/(h*h)



