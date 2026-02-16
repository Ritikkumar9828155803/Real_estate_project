# 🏡 Real Estate Price Predictor & Analytics

An end-to-end **machine learning project** for predicting residential plot prices and providing an interactive analytics dashboard using real-world real estate data.

 
📁 **Data Source:** 99acres (web-scraped) + additional integrated datasets  

---

# 📌 Project Overview

This project builds a complete **data science pipeline**:

- Web scraping real estate listings from 99acres  
- Data cleaning, preprocessing, and feature engineering  
- Exploratory Data Analysis (EDA) with statistical and geospatial insights  
- Training and comparing multiple regression models  
- Selecting the best model based on evaluation metrics  
- Deploying the model using **Streamlit** for real-time predictions and analytics  

---

# 🧰 Tech Stack

- **Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn, Plotly, WordCloud  
- **Machine Learning:** Scikit-learn, XGBoost  
- **Web Scraping:** BeautifulSoup, Requests  
- **Deployment:** Streamlit  
- **Model Serialization:** Pickle / Joblib  

---

# 📊 Dataset

- Scraped property listings from **99acres**  
- Integrated additional location and pricing datasets  
- Data preprocessing steps:
  - Handling missing values (imputation)  
  - Removing duplicates  
  - Outlier detection and treatment  
  - Unit standardization (sq.ft, price formats)  
  - Encoding categorical variables  
  - Feature scaling  

---

# 🔍 Exploratory Data Analysis (EDA)

Performed detailed EDA to extract meaningful insights:

- Price distribution and skewness analysis  
- Location-wise price trends  
- Area vs price scatter plots  
- Price per sq.ft analysis  
- Correlation heatmaps  
- Word cloud of amenities  
- Geographical price visualization using maps  

These insights improved **feature selection** and **model performance**.

---

# ⚙️ Feature Engineering

Key engineered features:

- Price per square foot  
- Location encoding  
- Property type grouping  
- Rare category handling  
- Log transformation of target variable  
- Missing value imputation  

---

# 🤖 Models Implemented

The following regression models were trained and compared:

- XGBoost Regressor
- Random Forest Regressor  
- Gradient Boosting Regressor  
- Support Vector Regressor (SVR)  
- Lasso Regression  
- Ridge Regression  
- ElasticNet  
- Decision Tree Regressor  
- MLP Regressor  

---

# 📈 Evaluation Metrics

Models were evaluated using:

- R² Score  
- Mean Absolute Error (MAE)  
- Root Mean Squared Error (RMSE)  
- Cross-validation scores  

---

# 🏆 Best Model

**XGBoost Regressor** achieved the best performance with:

- Highest R² score  
- Lowest RMSE  
- Better generalization on test data  

This model was selected for deployment in the Streamlit app.

---

# 🌐 Streamlit Web App

The deployed application allows users to:

- Input property details (location, area, amenities, etc.)  
- Get real-time price predictions  
- Explore interactive analytics and visual insights  

---


