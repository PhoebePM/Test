import streamlit as st
import pandas as pd
import numpy as np



#removed max rows that can be displayed 
pd.set_option("display.max_rows", None)

#this is what will be displayed on the main page - statistics
def stats(name_f):
    with col1:
        
        gender(name_f)

def gender(file):
    data = pd.read_excel("%s"%file,"member_data")
    #table of number of m and f
    gender_counts = data['sex_life_1'].value_counts()
    num_women = gender_counts.get('F', 0)
    num_men = gender_counts.get('M',0)
    num_people = gender_counts.get(not 'M' or not 'F',1)

    #calc percentage of m and f
    #add validation to - check no null values
    total = num_men + num_women + num_people
    percent_f = round(num_women / total,2)
    percent_m = round(num_men / total,2)
    #table - python dictioary
    gender_f = {
        'Gender': ['Male','Female'],
        'Count': [num_men, num_women],
        'Percent': [percent_m, percent_f]
    }

    df = pd.DataFrame(gender_f)
    st.dataframe(df)


st.set_page_config(
    page_title = "BD stats manager",
    layout = "wide",
    initial_sidebar_state= 'auto')

col1, col2, col3 = st.columns(0.4,0.3,0.3,gap ='small',vertical_alignment= 'top')


with st.sidebar:
    st.header('Files')
    st.header('File upload')
    
    uploaded_file = st.file_uploader('Upload a file')
    st.header('Uploaded files')
    
    if uploaded_file is not None:
        f_name = uploaded_file.name
        #when pressed will display statistics on the file - file name on button
        st.button(label = uploaded_file.name, on_click = lambda f_name: stats(f_name))


        


