# app_pages/dashboard.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load data
df = pd.read_csv('inputs/insurance.csv')

# Matplotlib scatterplot
def scatter(df):
    fig = plt.figure(figsize=(10,8))
    ax = plt.axes(projection='3d')
    x = df['age']
    y = df['bmi']
    z = df['charges']
    ax.scatter(x, y, z)
    st.pyplot(fig)

# Seaborn stacked bar chart
def stacked(df):
    df.groupby(['smoker','region']).size().unstack().plot(kind='bar', stacked=True)
    st.pyplot(plt)

# Plotly parallel coordinates
def parallel(df):
    df = df.copy()  # Avoid modifying original df
    df['smoker'] = df['smoker'].replace({'no':0, 'yes':1})
    df['sex'] = df['sex'].replace({'male':0, 'female':1})
    df['region'] = df['region'].replace({'northwest':0, 'northeast':1, 'southwest':2, 'southeast':3})

    # Make sure all columns are numeric
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['bmi'] = pd.to_numeric(df['bmi'], errors='coerce')
    df['children'] = pd.to_numeric(df['children'], errors='coerce')
    df['charges'] = pd.to_numeric(df['charges'], errors='coerce')

    fig = px.parallel_coordinates(
        df,
        color="smoker",
        dimensions=['age','sex','bmi','children','region','charges'],
        color_continuous_scale=px.colors.sequential.Viridis
    )
    st.plotly_chart(fig, use_container_width=True)

def linechart(df):
    fig = px.line(df, x='age', y='charges', title='Age vs Charges')
    st.plotly_chart(fig, use_container_width=True)


# Dashboard page
def dashboard_body():
    st.title('Dashboard')
    st.write('This is the dashboard page')

    st.write('Scatter plot of age, bmi and charges')
    scatter(df)

    st.write('Stacked bar chart of smokers by region')
    stacked(df)

    st.write('Parallel coordinates plot')
    parallel(df)

    st.write(df.columns)
    st.write(df.head())

    st.write('Line chart of Age vs Charges')
    linechart(df)
