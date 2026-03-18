"""
SaaS Growth Analytics – Churn & CAC Analysis
Author: Niloofar Vafa

This script performs:
- Churn rate calculation
- Churn analysis by contract type
- Basic CAC simulation
- Simple visualization
"""

import pandas as pd
import matplotlib.pyplot as plt


# -----------------------------
# Data Loading
# -----------------------------

def load_data(path):
    """
    Load dataset from CSV file.
    """
    return pd.read_csv(path)


# -----------------------------
# Analytics Functions
# -----------------------------

def calculate_churn_rate(df):
    """
    Calculate overall churn distribution.
    """
    return df["Churn"].value_counts(normalize=True)


def churn_by_contract(df):
    """
    Analyze churn rate grouped by contract type.
    """
    return df.groupby("Contract")["Churn"].value_counts(normalize=True)


def estimate_cac(df, monthly_marketing_spend=10000):
    """
    Simulate Customer Acquisition Cost (CAC).
    """
    new_customers = df[df["Churn"] == "No"].shape[0]
    return monthly_marketing_spend / new_customers


# -----------------------------
# Main Execution
# -----------------------------

def main():

    # Load dataset
    df = load_data("data/WA_Fn-UseC_-Telco-Customer-Churn.csv")

    # --- Churn Distribution ---
    churn_rate = calculate_churn_rate(df)
    print("=== Churn Distribution ===")
    print(churn_rate)

    # Visualization
    churn_rate.plot(kind="bar")
    plt.title("Churn Distribution")
    plt.xlabel("Churn Status")
    plt.ylabel("Percentage")
    plt.tight_layout()
    plt.show()

    # --- Churn by Contract ---
    print("\n=== Churn by Contract Type ===")
    print(churn_by_contract(df))

    # --- CAC Simulation ---
    cac = estimate_cac(df)
    print("\n=== Estimated CAC ===")
    print("Estimated CAC:", round(cac, 2))


# Standard Python execution pattern
if __name__ == "__main__":
    main()
