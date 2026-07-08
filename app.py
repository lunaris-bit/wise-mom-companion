import streamlit as st
import google.generativeai as genai

st.title("🔍 Detektif Model")
st.write("Klik tombol di bawah untuk melihat nama model yang tersedia untuk akun Kakak.")

# Konfigurasi API
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except Exception as e:
    st.error(f"Error API Key: {e}")

if st.button("Cek Model yang Tersedia"):
    try:
        # Ini adalah perintah untuk melihat daftar model yang diizinkan
        models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        st.success("Model yang bisa Kakak pakai:")
        st.write(models)
    except Exception as e:
        st.error(f"Error: {e}")
