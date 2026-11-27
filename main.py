
import streamlit as st
st.title('Daily Health Checkup')


n=st.text_input('enter your name')
a=st.number_input('enter your age')
g=st.number_input('enter the number of glasses you drink')
e=st.number_input('enter the number of minutes you exercise')
sc=st.number_input('enter your screen time in hours')
mood=st.selectbox("Choose your mood",["Happy", "Stressed", "Sad","Energetic"],)
score=0


if a<11:
  if g<5:
    st.error('You are drinking too less glasses, please increase your water intake')
    score=score+g/2+6
  elif g>=5 and g<=8:
    st.success('You are drinking ample amount of glasses, please maintain this consistency')
    score=score+25
  else:
    st.warning('you are drinking a little too much water, please reduce your water intake')
    score=score+15


  if e>=80 and e<=120:
     st.success('your exercise time is good')
     score=score+25
  elif e<80:
     st.warning('your exercise time is less, it may cause your body to become weak')
     score=score+e/4
     
  else:
     st.warning('your exercise time is too much, it may give physical exhausation')
     score=score+17


  if sc>4:
    st.error('Your screen time is too much,please reduyce it ')
    score=score+50/sc
  elif sc<2:
    st.success('Your screen time is good ,please maintain it')
    score=score+25
  else:            
    st.warning('Your screen time is a lttle above normal , please reduce it')
    score =score+17


  if mood=="Happy" or mood=="Energetic":
    st.success('Always stay happy and energetic')
    score=score+25
  elif mood=="Sad":
    st.warning('Why are you sad, stay happy and try to solve your problems')
    score=score+10
  else:
    st.warning('Talk to someone or play to lighten your mood')
    score=score+10


elif a>=11 and a<=39:
  if g<4:
    st.error('You are drinking too less glasses, please increase your water intake')
    score=score+g/2+6
  elif g>=4 and g<=8:
    st.success('You are drinking ample amount of glasses, please maintain this consistency')
    score=score+25
  else:
    st.warning('you are drinking a little too much water, please reduce your water intake')
    score=score+17


  if e>=45 and e<=100:
     st.success('your exercise time is good')
     score=score+25
  elif e<45:
     st.warning('your exercise time is less, it may make your body weak')
     score=score+e/3
  else:
     st.warning('your exercise time is too much, it may give physical exhausation')
     score=score+17


  if sc>6:
    st.error('Your screen time is too much,please reduyce it ')
    score=score+50/sc
  elif sc<3:
    st.success('Your screen time is good ,please maintain it')
    score=score+25
  else:            
    st.warning('Your screen time is a lttle above normal , please reduce it')
    score=score+17


  if mood=="Happy" or mood=="Energetic":
    st.success('Always stay happy and energetic')
    score=score+25
  elif mood=="Sad":
    st.warning('Why are you sad, stay happy and try to solve your problems')
    score=score+10
  else:
    st.warning('Talk to someone or play to lighten your mood')
    score=score+10


else:
  if g<4:
    st.error('You are drinking too less glasses, please increase your water intake')
    score=score+g/2+6
  elif g>=4 and g<=8:
    st.success('You are drinking ample amount of glasses, please maintain this consistency')
    score=score+25
  else:
    st.warning('you are drinking a little too much water, please reduce your water intake')
    score=score+17


  if e>=30 and e<=60:
     st.success('your exercise time is good')
     score=score+25
  elif e<30:
     st.warning('your exercise time is less, it may make your body weak')
     score=score+e/3.5
  else:
     st.warning('your exercise time is too much, it may give physical exhausation')


  if sc>4:
    st.error('Your screen time is too much,please reduce it ')
    score=score+35/sc
  elif sc<2:
    st.success('Your screen time is good ,please maintain it')
    score=score+25
  else:            
    st.warning('Your screen time is a lttle above normal , please reduce it')
    score=score+17


  if mood=="Happy" or mood=="Energetic":
    st.success('Always stay happy and energetic')
    score=score+25
  elif mood=="Sad":
    st.warning('take some time for yourself, stay happy and try to solve your problems')
    score+score+10
  else:
    st.warning('Talk to someone or play to lighten your mood')
    score+score+10

st.write('   ')
st.subheading('Wellness score')
st.write('Your wellnedd score is ',score,'/100')

   




  
   
      




                   



