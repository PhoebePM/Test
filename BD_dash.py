import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
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
    #not m or f
    num_other = gender_counts.get(not 'M' or not 'F',1)

    sizes = [num_men,num_women,num_other]
    #setting up pie chart
    label_pie_g = 'Male','Female','Other'
    colour_pie = 'b','r','g'
    #makes code thread safe
    fig, ax = plt.subplots()
    ax.pie(sizes,labels = label_pie_g, colours = colour_pie)
    st.pyplot(fig)

    #calc percentage of m and f
    #add validation to - check no null values
    total = num_men + num_women + num_other
    percent_f = round(num_women / total,2)
    percent_m = round(num_men / total,2)
    percent_o = round(num_other/ total,2)

    #table - python dictioary
    gender_f = {
        'Gender': ['Male','Female','Other'],
        'Count': [num_men, num_women, num_other],
        'Percent': [percent_m, percent_f, percent_o]
    }
    #display  data as a table
    df = pd.DataFrame(gender_f)
    st.dataframe(df)


st.set_page_config(
    page_title = "BD stats manager",
    layout = "wide",
    initial_sidebar_state= 'auto')

#column set up
col1, col2, col3 = st.columns([0.4,0.3,0.3], gap = 'small')

#setting up sidebar
with st.sidebar:
    st.header('Files')
    st.header('File upload')
    
    uploaded_file = st.file_uploader('Upload a file')
    st.header('Uploaded files')
    
    if uploaded_file is not None:
        f_name = uploaded_file.name
        #when pressed will display statistics on the file - file name on button
        st.button(label = uploaded_file.name, on_click = lambda: stats(f_name))


        


