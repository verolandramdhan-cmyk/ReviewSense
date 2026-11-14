import streamlit as st

st.set_page_config(
    page_title="ReviewSense",
    page_icon="*",
    layout="wide"
)

st.title("* ReviewSense*")
st.subheader("Analisis Sentimen Ulasan Google Play Store")
st.write(
    "Selamat datang di ReviewSense. " 
    "Aplikasi ini digunakan untuk membantu "
    "menganalisis sentimen ulasan pengguna."
)

st.divider()

st.header("Analisis Ulasan")

ulasan = st.text_area(
    "masukan ulasan aplikasi:"

)
if st.button("Analisis Sekarang"):
    if ulasan.strip():
        st.success("Ulasan berhasil dimasukan!")
        st.write("ulasan:", ulasan)
    else:
        st.warning("Masukan ulasan terlebih dahulu.")

st.divider()
st.caption("ReviewSense - Analisis Sentimen ")

