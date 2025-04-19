import streamlit as st

st.set_page_config(page_title="SteveAnaliz", layout="wide")
st.title("📊 SteveAnaliz Web Paneli")

st.markdown("""
Merhaba 👋  
Bu panel üzerinden SteveAnaliz verilerine erişebilir, analizleri inceleyebilirsin.
""")

ticker = st.text_input("Hisse Sembolü (örnek: AAPL)")
if ticker:
    st.success(f"Girilen sembol: {ticker}")
