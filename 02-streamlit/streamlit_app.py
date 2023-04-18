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
import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
print(chart_data)
#            a         b         c
# 0   1.604629 -0.561202 -1.756648
# 1   0.234535 -0.639890  0.188274
# 2  -2.185051  2.692159  0.851398
# ...
# 19  0.720349 -2.312322 -0.143059
st.line_chart(chart_data)













