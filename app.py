import streamlit as st
import google.generativeai as genai

# Konfigurasi Halaman
st.set_page_config(page_title="Wise Mom Companion", page_icon="👩‍👧‍👦")
st.title("👩‍👧‍👦 The Wise Mom Companion")
st.write("Teman bijak Bunda untuk menjawab pertanyaan si kecil dengan tenang dan santun.")

# Konfigurasi API Gemini
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
    # Model stabil yang sudah terbukti jalan di sistem Kakak
    model = genai.GenerativeModel('gemini-3.5-flash')
except Exception as e:
    st.error(f"Gagal memuat API Key atau Model: {e}")
    st.stop()

# Input Pengguna
usia = st.selectbox("Usia si kecil:", ["Balita (2-3 thn)", "Anak TK (4-6 thn)", "Anak SD (7-12 thn)"])
pertanyaan = st.text_area("Apa yang ditanyakan/dilakukan si kecil?", placeholder="Contoh: Bun, apa itu booty?")

# Tombol Action
if st.button("✨ Temukan Jawaban Bijak"):
    if pertanyaan:
        with st.spinner('Sedang meracik jawaban bijak...'):
            try:
                prompt = f"""
                Bertindaklah sebagai mentor parenting yang bijak dan penuh kasih. Berikan jawaban untuk ibu yang menghadapi situasi atau pertanyaan anak sebagai berikut:
                Anak usia: {usia}
                Situasi/Pertanyaan: {pertanyaan}
                
                Berikan output dalam dua bagian yang jelas:
                1. Skrip Jawaban untuk Bunda (bahasa lisan yang harus diucapkan ke anak, tenang, tidak menghakimi, dan edukatif).
                2. Tips Psikologis untuk Bunda (cara menenangkan diri dan kenapa jawaban ini diberikan).
                """
                
                response = model.generate_content(prompt)
                
                # Menampilkan hasil dengan rapi (tanpa kotak text_area)
                st.markdown("---")
                st.success("💬 **Skrip Jawaban Bunda:**")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"Waduh, ada error teknis nih. Pesan errornya: {e}")
    else:
        st.error("Isi dulu pertanyaannya ya, Bun!")
