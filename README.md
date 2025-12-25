# StockFlow 📊
**Smart Inventory Management & Demand Forecasting System**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-blue?logo=streamlit)](https://stockflow-opmproject.streamlit.app/)

**StockFlow** is a web-based application built with **Python** and **Streamlit** to help inventory managers and businesses forecast future demand from historical data. The project demonstrates core Operations Management (OPM) forecasting techniques in a user-friendly, interactive interface, with full support for English and Arabic (including RTL layout).

---

## Table of Contents
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [Installation & Setup](#-installation--setup)
- [How to Use](#-how-to-use)
- [Data Format & Templates](#-data-format--templates)
- [Forecasting Methods](#-forecasting-methods)
- [Exporting Results](#-exporting-results)
- [Troubleshooting](#-troubleshooting)
- [Author](#-author)
- [License](#-license)

---

## 🚀 Features
- 📈 Multiple forecasting methods:
  - Simple Moving Average (SMA) with adjustable period N.
  - Weighted Moving Average (WMA) (3-period weighted example).
  - Exponential Smoothing with customizable smoothing constant (α).
- 🌍 Bilingual support: English and Arabic (RTL UI when Arabic selected).
- 📊 Interactive visualizations comparing actual demand vs. forecast.
- 📂 Excel integration:
  - Download ready-to-use Excel template.
  - Upload historical data (.xlsx).
  - Export forecasts and results to Excel.
- 📱 Responsive: works on desktop and mobile sized screens.
- ✅ User-friendly sidebar controls for language selection and forecasting parameters.

---

## 🎬 Demo
Live demo: https://stockflow-opmproject.streamlit.app/

---

## 💻 Tech Stack
- Python — core logic
- Streamlit — web UI
- pandas — data manipulation
- numpy — numeric computations
- xlsxwriter / openpyxl — Excel handling

---

## 🛠️ Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/umalbaneinyusuf/StockFlow.git
cd StockFlow
```

2. (Optional) Create and activate a virtual environment
```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

3. Install dependencies

If you have a `requirements.txt`:
```bash
pip install -r requirements.txt
```

If there is no `requirements.txt`, install the common packages used by the app:
```bash
pip install streamlit pandas numpy xlsxwriter openpyxl
```

4. Run the app
```bash
streamlit run app.py
```

Open the printed local URL (usually http://localhost:8501) in your browser.

---

## 📋 How to Use
1. Select a language (English or Arabic) from the sidebar.
2. Download the Empty Template from the sidebar (optional) and fill in your historical data.
3. Upload your `.xlsx` file using the upload control.
4. Choose a forecasting method (SMA, WMA, or Exponential Smoothing).
5. Adjust method parameters:
   - SMA: number of periods N
   - WMA: weights (if configurable in UI)
   - Exponential Smoothing: smoothing constant α
6. View interactive charts and metrics.
7. Click "Download Results" to export the forecast and metrics to Excel.

---

## 📂 Data Format & Templates
- Required column: `Demand` (numeric).
- Optional column: `Month` (or any date/time identifier) — recommended for plotting.
- The app provides a downloadable Excel template that shows the expected column names and structure.

Example minimal Excel:
| Month     | Demand |
|-----------|--------|
| 2023-01   | 120    |
| 2023-02   | 135    |
| ...       | ...    |

---

## 🧮 Forecasting Methods Used

1. Simple Moving Average (SMA)  
   Calculates the average of the last n periods:
   $$F_{t+1} = \frac{\sum_{i=1}^{n} D_{t-i+1}}{n}$$

2. Weighted Moving Average (WMA)  
   Assigns weights to the last k observations (recent observations typically have larger weights):
   $$F_{t+1} = \frac{\sum_{i=1}^{k} w_i \cdot D_{t-i+1}}{\sum_{i=1}^{k} w_i}$$

3. Exponential Smoothing  
   Smooths forecasts using a smoothing constant α (0 < α ≤ 1):
   $$F_{new} = F_{old} + \alpha (A_{old} - F_{old})$$

---

## 📤 Exporting Results
- Use the "Download Results" button in the app to produce an Excel workbook containing:
  - Original data
  - Forecast values
  - Any computed error metrics and charts (if implemented)

---

## ⚠️ Troubleshooting
- If you get Excel-related errors, ensure `openpyxl` and/or `xlsxwriter` are installed:
  ```bash
  pip install openpyxl xlsxwriter
  ```
- If Streamlit does not start, confirm Python version (3.8+) and that the virtual environment is activated.
- For large datasets, performance may depend on your machine; consider sampling or increasing available memory.

---

## 👤 Author
Um Al-banein Yusuf — Front-End Developer  

---

## 📜 License
Please add a LICENSE file to the repository to clarify usage (e.g., MIT). If you want, I can add a suggested LICENSE file for you.
