import streamlit as st
from core.ai_handler import get_ai_response
from core.library import load_library, find_library_case

st.set_page_config(page_title="Wise Mom Companion", page_icon="👩‍👧‍👦")
st.title("👩‍👧‍👦 The Wise Mom Companion")

usia = st.selectbox("Usia si kecil:", ["Balita (2-3 thn)", "Anak TK (4-6 thn)", "Anak SD (7-12 thn)"])
pertanyaan = st.text_area("Apa yang ditanyakan/dilakukan si kecil?", placeholder="Contoh: Bun, apa itu booty?")

if st.button("✨ Temukan Jawaban Bijak"):
    if pertanyaan:
        with st.spinner('Sedang meracik jawaban bijak...'):
            try:
                prompt = f"""
                Bertindaklah sebagai mentor parenting yang bijak.
                Anak usia: {usia}
                Situasi/Pertanyaan: {pertanyaan}
                """
                jawaban = get_ai_response(prompt)
                
                st.markdown("---")
                st.success("💬 **Jawaban:**")
                st.write(jawaban)
            except Exception as e:
                st.error(f"Error teknis: {e}")
    else:
        st.error("Isi dulu pertanyaannya ya, Bun!")
