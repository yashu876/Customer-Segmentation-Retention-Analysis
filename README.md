# Customer Segmentation & Retention Analysis

## Project Overview

This project analyzes customer purchasing behavior using the Online Retail dataset to identify valuable customer segments, understand buying patterns, and support data-driven customer retention strategies.

The project follows a real-world data science workflow, starting from data understanding and cleaning, followed by exploratory data analysis, RFM feature engineering, customer segmentation using K-Means clustering, and later extending to churn prediction and an interactive dashboard.

---

## Business Problem

An e-commerce company has thousands of customers but lacks insights into:

* Who are the most valuable customers?
* Which customers are becoming inactive?
* Which customers should receive retention campaigns?
* How can customer groups be targeted effectively?

This project aims to answer these questions through customer segmentation.

---

## Dataset

**Dataset:** Online Retail Dataset

The dataset contains transactional records including:

* Invoice Number
* Product Information
* Quantity Purchased
* Unit Price
* Customer ID
* Invoice Date
* Country

Each row represents a single transaction item purchased by a customer.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Jupyter Notebook / Google Colab

---

## Project Workflow

### ✅ Phase 1: Business Understanding

* Defined business objectives
* Identified customer segmentation as the primary goal

### ✅ Phase 2: Data Understanding

* Explored dataset structure
* Understood each feature
* Analyzed missing values
* Investigated transaction records
* Identified cancellation invoices

### ✅ Phase 3: Data Cleaning

* Converted InvoiceDate to datetime
* Removed records with missing CustomerID
* Removed return/cancellation transactions
* Investigated duplicate records
* Created Revenue feature

### ✅ Phase 4: Exploratory Data Analysis

Performed analysis on:

* Revenue
* Customers
* Products
* Countries
* Purchase behavior

Generated business insights from customer purchasing patterns.

### ✅ Phase 5: RFM Analysis

Created customer-level features:

* Recency
* Frequency
* Monetary

Applied feature transformation and scaling before clustering.

### ✅ Phase 6: Customer Segmentation

* Determined the optimal number of clusters using the Elbow Method
* Applied K-Means clustering
* Identified customer groups based on purchasing behavior

---

## Current Progress

* [x] Business Understanding
* [x] Data Understanding
* [x] Data Cleaning
* [x] Exploratory Data Analysis
* [x] Revenue Feature Engineering
* [x] RFM Feature Engineering
* [x] Feature Scaling
* [x] Elbow Method
* [x] K-Means Clustering
* [ ] Customer Segment Interpretation
* [ ] Retention Strategy Recommendations
* [ ] Churn Prediction
* [ ] Streamlit Dashboard

---

## Repository Structure

```
customer-segmentation-retention-analysis/
│
├── data/
├── notebooks/
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Future Improvements

* Business interpretation of customer segments
* Customer retention recommendations
* Customer churn prediction using machine learning
* Interactive Streamlit dashboard
* Model evaluation and deployment

