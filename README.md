# Car Price Prediction Microservice

This project aims to build a microservice that predicts the price of a car based on input features.

### Note : this is not the final version... The project still needs develop and review. 

We can summarize what has been done on this repo so far in the next steps:

##### STEP 1 < Data Preprocessing > includes : 
1. Data Extraction:
Utilize text files to extract the necessary information and features for training a predictive model.
2. Data Cleaning and Transformation:
- Perform data cleaning to handle missing values and outliers.
- Transform the data as needed, ensuring it is in a suitable format for model training.

3. Feature Engineering:
- Engineer new features or modify existing ones to enhance the model's predictive power.
- Drop un needed features

4. Exploratory Data Analysis (EDA):
- Conduct an explorative data analysis to understand the characteristics of the dataset.
- Explore the relationships between different features and the target variable (car price).

##### STEP 2 < Model > includes : 

1. Model Selection:
- Consider encoding categorical variables and scaling numerical features.
- Split the dataset into training and testing sets for model evaluation.
- Model Training:
    Train the selected model on the training dataset.
- Evaluate different regression models suitable for the problem.
- Choose the best model among Polynomial Regression, kNN (k-Nearest Neighbors), and Decision Tree.

2. Microservice Development:
- Develop a Flask-based microservice that accepts input data about a car and returns the predicted price using the trained model

3. Testing:
- Test the microservice with sample input data to ensure correct functionality.
- Include sample JSON requests for testing with Postman. 

The test step did not work as expect so the microservice still under development.
