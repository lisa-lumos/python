# Implemented following Ken Jee's YouTube tutorial video on Streamlit: 
# https://www.youtube.com/watch?v=Yk-unX4KnV4

import pandas as pd 
import numpy as np 
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from datetime import datetime

# ---- load the data ----
@st.cache # so streamlit do not need to reload the data after each page refresh
def load_data(): # put into a function so works better with streamlit
    df_agg = pd.read_csv('Aggregated_Metrics_By_Video.csv').iloc[1:,:] # skip the first row
    # in vs code, run the code in Interactive Window to see the contents in variables
    # to use this relative dir, need to cd to this folder in the terminal
    df_agg_sub = pd.read_csv('Aggregated_Metrics_By_Country_And_Subscriber_Status.csv')
    df_comments = pd.read_csv('Aggregated_Metrics_By_Video.csv')
    df_time = pd.read_csv('Video_Performance_Over_Time.csv')

    df_agg.columns = ['Video','Video title','Video publish time','Comments added','Shares','Dislikes','Likes',
                      'Subscribers lost','Subscribers gained','RPM(USD)','CPM(USD)','Average % viewed','Average view duration',
                      'Views','Watch time (hours)','Subscribers','Your estimated revenue (USD)','Impressions','Impressions ctr(%)'] # clean up the column names
    df_agg['Video publish time'] = pd.to_datetime(df_agg['Video publish time']) # convert to datetime datatype
    df_agg['Average view duration'] = df_agg['Average view duration'].apply(lambda x: datetime.strptime(x,'%H:%M:%S')) # convert to duration datetime datatype
    df_agg['Avg_duration_sec'] = df_agg['Average view duration'].apply(lambda x: x.second + x.minute*60 + x.hour*3600) # create a new col, convert duration into seconds
    df_agg['Engagement_ratio'] =  (df_agg['Comments added'] + df_agg['Shares'] +df_agg['Dislikes'] + df_agg['Likes']) /df_agg.Views # create a new col for testing and exploring, may not be useful
    df_agg['Views / sub gained'] = df_agg['Views'] / df_agg['Subscribers gained'] # create a new col for testing and exploring, may not be useful

    df_time['Date'] = pd.to_datetime(df_time['Date']) # convert to datetime datatype

    return df_agg, df_agg_sub, df_comments, df_time 

df_agg, df_agg_sub, df_comments, df_time = load_data() #create dfs from the function 
















