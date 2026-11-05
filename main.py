import streamlit as st
st.title('Health Checkup')
h=st.number_input('Enter your height in m')
a=st.number_input('Enter your weight in kg')

bmi=float(a/(h*h),2)
st.write('your bmi is',bmi)


