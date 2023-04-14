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






































## my notes
- Clicking a button will not cause the page to reload, instead, its status is set to "got clicked"
- Selecting a checkbox will cause the app to reload. So if use a checkbox inside a button, the button's state will be lost from refreshing the page when the checkbox got selected (reset to not-got-clicked). So if you use a button, make sure it is the last nested button you use. 


## References
- `https://30days.streamlit.app/`
- `https://docs.streamlit.io/library/api-reference/widgets/st.button`
- `https://www.youtube.com/watch?v=Yk-unX4KnV4`











