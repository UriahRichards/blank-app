import streamlit as st
import pandas as pd
import numpy as np
#for displaying images
from PIL import Image
import seaborn as sns

st.title("Dress to Impress")

df=pd.read_csv("wine_quality_red.csv")

st.dataframe(df.head(5))
image_path = Image.open("imagr.png")
st.image(image_path,width=400)
df=pd.read_csv("wine_quality_red.csv")

st.dataframe(df.head(5))

dfnull = df.isnull()/len(df)*100
total_missing = dfnull.sum().round(2)
st.write(total_missing)
st.write(dfnull)
if total_missing[0] == 0.0:
    st.success("Congrats you are an alcholic")

    st.subheader("03 Data Visulaztion")
    list_columns = df.columns
    
    values = st.multiselect("Select two variables:", list_columns, ["quality", "citric acid"])

    #creation of the line chart
    st.line_chart(df,x=values[0],y=values[1])
    
    # Creation of the bar chart
    st.bar_chart(df,x=values[0], y=values[1])

    #Pairplot
    values_pairplot = st.multiselect("Select 4 variables:", list_columns, ["quality", "citric acid", "alcohol", "chlorides"])

    df2 = df[[values_pairplot[0],values_pairplot[1],values_pairplot[2],values_pairplot[3]]]
    st.pyplot(sns.pairplot(df2))