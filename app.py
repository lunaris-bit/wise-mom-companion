import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Wise Mom Companion", page_icon="👩‍👧‍👦")
st.title("👩‍👧‍👦 The Wise Mom Companion")
st.write("Teman bijak Bunda untuk menjawab pertanyaan si kecil dengan tenang dan santun.")

# Konfigurasi API Gemini
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Input Pengguna
usia = st.selectbox("Usia si kecil:", ["Balita (2-3 thn)", "Anak TK (4-6 thn)", "Anak SD (7-12 thn)"])
pertanyaan = st.text_area("Apa yang ditanyakan/dilakukan si kecil?", placeholder="Contoh: Bun, apa itu booty?")

# Tombol Action
if st.button("✨ Temukan Jawaban Bijak"):
    if pertanyaan:
        with st.spinner('Sedang meracik jawaban bijak...'):
            prompt = f"""
            Bertindaklah sebagai mentor parenting yang bijak. Berikan jawaban untuk ibu yang menghadapi situasi/pertanyaan anak sebagai berikut:
            Anak usia: {usia}
            Situasi/Pertanyaan: {pertanyaan}
            
            Berikan output dalam dua bagian:
            1. Skrip Jawaban untuk Bunda (bahasa lisan yang harus diucapkan ke anak, tenang dan edukatif).
            2. Tips Psikologis untuk Bunda (cara menenangkan diri dan kenapa jawaban ini diberikan).
            """
            
            response = model.generate_content(prompt)
            
            st.markdown("---")
            st.success("💬 **Skrip Jawaban Bunda:**")
            st.write(response.text)
    else:
        st.error("Isi dulu pertanyaannya ya, Bun!")
