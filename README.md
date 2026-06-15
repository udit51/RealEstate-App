# Machine Learning Project - Antigravity

This project is a Streamlit application for real estate price prediction, analysis, and features an interactive AI property assistant chatbot.

## Prerequisites

- Python 3.8+
- pip

## Installation

1.  **Dependencies**:
    ```bash
    pip install streamlit pandas numpy scikit-learn
    ```

## Running the Application

To start the application, run the following command in your terminal from the project directory:

```bash
streamlit run main.py
```

If the `streamlit` command is not found, use:

```bash
python -m streamlit run main.py
```

This will launch the application in your default web browser at `http://localhost:8501`.

## Application Structure

- `main.py`: The main entry point.
- `Pages/`: Contains the application pages.
- `chatbot.py`: Interactive AI property assistant.
- `df.pkl`, `pipeline.pkl`: Serialized data and model files.













Capstone Project Overview: Real Estate Data Science Application
In this comprehensive capstone project, the primary focus was on leveraging data science techniques to provide insights, predictions, and recommendations in the real estate domain. The project unfolds through various stages, covering data gathering, cleaning, exploratory analysis, modeling, recommendation systems, and the deployment of a user-friendly application.
Data Gathering:
The project commenced with the collection of real estate data, which was self-scraped from the 99acres website. Similar datasets from other property listing websites were also explored, ensuring a diverse and representative dataset.
Data Cleaning and Merging:
To prepare the dataset for analysis, a meticulous data cleaning process was undertaken, handling missing values and ensuring consistency. The data was then merged, bringing together information on houses and flats into a unified dataset.
Feature Engineering:
The dataset underwent feature engineering to enhance its richness and informativeness. New features, such as additional room indicators, area with type specifications, age of possession, furnish details, and a luxury score, were introduced to provide a more detailed representation of the properties.
Exploratory Data Analysis (EDA):
Univariate and multivariate analyses were conducted to uncover patterns and relationships within the data. The use of Pandas Profiling facilitated a deeper understanding of data distribution and structure.
Outlier Detection, Missing Value Imputation:
Outliers were identified and removed to ensure the robustness of subsequent analyses. Missing values, particularly in critical columns like area and bedroom, were addressed using appropriate imputation techniques.
Feature Selection:
Multiple feature selection techniques were employed to identify the most impactful variables for modeling. These included correlation analysis, random forest and gradient boosting feature importance, permutation importance, LASSO, recursive feature elimination, and SHAP (Explainable AI).
Model Selection & Productionalization:
In the Model Selection and Productionalization phase, an exhaustive comparison of various regression models was conducted to determine the most effective model for predicting property prices. The process involved implementing a detailed price prediction pipeline that incorporated encoding methods, ensuring the robustness and accuracy of the chosen model. The selected model was then deployed using Streamlit, creating an intuitive and user-friendly web interface for end-users.
The regression models considered in the comparison included:
Linear Regression:
A foundational regression model that assumes a linear relationship between the input features and the target variable.
Support Vector Regression (SVR):
A regression technique that leverages support vector machines to find a hyperplane that best fits the data, allowing for non-linear relationships.
Random Forest Regressor:
An ensemble learning method that builds a multitude of decision trees during training and outputs the average prediction of the individual trees.
Multi-layer Perceptron (MLP):
A type of artificial neural network that consists of multiple layers of nodes and is capable of learning complex patterns.
LASSO Regression:
A linear regression technique that incorporates L1 regularization, encouraging sparsity in the coefficient estimates.
Ridge Regression:
A linear regression technique with L2 regularization, which helps prevent multicollinearity and stabilizes the model.
Gradient Boosting Regressor:
An ensemble learning method that builds trees sequentially, with each tree correcting the errors of the previous ones.
Decision Tree Regressor:
A non-linear regression model that splits the dataset into subsets based on the most significant attribute at each node.
K-Nearest Neighbors Regressor:
A regression model that predicts the target variable by averaging the values of its k-nearest neighbors.
ElasticNet Regression:
A linear regression technique that combines L1 and L2 regularization terms.
The comparison involved assessing the performance of each model on relevant evaluation metrics, considering factors such as accuracy, precision, and recall. After careful evaluation, the most suitable regression model was selected based on its overall performance and ability to generalize to new data.
The chosen regression model was then integrated into a comprehensive price prediction pipeline, which included preprocessing steps, encoding methods, and handling of various features to ensure optimal performance. The final model was deployed using Streamlit, creating an interactive and user-friendly web interface for predicting property prices. This productionalization step made the model accessible to end-users, allowing them to make informed decisions in the real estate domain.
Building the Analytics Module:
An analytics module was developed to visually represent key insights about the real estate data. Geographical maps, word clouds for amenities, scatter plots, pie charts, and box plots were employed to offer users a comprehensive understanding of the market.
Building the Recommender System:
In the process of building the Recommender System, three distinct recommendation models were developed, each focusing on different aspects of the real estate dataset: top facilities, price details, and location advantages. The goal was to provide users with personalized recommendations tailored to their preferences and priorities. Additionally, a user-friendly recommendation interface was crafted using Streamlit, enhancing the accessibility of the recommendation systems.
Building the Property Assistant Chatbot:
An interactive AI assistant was integrated into the application using `streamlit-float` to help users navigate the real estate data. The chatbot provides a floating, always-available interface that can answer queries, guide users to relevant tools like the Price Predictor or Analytics page, and improve the overall user experience.

Deploying the Application on AWS:
The entire application, encompassing prediction, analytics, and recommendation functionalities, was deployed on Amazon Web Services (AWS). This step ensured the scalability and accessibility of the project.
This capstone project not only demonstrates proficiency in data science techniques such as feature engineering, exploratory analysis, and model building but also showcases the deployment of a real-world application, making valuable insights and recommendations accessible to end-users.