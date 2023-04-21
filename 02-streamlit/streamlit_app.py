# set 'stenv' as interpreter for the IDE
import streamlit as st

# ----------- 1. the Hello World app -----------
# st.write('Hello world!')

# ----------- 2. widgets: button -----------
# st.header('st.button') # header text
# if st.button('click me, I am a button'): # button has text str; clause returns true if button is clicked
#     st.write('The button was clicked') # write this text to the screen
# else:
#     st.write('The button has not been clicked')

# ----------- 3. st.write() -----------
# import numpy as np
# import altair as alt
# import pandas as pd
# import streamlit as st

# st.header('st.write()')
# st.write('Hello, *World!* :sunglasses:') # can display text using markdown format
# st.write(1234) # display a number
# df = pd.DataFrame({
#      'first column': [1, 2, 3, 4],
#      'second column': [10, 20, 30, 40]
#      })
# st.write(df) # display a dataframe as table
# df2 = pd.DataFrame(
#      np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c) # display a chart plot

# ----------- 4. st.slider() -----------
# import streamlit as st
# from datetime import time, datetime

# st.header('st.slider')

# st.subheader('Slider')
# age = st.slider('How old are you?', 0, 130, 10) # returns the val of the slider
# #                text of slider     min/max, default val
# st.write("I'm ", age, 'years old')

# st.subheader('Range slider')
# values = st.slider(
#      'Select a range of values',
#      0.0, 100.0, (25.0, 75.0))
# #                tuple of default range
# st.write('Values:', values)

# st.subheader('Range time slider')
# appointment = st.slider(
#      "Schedule your appointment:",
#      value=(time(11, 30), time(13, 45)))
# #    default value range as a tuple, need to specify value because skipped min/max value
# st.write("You're scheduled for:", appointment)

# st.subheader('Datetime slider')
# start_time = st.slider(
#      "When do you start?",
#      value=datetime(2020, 1, 1, 9, 30),
#      format="MM/DD/YY - hh:mm")
# #    sets the default display format of values
# st.write("Start time:", start_time)

# ----------- 5. st.line_chart() -----------
# import streamlit as st
# import pandas as pd
# import numpy as np

# st.header('Line chart')

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
# print(chart_data)
# #            a         b         c
# # 0   1.604629 -0.561202 -1.756648
# # 1   0.234535 -0.639890  0.188274
# # 2  -2.185051  2.692159  0.851398
# # ...
# # 19  0.720349 -2.312322 -0.143059
# st.line_chart(chart_data)

# import streamlit as st

# st.header('st.selectbox')
# option = st.selectbox(
#      'What is your favorite color?', # display the question
#      ('Blue', 'Red', 'Green')) # choices for users
# st.write('Your favorite color is ', option)

# import streamlit as st
# st.header('st.multiselect')
# options = st.multiselect(
#      'What are your favorite colors', # question to display
#      ['Green', 'Yellow', 'Red', 'Blue'], # list of choices
#      ['Yellow', 'Red']) # default choices
# st.write('You selected:', options)

# import streamlit as st
# st.header('st.checkbox')
# st.write ('What would you like to order?')
# icecream = st.checkbox('Ice cream')
# coffee = st.checkbox('Coffee')
# cola = st.checkbox('Cola')
# if icecream:
#      st.write("Great! Here's some more 🍦")
# if coffee: 
#      st.write("Okay, here's some coffee ☕")
# if cola:
#      st.write("Here you go 🥤")


# import streamlit as st
# import pandas as pd
# import pandas_profiling
# from streamlit_pandas_profiling import st_profile_report # pip install streamlit_pandas_profiling

# st.header('`streamlit_pandas_profiling`')
# df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
# pr = df.profile_report() # generate pandas profiling report
# st_profile_report(pr) # display

# import streamlit as st
# st.header('st.latex')
# st.latex(r'''
#      a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#      \sum_{k=0}^{n-1} ar^k =
#      a \left(\frac{1-r^{n}}{1-r}\right)
#      ''')

# import streamlit as st

# st.title('Customizing the theme of Streamlit apps')
# st.write('Contents of the `.streamlit/config.toml` file of this app')
# st.code("""
# [theme]
# primaryColor="#F39C12"
# backgroundColor="#2E86C1"
# secondaryBackgroundColor="#AED6F1"
# textColor="#FFFFFF"
# font="monospace"
# """) # display a code block
# number = st.sidebar.slider('Select a number:', 0, 10, 5)
# st.write('Selected number from slider widget is:', number)

# import streamlit as st
# st.title('st.secrets')
# st.write(st.secrets['message'])

# import streamlit as st
# import pandas as pd

# st.title('st.file_uploader')
# st.subheader('Input CSV')
# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#   df = pd.read_csv(uploaded_file)
#   st.subheader('DataFrame')
#   st.write(df)
#   st.subheader('Descriptive Statistics')
#   st.write(df.describe())
# else:
#   st.info('☝️ Upload a CSV file')

# import streamlit as st

# st.set_page_config(layout="wide") # displays the page in wide mode, otherwise the contents are in a fixed width box by default
# st.title('How to layout your Streamlit app')
# with st.expander('About this app'): # text/image inside a collapsible container box
#   st.write('This app shows the various ways on how you can layout your Streamlit app.')
#   st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

# st.sidebar.header('Input')
# user_name = st.sidebar.text_input('What is your name?')
# user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
# user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

# st.header('Output')

# col1, col2, col3 = st.columns(3) # create 3 cols

# with col1:
#   if user_name != '':
#     st.write(f'👋 Hello {user_name}!')
#   else:
#     st.write('👈  Please enter your **name**!')

# with col2:
#   if user_emoji != '':
#     st.write(f'{user_emoji} is your favorite **emoji**!')
#   else:
#     st.write('👈 Please choose an **emoji**!')

# with col3:
#   if user_food != '':
#     st.write(f'🍴 **{user_food}** is your favorite **food**!')
#   else:
#     st.write('👈 Please choose your favorite **food**!')

























