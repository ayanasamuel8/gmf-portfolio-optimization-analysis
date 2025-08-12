# 📈 GMF Time Series Forecasting & Portfolio Optimization

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)![License](https://img.shields.io/badge/License-MIT-yellow.svg)

An end-to-end quantitative analysis project to enhance portfolio management strategies for Guide Me in Finance (GMF) Investments. This repository documents the process of fetching financial data, developing predictive time series models, and constructing an optimal investment portfolio based on Modern Portfolio Theory (MPT).

---

## 🎯 Project Overview

As a Financial Analyst at GMF Investments, the objective is to leverage data-driven insights to optimize client portfolios. This project utilizes historical financial data for three key assets with distinct risk profiles:

*   **Tesla (TSLA):** High-growth, high-volatility stock.
*   **S&P 500 ETF (SPY):** Diversified, moderate-risk market benchmark.
*   **Vanguard Total Bond Market ETF (BND):** Stable, low-risk bond fund.

By forecasting future trends for a key volatile asset and understanding asset correlations, we aim to build and validate a portfolio that maximizes risk-adjusted returns, grounded in proven financial theories.

---

## ✨ Key Features

*   📦 **Automated Data Ingestion** – Fetches over a decade of financial data using the `yfinance` API.
*   📊 **In-Depth EDA** – Analysis of price trends, volatility, return distributions, and risk metrics.
*   🤖 **Advanced Time Series Forecasting** – A comparative analysis between a classical ARIMA model and a deep learning LSTM model to generate a forward-looking market view.
*   ⚙️ **Portfolio Optimization (MPT)** – A framework to calculate the Efficient Frontier and identify key portfolios based on forecasted returns.
*   🧪 **Strategy Backtesting** – A system to validate the performance of the model-driven portfolio against a standard industry benchmark.

---

## 🚀 Project Roadmap & Key Findings

### ✅ Completed: Task 1 – Data Preprocessing & Exploratory Data Analysis

*   Successfully ingested, cleaned, and processed ten years of historical data (July 2015 – July 2025) for TSLA, SPY, and BND.
*   Conducted in-depth EDA to understand the characteristics of each asset, identifying TSLA's significant volatility compared to the stability of SPY and BND.
*   Calculated foundational risk metrics like Value at Risk (VaR) to establish a baseline understanding of portfolio risk.

### ✅ Completed: Task 2 – Developing Time Series Forecasting Models

*   Built and compared a classical ARIMA model with a deep learning LSTM model to forecast Tesla's stock price.
*   **Key Finding:** The LSTM model vastly outperformed the ARIMA model, demonstrating its superior ability to capture the non-linear dynamics of a volatile asset. The LSTM achieved a Mean Absolute Percentage Error (MAPE) of **4.73%** on the test set, compared to the ARIMA model's **24.05%**.

### ✅ Completed: Task 3 – Forecasting Future Market Trends

*   Utilized the superior LSTM model to generate a 12-month forward-looking forecast for TSLA.
*   **Key Finding:** The model projects a significant **bearish trend for TSLA**, with an expected annualized return of **-40.08%**.
*   Generated 95% confidence intervals for the forecast, visually demonstrating that predictive certainty decreases significantly over the long term. This insight is crucial for risk management.

### ➡️ Next Steps:

#### 🎯 Task 4: Portfolio Optimization

*   Combine the LSTM's bearish forecast for TSLA with the historical returns of SPY and BND to create a vector of expected returns.
*   Use the historical covariance matrix and the principles of MPT to generate the Efficient Frontier.
*   Identify and analyze the "Maximum Sharpe Ratio" and "Minimum Volatility" portfolios based on these inputs.

#### 📜 Task 5: Strategy Backtesting & Validation

*   Conduct a one-year backtest of the optimized portfolio strategy.
*   Compare its performance (total return, Sharpe Ratio) against a passive 60% SPY / 40% BND benchmark to validate the effectiveness of our data-driven approach.

---

## 🔮 Forecasting Highlights

*   **Model Selection:** The LSTM model was unequivocally chosen over ARIMA for its **4x better performance** on the historical test set, proving its value for complex, non-linear assets like TSLA.
*   **Forward-Looking View:** Our final forecast provides a strong, data-driven signal of a potential **-40% downturn** in TSLA over the next 12 months. This bearish view is the central hypothesis for the portfolio optimization task.
*   **Risk & Uncertainty:** The forecast's confidence intervals widen dramatically over time. This reinforces a key investment principle: long-term point forecasts are highly unreliable, and models are best used to understand potential trends and risk levels.

---

## 🗂 Project Structure

```
gmf-portfolio-optimization-analysis/
│
├── .github/              # GitHub Actions for CI/CD
├── data/
│   ├── processed/        # Processed data, forecasts
│   └── raw/              # Raw data from yfinance
│
├── models/               # Saved trained models (e.g., final LSTM model)
│
├── notebooks/            # Jupyter Notebooks for analysis
│   ├── 1.0-data_exploration.ipynb
│   ├── 2.0-forecasting_models.ipynb
│   └── 3.0-future_trends_forecast.ipynb
│
├── reports/              # Final reports & figures
│   └── figures/
│
├── src/                  # Source code
│   ├── data_ingestion.py # Script to fetch data
│   └── utils.py          # Helper functions
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🛠 Setup & Installation

1.  **Clone Repository**
    ```bash
    git clone https://github.com/your-username/gmf-portfolio-optimization-analysis.git
    cd gmf-portfolio-optimization-analysis
    ```
2.  **Create Virtual Environment**

    **Windows:**
    ```bash
    python -m venv venv
    .\venv\Scripts\Activate
    ```
    **macOS / Linux:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🚀 How to Use

**Step 1 – Data Ingestion:**

```bash
python src/data_ingestion.py
```

This populates the `data/raw/` directory with the necessary CSV files.

**Step 2 – Run Analysis Notebooks:**

Open Jupyter Lab or Jupyter Notebook:

```bash
jupyter lab
```

Run the notebooks in the `notebooks/` directory in the following order to reproduce the analysis:
1.  `1.0-data_exploration.ipynb`
2.  `2.0-forecasting_models.ipynb`
3.  `3.0-future_trends_forecast.ipynb`

---

## 💻 Technologies Used

*   **Python 3.10+**
*   **Libraries:**
    *   Data & Analysis: `pandas`, `numpy`, `yfinance`
    *   Visualization: `matplotlib`, `seaborn`
    *   Time Series & ML: `statsmodels`, `tensorflow`, `scikit-learn`
    *   Portfolio Optimization: `PyPortfolioOpt`