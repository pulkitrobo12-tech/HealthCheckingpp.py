import streamlit as st
st.title('Daily Health Checkup')


n=st.text_input('enter your name')
a=st.number_input('enter your age')
g=st.number_input('enter the number of glasses you drink')
e=st.number_input('enter the number of minutes you exercise')
sc=st.number_input('enter your screen time in hours')
mood=st.selectbox("Choose your mood",["Happy", "Stressed", "Sad","Energetic"],)


if age<10
  if g<4:
    st.error('You are drinking too less glasses, please increase your water intake')
  elif g>=4 and gt<=8:
    st.success('You are drinking ample amount of glasses, please maintain this consistency')
  else:
    st.warning('you are drinking a little too much water, please reduce your water intake')


  if m>=80 and m<=120
     st.success('your exercise time is good')
  elif m<80
     st.warning('your exercise time is less')
  else
     st.warning('your exercise time is too much, it may give physical exhausation')


  if sc>4:
    st.error('Your screen time is too much,please reduyce it ')
  elif sc<2
   




  
   
      




                   



