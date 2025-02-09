import streamlit as st
import pandas as pd
import joblib
import os

# Load the trained model
# model_path = os.path.join(os.path.dirname(__file__), '..', 'xgboost_property_valuation_model.pkl')
# model = joblib.load(model_path)
# print('model_path', model_path)
# model = joblib.load('xgboost_property_valuation_model.pkl')
# print(model)

# def property_valuation_page():
#     st.header("Property Valuation")
    
#     # Input fields for property details
#     size = st.number_input("Size (sq ft)", min_value=500, max_value=10000, value=1000)
#     bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
#     bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
#     location = st.selectbox("Location", ['Urban', 'Suburban', 'Rural'])

#     # Predict button
#     if st.button("Predict Price"):
#         input_data = pd.DataFrame({
#             'size': [size],
#             'bedrooms': [bedrooms],
#             'bathrooms': [bathrooms],
#             'location': [location]
#         })
        
#         predicted_price = model.predict(input_data)[0]
#         st.success(f"Estimated Property Price: ${predicted_price:,.2f}")


# Load the trained model
model = joblib.load('xgboost_property_valuation_model.pkl')

def property_valuation_page():
    st.header("Property Valuation")
    
    # Input fields for property details
    size = st.number_input("Size (sq ft)", min_value=500, max_value=10000, value=1000)
    bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
    location = st.selectbox("Location", ['Urban', 'Suburban', 'Rural'])

    # Predict button
    if st.button("Predict Price"):
        # Create input data
        input_data = pd.DataFrame({
            'size': [size],
            'bedrooms': [bedrooms],
            'bathrooms': [bathrooms],
            'location': [location]
        })
        
        # Encode the location column
        input_data['location'] = input_data['location'].astype('category').cat.codes
        
        # Make prediction
        predicted_price = model.predict(input_data)[0]
        st.success(f"Estimated Property Price: ${predicted_price:,.2f}")