# set 'stenv' as interpreter for the IDE
import streamlit as st

# ----------- 1. the Hello World app -----------
# st.write('Hello world!')

# ----------- 2. widgets -----------
st.header('st.button') # header text
if st.button('click me, I am a button'): # button has text str; clause returns true if button is clicked
    st.write('The button was clicked') # write this text to the screen
else:
    st.write('The button has not been clicked')



















