# MSDS422 – Final Project  
## Formula One Race Outcome Prediction

### Course
MSDS 422 – Practical Machine Learning  
Northwestern University

### Team Members
- **Sara Alsiyat**
- **Qifan**
- **Boqi**

---

## Project Overview

This project applies machine learning techniques to historical Formula One race data to predict whether a driver will finish within the **top 10 positions** of a race. Finishing in the top 10 is a meaningful performance threshold in Formula One because only these drivers earn championship points under modern regulations.

The analysis follows an end-to-end machine learning workflow aligned with the **CRISP-DM** framework, beginning with data understanding and exploratory analysis, followed by feature engineering and baseline modeling. The project emphasizes realistic prediction settings through **leakage-safe feature construction** and **temporal data splits**.

---

## Research Question

To what extent can historical Formula One race data be used to predict whether a driver will finish within the top 10 positions of a race using machine learning models that integrate driver performance history, constructor strength, circuit characteristics, and broader competitive and temporal race context?

---

## Dataset

The project uses the **Formula One World Championship dataset (1950–2024)** from Kaggle. The dataset consists of multiple relational tables, including race results, qualifying performance, drivers, constructors, circuits, pit stops, standings, and race status information.

After integration, the unit of analysis is at the **driver–race level**, resulting in approximately **26,000+ observations** spanning more than seven decades of Formula One history.

**Source:**  
Vopani. *Formula 1 World Championship (1950–2024).* Kaggle, 2025.  
https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020

---

## Methodology

### Exploratory Data Analysis (EDA)
- Temporal coverage and regulation-era trends (1950–2024)
- Distribution of top-10 finishes and DNFs
- Impact of starting grid position
- Constructor dominance and driver consistency
- Circuit-level variation and reliability patterns
- Missing data analysis and visualization

### Feature Engineering
A comprehensive feature engineering pipeline was developed using **only pre-race information**. All rolling and expanding statistics apply `shift(1)` to prevent data leakage.

Feature categories include:
- Temporal and season-stage features
- Driver recent form and career history
- Constructor performance history
- Circuit characteristics and difficulty
- Driver–constructor interaction features
- Grid and qualifying-based indicators
- Competitive and championship context
- Momentum and streak indicators
- Regulation-era encodings

---

## Modeling (Exploratory Extension)

Although the primary focus of Milestone 2 is exploratory data analysis and feature engineering, baseline machine learning models were trained as an exploratory extension:

- Logistic Regression  
- Random Forest  
- Gradient Boosting  

Models were evaluated using a **temporal train–validation–test split** to reflect real-world forecasting conditions. These results are preliminary and are intended to validate the usefulness of the engineered features. Full hyperparameter tuning, interpretability analysis, and deployment considerations will be addressed in later milestones.

---

## Key Takeaways (So Far)

- Starting grid position is one of the strongest predictors of top-10 finishes.
- Constructor performance plays a dominant role across eras.
- Reliability (DNF risk) has changed substantially over time, requiring temporal context.
- Leakage-safe feature engineering is critical when working with historical sports data.
- Machine learning models show promising performance on unseen seasons.

---

## Tools & Technologies

- Python (pandas, numpy, scikit-learn)
- Matplotlib and Seaborn for visualization
- Jupyter / Google Colab
- Git and GitHub for version control

---

## Next Steps

- Hyperparameter tuning and model optimization
- Advanced models (e.g., XGBoost / LightGBM)
- Model interpretability (feature importance, SHAP)
- Validation of analytical assumptions
- Final presentation and recommendations

---

## References

A complete list of academic and data references is included in the project report and notebooks.


