# 📈 GMF Time Series Forecasting & Portfolio Optimization

![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)![License](https://img.shields.io/badge/License-MIT-yellow.svg)

An end-to-end quantitative analysis project to enhance portfolio management strategies for Guide Me in Finance (GMF) Investments. This repository documents the process of fetching financial data, developing predictive time series models, constructing an optimal investment portfolio based on Modern Portfolio Theory (MPT), and validating the strategy through a historical backtest.

---

## 🎯 Project Overview

As a Financial Analyst at GMF Investments, the objective is to leverage data-driven insights to optimize client portfolios. This project utilizes historical financial data for three key assets with distinct risk profiles:

*   **Tesla (TSLA):** High-growth, high-volatility stock.
*   **S&P 500 ETF (SPY):** Diversified, moderate-risk market benchmark.
*   **Vanguard Total Bond Market ETF (BND):** Stable, low-risk bond fund.

By forecasting future trends for a key volatile asset and understanding asset correlations, we built and validated a portfolio that maximizes risk-adjusted returns, grounded in proven financial theories. The final model-driven strategy proved to be more efficient and less volatile than a traditional benchmark portfolio.

---

## ✨ Key Features

*   📦 **Automated Data Ingestion** – Fetches over a decade of financial data using the `yfinance` API.
*   📊 **In-Depth EDA** – Analysis of price trends, volatility, return distributions, and risk metrics.
*   🤖 **Advanced Time Series Forecasting** – A comparative analysis between a classical ARIMA model and a deep learning LSTM model to generate a forward-looking market view.
*   ⚙️ **Portfolio Optimization (MPT)** – Calculation of the Efficient Frontier and identification of the Maximum Sharpe Ratio portfolio based on the model's forecast.
*   🧪 **Strategy Backtesting** – Validation of the optimized portfolio's performance against a standard industry benchmark, confirming superior risk-adjusted returns.

---

## 🚀 Project Roadmap & Key Findings

### ✅ Completed: Task 1 – Data Preprocessing & Exploratory Data Analysis

*   Successfully ingested, cleaned, and processed ten years of historical data (July 2015 – July 2025) for TSLA, SPY, and BND.
*   Conducted in-depth EDA to understand the characteristics of each asset, identifying TSLA's significant volatility compared to the stability of SPY and BND.

### ✅ Completed: Task 2 – Developing Time Series Forecasting Models

*   Built and compared a classical ARIMA model with a deep learning LSTM model to forecast Tesla's stock price.
*   **Key Finding:** The LSTM model vastly outperformed the ARIMA model, demonstrating its superior ability to capture the non-linear dynamics of a volatile asset.

### ✅ Completed: Task 3 – Forecasting Future Market Trends

*   Utilized the superior LSTM model to generate a 12-month forward-looking forecast for TSLA.
*   **Key Finding:** The model projects a significant **bearish trend for TSLA**, with an expected annualized return of **-40.08%**. This became the central hypothesis for our optimization.

### ✅ Completed: Task 4 – Portfolio Optimization

*   Combined the LSTM's bearish forecast for TSLA with the historical returns of SPY and BND.
*   Generated the Efficient Frontier using Modern Portfolio Theory, which visually confirmed that including TSLA would be inefficient.
*   **Key Finding:** The optimal **Maximum Sharpe Ratio Portfolio** recommends a highly defensive allocation:
    *   **TSLA: 0.0%**
    *   **SPY: 21.8%**
    *   **BND: 78.2%**

### ✅ Completed: Task 5 – Strategy Backtesting & Validation

*   Conducted a one-year backtest of our recommended portfolio against a passive 60% SPY / 40% BND benchmark.
*   **Key Finding:** The model-driven strategy was **more efficient and less volatile**, achieving a superior risk-adjusted return.

---

## 🏆 Final Results & Validation

The one-year backtest confirmed the value of our data-driven approach. While the benchmark portfolio had a higher absolute return, our strategy delivered a **better return for each unit of risk taken.**

| Portfolio | Total Return | **Sharpe Ratio (Risk-Adjusted Return)** |
| :--- | :--- | :--- |
| **Our Strategy** | 6.52% | **1.07** |
| **Benchmark (60/40)** | 12.47% | **1.02** |

The higher Sharpe Ratio demonstrates that our strategy successfully translated the model's forecast into a more stable and efficient portfolio, fulfilling the core project objective.

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
├── models/               # Saved trained models
│
├── notebooks/            # Jupyter Notebooks for analysis
│   ├── 1.0-data_exploration.ipynb
│   ├── 2.0-forecasting_models.ipynb
│   ├── 3.0-forecast_future_market_trends.ipynb
│   ├── 4.0-optimize_portfolio_based_on_forecast.ipynb
│   └── 5.0-strategy_backtesting.ipynb
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

Run the notebooks in the `notebooks/` directory in sequential order to reproduce the entire analysis from start to finish.

---

## 💻 Technologies Used

*   **Python 3.10+**
*   **Libraries:**
    *   Data & Analysis: `pandas`, `numpy`, `yfinance`
    *   Visualization: `matplotlib`, `seaborn`
    *   Time Series & ML: `statsmodels`, `tensorflow`, `scikit-learn`
    *   Portfolio Optimization: `PyPortfolioOpt`