
import streamlit as st
st.title('Daily Health Checkup')


n=st.text_input('enter your name')
a=st.number_input('enter your age')
g=st.number_input('enter the number of glasses you drink')
e=st.number_input('enter the number of minutes you exercise')
sc=st.number_input('enter your screen time in hours')
mood=st.selectbox("Choose your mood",["Happy", "Stressed", "Sad","Energetic"],)


if a<11:
  if g<4:
    st.error('You are drinking too less glasses, please increase your water intake')
  elif g>=4 and g<=8:
    st.success('You are drinking ample amount of glasses, please maintain this consistency')
  else:
    st.warning('you are drinking a little too much water, please reduce your water intake')


  if e>=80 and e<=120:
     st.success('your exercise time is good')
  elif e<80:
     st.warning('your exercise time is less')
  else:
     st.warning('your exercise time is too much, it may give physical exhausation')


  if sc>4:
    st.error('Your screen time is too much,please reduyce it ')
  elif sc<2:
    st.success('Your screen time is good ,please maintain it')
  else:            
    st.warning('Your screen time is a lttle above normal , please reduce it')


  if mood=="Happy" or mood=="Energetic":
    st.success('Always stay happy and energetic')
  elif mood=="Sad":
    st.warning('Why are you sad, stay happy and try to solve your problems')
  else:
    st.warning('Talk to someone or play to lighten your mood')


elif a>=11 and a<=39:
  if g<4:
    st.error('You are drinking too less glasses, please increase your water intake')
  elif g>=4 and g<=8:
    st.success('You are drinking ample amount of glasses, please maintain this consistency')
  else:
    st.warning('you are drinking a little too much water, please reduce your water intake')


  if e>=45 and e<=100:
     st.success('your exercise time is good')
  elif e<45:
     st.warning('your exercise time is less')
  else:
     st.warning('your exercise time is too much, it may give physical exhausation')


  if sc>6:
    st.error('Your screen time is too much,please reduyce it ')
  elif sc<3:
    st.success('Your screen time is good ,please maintain it')
  else:            
    st.warning('Your screen time is a lttle above normal , please reduce it')


  if mood=="Happy" or mood=="Energetic":
    st.success('Always stay happy and energetic')
  elif mood=="Sad":
    st.warning('Why are you sad, stay happy and try to solve your problems')
  else:
    st.warning('Talk to someone or play to lighten your mood')


else:
  if g<4:
    st.error('You are drinking too less glasses, please increase your water intake')
  elif g>=4 and g<=8:
    st.success('You are drinking ample amount of glasses, please maintain this consistency')
  else:
    st.warning('you are drinking a little too much water, please reduce your water intake')


  if e>=30 and e<=60:
     st.success('your exercise time is good')
  elif e<30:
     st.warning('your exercise time is less')
  else:
     st.warning('your exercise time is too much, it may give physical exhausation')


  if sc>4:
    st.error('Your screen time is too much,please reduyce it ')
  elif sc<2:
    st.success('Your screen time is good ,please maintain it')
  else:            
    st.warning('Your screen time is a lttle above normal , please reduce it')


  if mood=="Happy" or mood=="Energetic":
    st.success('Always stay happy and energetic')
  elif mood=="Sad":
    st.warning('take some time for yourself, stay happy and try to solve your problems')
  else:
    st.warning('Talk to someone or play to lighten your mood')

   




  
   
      




                   



