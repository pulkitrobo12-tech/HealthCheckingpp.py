import streamlit as st
st.title('Daily Health Checkup')
h=st.number_input('Enter your height in m')
a=st.number_input('Enter your weight in kg')
o=st.number_input('Enter your oxygen level')
bp=st.number_input('Enter your Blood Pressure')
age=st.number_input('Enter your age')
                   

bmi =round(a/(h*h), 2)
st.write('your bmi is',bmi)

if age>18:
  if bmi<18:
    st.write('You are underweight , please change your diet and include more nutrient rich food .')
    st.warning('Please visit a dietition follow his/her orders')
  elif bmi>=18 and bmi<25:
    st.write('You are healthy please maintain your lifestyle')
  elif bmi>=25 and bmi<=29.9:
    st.write('You are slightly overweight, please change your diet, reduce junk food, eat more healthy nutrient rich food and exercise daily')
    st.warning('Please visit a dietition and follow his/her orders')
  elif bmi>30 and bmi<=34.9:
     st.write('You are Class-1 Obese, please try to reduce your weight, eat less-calorie healthy food, increase physical activity and stop eating junk food')
     st.warning('Please visit a dietition and follow his/her orders')
     st.warning('Get a full health checkup from a certified doctor')
     st.error('High Opesit can cause Heart Problems, Type 2 Diabetes and other harmful problems')
  


