# import pandas as pd
# from sklearn.model_selection import train_test_split
# from xgboost import XGBRegressor
# import joblib

# # Load the dataset
# data = pd.read_csv('data/real_estate_data.csv')

# # Define features and target variable
# X = data[['size', 'bedrooms', 'bathrooms']]
# y = data['price']

# # Encode categorical variables (if any)
# data['location'] = data['location'].astype('category').cat.codes
# X['location'] = data['location']

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train an XGBoost model
# model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
# model.fit(X_train, y_train)

# # Save the model
# joblib.dump(model, 'pages/xgboost_property_valuation_model.pkl')

# print("Model trained and saved successfully!")


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from xgboost import XGBRegressor, DMatrix
# import joblib

# # Load the dataset
# data = pd.read_csv('data/real_estate_data.csv')

# # Define features and target variable
# X = data[['size', 'bedrooms', 'bathrooms', 'location']]
# y = data['price']

# # Encode the location column as a categorical variable
# X['location'] = X['location'].astype('category')

# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train an XGBoost model with categorical support
# model = XGBRegressor(
#     n_estimators=100,
#     learning_rate=0.1,
#     max_depth=5,
#     random_state=42,
#     enable_categorical=True  # Enable support for categorical variables
# )
# model.fit(X_train, y_train)

# # Save the model
# joblib.dump(model, 'pages/xgboost_property_valuation_model.pkl')

# print("Model trained and saved successfully!")


import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib

# Load the dataset
data = pd.read_csv('data/real_estate_data.csv')

# Define features and target variable
X = data[['size', 'bedrooms', 'bathrooms', 'location']]
y = data['price']

# Encode the location column as a categorical variable
X['location'] = X['location'].astype('category')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train an XGBoost model with categorical support and a compatible tree method
model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=5,
    random_state=42,
    enable_categorical=True,  # Enable support for categorical variables
    tree_method='hist'        # Use a compatible tree method
)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'pages/xgboost_property_valuation_models.pkl')

print("Model trained and saved successfully!")