import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Segmentation & Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("models/churn_prediction_model.pkl")

# -----------------------------
# Load Customer Data
# -----------------------------
customer_data = pd.read_csv("customer_features1.csv")

# -----------------------------
# Title
# -----------------------------
st.title("📊 Customer Segmentation & Retention Analysis")

st.write("""
This application predicts customer churn using a trained XGBoost model
and provides business recommendations.
""")

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("Project Information")

st.sidebar.write("""
**Dataset:** Online Retail Dataset

**Model:** Tuned XGBoost

**Features Used**
- Frequency
- Monetary
- Unique Products
- Average Order Value
- Average Items Per Order
""")

# -----------------------------
# Dataset Overview
# -----------------------------
st.header("📋 Customer Dataset")

st.metric("Total Customers", len(customer_data))

# -----------------------------
# Customer Selection
# -----------------------------
st.header("🔍 Select Customer")

customer_id = st.selectbox(
    "Choose Customer ID",
    customer_data["CustomerID"]
)

selected_customer = customer_data[
    customer_data["CustomerID"] == customer_id
]

st.subheader("Customer Details")

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "Frequency",
        int(selected_customer["Frequency"].values[0])
    )

    st.metric(
        "Monetary",
        f"₹{selected_customer['Monetary'].values[0]:.2f}"
    )

    st.metric(
        "Unique Products",
        int(selected_customer["UniqueProducts"].values[0])
    )
    st.metric(
        "Quantity",
        int(selected_customer["Quantity"].values[0])
    )
with col2:
     st.metric(
        "Unique Products",
        int(selected_customer["UniqueProducts"].values[0])
    )
     st.metric(
        "Average Order Value",
        f"₹{selected_customer['AvgOrderValue'].values[0]:.2f}"
    )
    

# -----------------------------
# Prediction
# -----------------------------
st.header("🤖 Churn Prediction")

if st.button("Predict Churn"):

    features = selected_customer[
        [
            "Frequency",
            "Monetary",
            "Quantity",
            "UniqueProducts",
            "AvgOrderValue"
        ]
    ]

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Customer is Likely to Churn")
    else:
        st.success("✅ Customer is Likely to Stay")

    st.write(f"**Churn Probability:** {probability:.2%}")

    st.subheader("Business Recommendation")

    if probability >= 0.70:
        st.error("""
### High Risk

Recommended Actions:

- Offer Discount Coupon
- Personalized Email Campaign
- Loyalty Rewards
- Follow-up Call
""")

    elif probability >= 0.40:
        st.warning("""
### Medium Risk

Recommended Actions:

- Recommend Similar Products
- Send Promotional Offers
- Encourage Repeat Purchases
""")

    else:
        st.success("""
### Low Risk

Recommended Actions:

- Continue Loyalty Program
- Recommend New Products
- Maintain Regular Engagement
""")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.caption(
    "Developed using Python, Streamlit, XGBoost, Pandas and Scikit-learn."
)