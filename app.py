import streamlit as st
import joblib
model = joblib.load('spam-ham') #we are loading the pipelined model using joblib
st.title('SPAM-HAM CLASSIFIER') #creates a title in web app
ip = st.text_input('Enter the message')# creates a textbox in the web app
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0]) #st.button will create a buttonwith the name predict
  #st.title(op[0]) # the 0th element in op variable is displayed as a title





