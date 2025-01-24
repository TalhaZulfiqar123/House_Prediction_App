import streamlit as st
import joblib
import numpy as np

model = joblib.load("model.pkl")

st.title("House Price Prediction App")

st.divider()

st.write("This app use machine learning for predicting house price with given feature of the house. For using this app you can enter the inputs from this UI and then use predict button.")

st.divider()

bedrooms = st.number_input("Number of Bedrooms",min_value = 0, value = 0)
bathrooms = st.number_input("Number of Bathrooms",min_value = 0, value = 0)
livingarea = st.number_input("Living area", min_value = 0, value = 2000)
condition = st.number_input("Condition", min_value = 0, value = 3 )
nuberofschool = st.number_input("Number of School nearby",min_value = 0, value = 0)

st.divider()

X = [bedrooms,bathrooms,livingarea,condition,nuberofschool]

predictbutton = st.button("Predict")

if predictbutton:

    # st.balloons()

    X_array = np.array(X).reshape(1, -1) 

    prediction = model.predict(X_array)

    st.write(f"Price prediction is {prediction[0]:,.2f}")


else:
    st.write("Please use predict button after entering values ")




#  Index(['number of bedrooms', 'number of bathrooms', 'living area'
#        'condition of the house', 'Number of schools nearby'],
#       dtype='object')