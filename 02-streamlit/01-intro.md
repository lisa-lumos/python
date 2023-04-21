# 1. Streamlit Intro
Streamlit is a Python library that allows the creation of interactive, data-driven web applications in Python.

## Setup
1. install Miniconda from `https://docs.conda.io/en/latest/miniconda.html`
2. create a new environment with Python 3.9 with `conda create -n stenv python=3.9`
3. activate the conda env: `conda activate stenv`. A conda environment is a folder or directory that contains a specific collection of conda packages and their dependencies. This allows them to be maintained and run separately without interference from each other.
4. install the Streamlit library: `pip install streamlit`
5. launch the Streamlit demo app: `streamlit hello`

<img src="images/01-demo.png">

## The "Hello World" app
Create a file "streamlit_app.py":
```py
# set 'stenv' as interpreter for the IDE
import streamlit as st
st.write('Hello world!')
```

To run the app, in the terminal:
```console
(base) lisa@mac16 python % conda info --envs
# conda environments:
#
base                  *  /Users/lisa/miniconda3
                         /Users/lisa/opt/anaconda3/envs/stenv

(base) lisa@mac16 python % conda activate /Users/lisa/opt/anaconda3/envs/stenv

(stenv) lisa@mac16 python % cd 02-streamlit  # cd to the folder that has the .py file

(stenv) lisa@mac16 02-streamlit % streamlit run streamlit_app.py  

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.194:8501

  For better performance, install the Watchdog module:

  $ xcode-select --install
  $ pip install watchdog
           
```
And the app opens in the browser:
<img src="images/02-hello-world.png">

## Streamlit button
```py
st.header('st.button') # header text
if st.button('click me, I am a button'): # button has text str; clause returns true if button is clicked
    st.write('The button was clicked') # write this text to the screen
else:
    st.write('The button has not been clicked')
```

Run the app, it displays:
<img src="images/03-button1.png">

If we click the button, it then displays:
<img src="images/03-button2.png">

## Data Science portfolio project
This dashboard analyzes Ken Jee's YouTube channel. It shows the KPIs that he would like to see as a YouTuber. It contains these pages:
- Aggregate metrics - overall channel health; performance in the last 6 mo vs the baseline; how each individual video performed against the baseline 
- Individual video analysis - num of views vs subscription in diff countries; views of this video in first 30 days compared to average, top 20%, top 80% videos 

See details in the folder `youtube-data-analysis`

## st.write()
st.write allows add the following to the Streamlit app: 
- Prints strings, works like st.markdown()
- Displays a Python dict
- Displays pandas DataFrame as a table
- Plots/graphs/figures from matplotlib, plotly, altair, graphviz, bokeh
- ...

```py
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write()')
st.write('Hello, *World!* :sunglasses:') # can display text using markdown format
st.write(1234) # display a number
df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df) # display a dataframe as table
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c) # display a chart plot
```

Run the app, it displays:
<img src="images/04-write.png">

## Deploy the app to Streamlit Community Cloud
Register at `https://share.streamlit.io/` and link GibHub account. 

Fill in the repo and path: 

<img src="images/05-deploy1.png">

Click "Deploy" and the app is deployed to the public cloud. Then any time you do a git push your app will update immediately.

<img src="images/05-deploy2.png">

## st.slider()
st.slider() displays a slider input widget. Data types supported: int, float, date, time, and datetime.
```py
import streamlit as st
from datetime import time, datetime

st.header('st.slider')

st.subheader('Slider')
age = st.slider('How old are you?', 0, 130, 10) # returns the val of the slider
#                text of slider     min/max, default val
st.write("I'm ", age, 'years old')

st.subheader('Range slider')
values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
#                tuple of default range
st.write('Values:', values)

st.subheader('Range time slider')
appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(13, 45)))
#    default value range as a tuple, need to specify value because skipped min/max value
st.write("You're scheduled for:", appointment)

st.subheader('Datetime slider')
start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
#    sets the default display format of values
st.write("Start time:", start_time)
```

<img src="images/06-slider.png">

## st.line_chart()
Good for "just plot this" scenarios, but less customizable. If `st.line_chart` does not guess the data specification correctly, try specifying your desired chart using `st.altair_chart`.

```py
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
```

<img src="images/07-line_chart.png">

## st.selectbox()
```py
import streamlit as st

st.header('st.selectbox')
option = st.selectbox(
     'What is your favorite color?', # display the question
     ('Blue', 'Red', 'Green')) # choices for users
st.write('Your favorite color is ', option)
```
<img src="images/08-selectbox.png">

## st.multiselect()
```py
import streamlit as st
st.header('st.multiselect')
options = st.multiselect(
     'What are your favorite colors', # question to display
     ['Green', 'Yellow', 'Red', 'Blue'], # list of choices
     ['Yellow', 'Red']) # default choices
st.write('You selected:', options)
```

<img src="images/09-multiselect.png">

## st.checkbox
```py
import streamlit as st
st.header('st.checkbox')
st.write ('What would you like to order?')
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')
if icecream:
     st.write("Great! Here's some more 🍦")
if coffee: 
     st.write("Okay, here's some coffee ☕")
if cola:
     st.write("Here you go 🥤")
```

<img src="images/10-checkbox.png">

## Streamlit Components
Components are third-party Python modules that extend Streamlit, such as `streamlit_pandas_profiling`
```py
import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report # pip install streamlit_pandas_profiling

st.header('`streamlit_pandas_profiling`')
df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
pr = df.profile_report() # generate pandas profiling report
st_profile_report(pr) # display
```

<img src="images/11-components.png">

## st.latex
Display math expressions formatted as LaTeX.
```py
import streamlit as st

st.header('st.latex')
st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''')
```

<img src="images/12-latex.png">

## App theme customization
Create a theme file in the follow path: `.streamlit/config.toml`, and put the following content in:
```
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
```

And in the python file: 
```py
import streamlit as st
st.title('Customizing the theme of Streamlit apps')
st.write('Contents of the `.streamlit/config.toml` file of this app')
st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""") # display a code block
number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
```

Note that although `streamlit run file.py` could refresh the app when the contents of the file changes, but to allow it to incorporate this theme file, we need to re-run this command. 

<img src="images/13-theme.png">

## st.secrets
Store confidential info such as API keys, database passwords, etc.
```py
import streamlit as st
st.title('st.secrets')
st.write(st.secrets['message'])
```
Secrets can be stored in Streamlit Community Cloud, or, if working locally, they can be stored in `.streamlit/secrets.toml`, but make sure to NOT uploading it to a GitHub repo when deploying the app.

## st.file_uploader
By default, uploaded files are limited to 200MB. You can configure this using the server.maxUploadSize config option.
```py
import streamlit as st
import pandas as pd

st.title('st.file_uploader')
st.subheader('Input CSV')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file)
  st.subheader('DataFrame')
  st.write(df)
  st.subheader('Descriptive Statistics')
  st.write(df.describe())
else:
  st.info('☝️ Upload a CSV file')
```

<img src="images/14-file_uploader.png">

## layouts
```py
import streamlit as st

st.set_page_config(layout="wide") # displays the page in wide mode, otherwise the contents are in a fixed width box by default
st.title('How to layout your Streamlit app')
with st.expander('About this app'): # text/image inside a collapsible container box
  st.write('This app shows the various ways on how you can layout your Streamlit app.')
  st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

st.sidebar.header('Input')
user_name = st.sidebar.text_input('What is your name?')
user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')

col1, col2, col3 = st.columns(3) # create 3 cols

with col1:
  if user_name != '':
    st.write(f'👋 Hello {user_name}!')
  else:
    st.write('👈  Please enter your **name**!')

with col2:
  if user_emoji != '':
    st.write(f'{user_emoji} is your favorite **emoji**!')
  else:
    st.write('👈 Please choose an **emoji**!')

with col3:
  if user_food != '':
    st.write(f'🍴 **{user_food}** is your favorite **food**!')
  else:
    st.write('👈 Please choose your favorite **food**!')
```

<img src="images/15-layout.png">

## 




## 




## 




## 




## 




## 




## 




## 




## 




## 




## 






## my notes
- Clicking a button will not cause the page to reload, instead, its status is set to "got clicked"
- Selecting a checkbox will cause the app to reload. So if use a checkbox inside a button, the button's state will be lost from refreshing the page when the checkbox got selected (reset to not-got-clicked). So if you use a button, make sure it is the last nested button you use. 


## References
- `https://30days.streamlit.app/`
- `https://docs.streamlit.io/library/api-reference`
- `https://share.streamlit.io/`
- `https://www.youtube.com/watch?v=Yk-unX4KnV4`











