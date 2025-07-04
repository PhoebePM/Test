import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np


#removed max rows that can be displayed 
pd.set_option("display.max_rows", None)

#this is what will be displayed on the main page - statistics
def stats(uploaded_file):
    #places gender statistics in column one
    with col1:
        st.write(uploaded_file.name)
        st.header('Statistics On Pension File')
        get_total_pension(uploaded_file)
        portion_married(uploaded_file)
    
    with col2:
        gender(uploaded_file)
    
    with col3:
        age_variation(uploaded_file)

#showing the variation in age of the pensioners
def age_variation(file):
    data = pd.read_excel(file,sheet_name = 'member_data')
    fig = go.Figure()
    #creating box plot based on dob column
    fig.add_trace(go.Box(x = data['date_of_birth_1'] ))
    #adding labels to box plot
    fig.update_layout(
        title = 'Age Variation',
        yaxis_title = 'Pensioner Ages',
        xaxis_title = 'Date of Birth'
    )
    st.plotly_chart(fig)


def portion_married(file):
    data = pd.read_excel(file,sheet_name = 'member_data')
    #table of married status 
    married_counts = data['marital_status'].value_counts()
    st.subheader('**Marital Status Of Pensioners**')
    #generate bar chart based on data
    st.bar_chart(pd.DataFrame(married_counts))

   
def get_total_pension(file):
    data = pd.read_excel(file,sheet_name = 'member_data')
    #sums the value in the total member pension column
    total_pension = data['total_member_pension'].sum()
    st.write('**Total Of All Member Pensions:**',total_pension)


def gender(file):
    data = pd.read_excel(file,sheet_name = "member_data")
    #table of number of m and f
    gender_counts = data['sex_life_1'].value_counts()
    num_women = gender_counts.get('F', 0)
    num_men = gender_counts.get('M',0)
    #getting total number of members
    total = data.shape[0]
    #not m or f
    num_other = total - (num_women + num_men)

    sizes = [num_men,num_women,num_other]
    #setting up pie chart
    label_pie_g = 'Male','Female','N/A'
    fig = px.pie(
        names = label_pie_g,
        values = sizes,
        title = 'Sex Distribution',
        color_discrete_sequence = ['#003F5C','#BC5090','#FFA600'],

    )
    #allows for the percentages to be displayed when the section is hovered over
    fig.update_traces(textinfo = 'none', hovertemplate='%{label}: %{percent}' )
    st.plotly_chart(fig)


st.set_page_config(
    page_title = "BD stats manager",
    layout = "wide",
    initial_sidebar_state= 'auto')

#column set up
col1, col2, col3 = st.columns([0.3,0.4,0.3], gap = 'medium')

#setting up sidebar
with st.sidebar:
    st.header('Files')
    st.header('File upload')
    with col1:
        placeholder = st.empty()
        placeholder.title('Upload A File To Recieve Statistics')
        
    if 'uploaded_file' not in st.session_state:
        #dictionary that stores each file uploaded
        st.session_state.uploaded_file = {}
    
    new_file = st.file_uploader('Upload a file')
    
    if new_file is not None:
        placeholder.empty()
        #assigns the key as the name of thr file and the new_file as the value (its and object)
        st.session_state.uploaded_file[new_file.name] = new_file
        #produces a button for each file that is in our dictionary
        st.subheader('Click On File to See Stats')
        for name, file in st.session_state.uploaded_file.items():
         #when pressed will display statistics on the file - file name on button
            st.button(label = name, on_click = lambda f = file: stats(f))
