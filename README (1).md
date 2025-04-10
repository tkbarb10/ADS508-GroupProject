# ADS508-GroupProject
# Space Waste: Predicting and Mitigating Space Debris

## Overview
Space debris poses an increasing threat to current and future space missions. The Space Waste project leverages data science and cloud computing to analyze, track, and predict space debris accumulation while identifying high-risk areas for cleanup. Our goal is to support NASA and other stakeholders in ensuring the long-term sustainability of Earth's orbit.

## Authors
- Anahit Shekikyan
- Taylor Kirk
- Alli McKernan

## Industry
**Aerospace and Environmental Technology**

## Company Size
**Startup**

## Problem Statement
The growing number of inactive satellites and space debris increases the risk of cascading collisions, known as *Kessler Syndrome*. These collisions can endanger operational spacecraft, disrupt global communications, and increase mission costs. Our goal is to apply data science and machine learning to:
- Predict debris accumulation trends.
- Identify high-risk zones in orbit.
- Provide NASA with actionable insights for debris mitigation.

## Project Goals
1. **Trend Analysis (1960-Present):** Analyze historical NORAD and ESA data to assess space debris accumulation rates.
2. **Debris Growth Reduction:** Reduce projected debris growth in Low Earth Orbit (LEO) by **15% over 10 years** using predictive modeling.
3. **High-Density Debris Field Identification:** Identify the **top 5 highest-density debris zones** with at least **90% accuracy** using clustering techniques.
4. **Collision Prediction:** Achieve an **AUC score of at least 0.85** when predicting the likelihood of debris collisions.
5. **Debris Removal Prioritization:** Provide NASA with **data-driven recommendations** to reduce high-risk object density by **20%** while optimizing cost.

## Data Sources
- **NORAD & ESA Data:** Historical debris tracking datasets.
- **Space-Track.org API:** Data on active/inactive LEO objects.
- **CelesTrak API:** Information on lost objects and collision events.
- **AWS S3 Storage:** Secure storage of all datasets with IAM-controlled access.

## Data Processing & Modeling
### Data Preparation
- **Feature Selection:** Removing redundant and irrelevant features.
- **Missing Data Handling:** Using imputation techniques (mean/median) for numerical features.
- **Normalization:** Standardizing numerical features for machine learning models.
- **Data Security:** Implementing encryption at rest (S3 SSE-KMS) and transit (SSL/TLS).

### Machine Learning Approaches
- **Time Series Forecasting:** ARIMA, ETS for debris growth modeling.
- **Predictive Modeling:** Random Forest, XGBoost, and LSTMs for collision prediction.
- **Clustering:** K-Means and DBSCAN to identify high-density debris fields.
- **Anomaly Detection:** Autoencoders, Isolation Forests for tracking unregistered debris.

### Model Evaluation Metrics
- **Debris Growth Forecast Accuracy:** RMSE ≤ **5%**
- **Collision Risk Model Performance:** AUC ≥ **0.85**
- **Clustering Accuracy:** ≥ **90%**
- **High-Risk Object Reduction:** **20%**

## Data Storage & Security
- **AWS S3 Bucket:** `sagemaker-us-east-1-266917422334`
- **Data Encryption:** AWS Key Management Service (KMS)
- **Access Management:** Role-based IAM policies

## Future Enhancements
- **Real-Time Tracking:** AI-powered continuous debris monitoring.
- **Automated Collision Avoidance:** Using ML-driven navigation for active satellites.
- **Reinforcement Learning (RL):** Optimizing debris removal strategies with AI.

## Repository Structure
```
├── data/                  # Raw and processed datasets
├── Goal 4 modeling/       # Notebooks for EDA and modeling
├── Variable Descriptions/ # Variable descriptions 
├── notes.md               # Project notes and miscellaneous information
├── LICENSE                # License information
├── README.md              # Project overview & instructions

```

## Getting Started
### Prerequisites
- Python 3.x
- AWS CLI & Boto3
- Jupyter Notebook
- Pandas, NumPy, Scikit-Learn, XGBoost
- AWS SageMaker Studio

### Installation
Clone the repository and install dependencies:
```bash
git clone https://github.com/tkbarb10/ADS508-GroupProject.git
cd ADS508-GroupProject
pip install -r requirements.txt
```

### Running the Project
1. **Set up AWS S3 access** using IAM roles.
2. **Download data** from Space-Track and CelesTrak APIs.
3. **Run EDA notebooks** to preprocess and explore the data.
4. **Train models** using SageMaker AutoML or custom algorithms.
5. **Evaluate model performance** and generate visualizations.


---
**GitHub Repository:** [ADS508-GroupProject](https://github.com/tkbarb10/ADS508-GroupProject)

