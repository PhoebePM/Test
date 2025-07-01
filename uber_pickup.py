import streamlit as st
import pandas as pd
import numpy as np
st.title("Ride")
pd.set_option("display.max_rows", None)
data = pd.read_excel("data1.xlsx","member_data")


def gender():
    #table of numner of m and f
    gender_counts = data['sex_life_1'].value_counts()
    num_women = gender_counts.get('F', 0)
    num_men = gender_counts.get('M',0)

    #calc percentage of m and f
    total = num_men + num_women
    percent_f = round(num_women / total,2)
    percent_m = round(num_men / total,2)
    #table
    gender_f = {
        'Gender': ['Male','Female'],
        'Count': [num_men, num_women],
        'Percent': [percent_m, percent_f]
    }

    df = pd.DataFrame(gender_f)
    st.dataframe(df)

gender()