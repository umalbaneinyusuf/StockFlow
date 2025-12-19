import streamlit as st
import pandas as pd
import numpy as np
import io


st.set_page_config(page_title="StockFlow", layout="wide")

translations = {
    "English": {
        "title": "StockFlow: Demand Forecasting",
        "subtitle": "### Smart Inventory Management System",
        "sidebar_data": "1. Data Input",
        "instructions_title": "**⚠️ File Format Instructions:**",
        "inst_1": "1. File must be `.xlsx` format.",
        "inst_2": "2. Must contain a column named **`Demand`**.",
        "inst_3": "3. Preferably include a **`Month`** column.",
        "example_format": "**Example Format:**",
        "download_template": "📥 Download Empty Template",
        "upload_label": "Upload Your Excel File",
        "sidebar_method": "2. Forecasting Method",
        "select_method": "Select Method",
        "methods": ["Simple Moving Average (SMA)", "Weighted Moving Average (WMA)", "Exponential Smoothing"],
        "sma_n": "Select N (Number of Periods)",
        "wma_weights": "Ensure weights match period length (Default N=3)",
        "w1": "Weight for (t-1) [Most Recent]",
        "w2": "Weight for (t-2)",
        "w3": "Weight for (t-3) [Oldest]",
        "alpha": "Alpha (Smoothing Constant)",
        "init_forecast": "Initial Forecast (F1)",
        "results_title": "### 📊 Results & Forecasts",
        "export_title": "### 📥 Export Results",
        "download_result": "Download Results as Excel",
        "forecast_metric": "Forecast for Next Period",
        "error_col": "Error: The Excel file must contain a column named 'Demand'.",
        "upload_prompt": "👈 Please upload an Excel file from the sidebar to start."
    },
    "العربية": {
        "title": " StockFlow: نظام التنبؤ بالطلب",
        "subtitle": "### تطبيق إدارة المخزون والتنبؤ الإحصائي",
        "sidebar_data": "1. إدخال البيانات",
        "instructions_title": "**⚠️ تعليمات تنسيق الملف:**",
        "inst_1": "1. يجب أن يكون الملف بصيغة `.xlsx`.",
        "inst_2": "2. يجب أن يحتوي عمود باسم **`Demand`**.",
        "inst_3": "3. يفضل وجود عمود **`Month`**.",
        "example_format": "**مثال على التنسيق:**",
        "download_template": "📥 تحميل قالب فارغ",
        "upload_label": "ارفع ملف الإكسل هنا",
        "sidebar_method": "2. طريقة التنبؤ",
        "select_method": "اختر الطريقة",
        "methods": ["المتوسط المتحرك البسيط (SMA)", "المتوسط المتحرك الموزون (WMA)", "التمهيد الأسي (Exponential Smoothing)"],
        "sma_n": "اختر عدد الفترات (N)",
        "wma_weights": "تأكد من الأوزان (الافتراضي لـ 3 فترات)",
        "w1": "وزن الفترة (t-1) [الأحدث]",
        "w2": "وزن الفترة (t-2)",
        "w3": "وزن الفترة (t-3) [الأقدم]",
        "alpha": "معامل التمهيد (Alpha)",
        "init_forecast": "التنبؤ الأولي (F1)",
        "results_title": "### 📊 النتائج والتوقعات",
        "export_title": "### 📥 تصدير النتائج",
        "download_result": "تحميل النتائج (Excel)",
        "forecast_metric": "توقع الفترة القادمة",
        "error_col": "خطأ: الملف يجب أن يحتوي على عمود باسم 'Demand'.",
        "upload_prompt": "👉 يرجى رفع ملف إكسل من القائمة الجانبية للبدء."
    }
}

st.sidebar.header("Language / اللغة")
language = st.sidebar.radio("Select Language", ["English", "العربية"], label_visibility="collapsed")

t = translations[language]

if language == "العربية":
    st.markdown("""
        <style>
        .stApp {
            direction: rtl;
            text-align: right;
        }

        h1, h2, h3 {
            text-align: right !important;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        .stMarkdown, .stText, p, .stAlert {
            text-align: right !important;
        }

        .stDataFrame {
            direction: rtl;
        }
        [data-testid="stMetricLabel"] {
            width: 100%;
            text-align: right !important;
             display: flex;
            flex-direction: row-reverse;
        }
        [data-testid="stMetricValue"] {
            width: 100%;
            text-align: right !important;
        }
        </style>
        """, unsafe_allow_html=True)


st.title(t["title"])
st.markdown(t["subtitle"])
st.markdown("---")

st.sidebar.header(t["sidebar_data"])
st.sidebar.info(f"""
{t['instructions_title']}
{t['inst_1']}
{t['inst_2']}
{t['inst_3']}
""")

st.sidebar.markdown(t["example_format"])
example_data = pd.DataFrame({"Month": [1, 2, 3], "Demand": [120, 130, 110]})
st.sidebar.table(example_data)

def get_template():
    df_template = pd.DataFrame({"Month": [1, 2, 3, 4, 5], "Demand": [120, 130, 110, 140, 160]})
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_template.to_excel(writer, index=False, sheet_name='Sheet1')
    return output.getvalue()

st.sidebar.download_button(
    label=t["download_template"],
    data=get_template(),
    file_name="template_demand.xlsx",
    mime="application/vnd.ms-excel"
)

st.sidebar.markdown("---")
uploaded_file = st.sidebar.file_uploader(t["upload_label"], type=['xlsx'])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    
    if 'Demand' not in df.columns:
        st.error(t["error_col"])
    else:
        demand_col = df['Demand'].tolist()

        st.sidebar.header(t["sidebar_method"])

        method_options = t["methods"] 
        selected_method_text = st.sidebar.selectbox(t["select_method"], method_options)

        is_sma = selected_method_text == method_options[0]
        is_wma = selected_method_text == method_options[1]
        is_exp = selected_method_text == method_options[2]

        if is_sma:
            n = st.sidebar.number_input(t["sma_n"], min_value=2, max_value=10, value=3)
            df[f'SMA_{n}'] = df['Demand'].rolling(window=n).mean().shift(1)
            if len(demand_col) >= n:
                next_val = sum(demand_col[-n:]) / n
                st.metric(label=f"{t['forecast_metric']} ({len(demand_col)+1})", value=f"{next_val:.2f}")


        elif is_wma:
            st.sidebar.info(t["wma_weights"])
            w1 = st.sidebar.number_input(t["w1"], value=3)
            w2 = st.sidebar.number_input(t["w2"], value=2)
            w3 = st.sidebar.number_input(t["w3"], value=1)
            weights = [w1, w2, w3]

            def calculate_wma_row(data, idx, w):
                if idx < 3: return np.nan
                return ((data[idx-1]*w[0]) + (data[idx-2]*w[1]) + (data[idx-3]*w[2])) / sum(w)

            wma_values = [calculate_wma_row(demand_col, i, weights) for i in range(len(demand_col))]
            df['WMA_3'] = wma_values

            last_idx = len(demand_col)
            next_val = ((demand_col[-1]*w1) + (demand_col[-2]*w2) + (demand_col[-3]*w3)) / sum(weights)
            st.metric(label=f"{t['forecast_metric']} ({last_idx+1})", value=f"{next_val:.2f}")

        elif is_exp:
            alpha = st.sidebar.slider(t["alpha"], 0.0, 1.0, 0.1)
            initial_forecast = st.sidebar.number_input(t["init_forecast"], value=float(demand_col[0]))

            exp_forecasts = [initial_forecast]
            for i in range(1, len(demand_col)):
                new_f = exp_forecasts[i-1] + alpha * (demand_col[i-1] - exp_forecasts[i-1])
                exp_forecasts.append(new_f)

            df[f'Exp_Smoothing_{alpha}'] = exp_forecasts
            next_val = exp_forecasts[-1] + alpha * (demand_col[-1] - exp_forecasts[-1])
            st.metric(label=f"{t['forecast_metric']} ({len(demand_col)+1})", value=f"{next_val:.2f}")


        st.markdown(t["results_title"])
        st.dataframe(df)
        st.line_chart(df.set_index(df.columns[0])[['Demand', df.columns[-1]]])

        st.markdown(t["export_title"])
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Forecast_Results')

        st.download_button(
            label=t["download_result"],
            data=output.getvalue(),
            file_name="Demand_Forecast_Results.xlsx",
            mime="application/vnd.ms-excel"
        )

else:
    st.info(t["upload_prompt"])