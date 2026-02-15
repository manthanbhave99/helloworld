import streamlit as st


st.header("Manthan App")
st.write("Hello everyone, i am manthan..")

city = st.selectbox("Select City", ["Delhi", "Mumbai", "Chennai"])
st.write("You selected:", city)