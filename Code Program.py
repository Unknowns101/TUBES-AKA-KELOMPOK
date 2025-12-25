import streamlit as st
import time
import matplotlib.pyplot as plt
import sys

# Set limit rekursi lebih tinggi agar tidak error pada angka yang sangat panjang
sys.setrecursionlimit(2000)

# --- Algoritma Iteratif ---
def sum_digits_iterative(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# --- Algoritma Rekursif ---
def sum_digits_recursive(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits_recursive(n // 10)

# --- UI Streamlit ---
st.set_page_config(page_title="Analisis Kompleksitas Algoritma", layout="wide")

st.title("📊 Analisis Kompleksitas: Penjumlahan Digit")
st.write("Membandingkan performa algoritma **Iteratif** vs **Rekursif**.")

with st.sidebar:
    st.header("Input Data")
    input_num = st.text_input("Masukkan bilangan bulat (bisa sangat panjang):", "123456789")
    
if input_num:
    try:
        num = int(input_num)
        
        col1, col2 = st.columns(2)

        # Eksekusi Iteratif
        start_time = time.perf_counter()
        res_iter = sum_digits_iterative(num)
        end_time = time.perf_counter()
        time_iter = end_time - start_time

        # Eksekusi Rekursif
        start_time = time.perf_counter()
        res_recursive = sum_digits_recursive(num)
        end_time = time.perf_counter()
        time_recursive = end_time - start_time

        # Tampilan Hasil
        with col1:
            st.subheader("Hasil Perhitungan")
            st.success(f"Hasil: **{res_iter}**")
            st.info(f"Waktu Iteratif: {time_iter:.8f} detik")
            st.info(f"Waktu Rekursif: {time_recursive:.8f} detik")

        with col2:
            st.subheader("Visualisasi Performa")
            fig, ax = plt.subplots()
            algos = ['Iteratif', 'Rekursif']
            times = [time_iter, time_recursive]
            ax.bar(algos, times, color=['#3498db', '#e74c3c'])
            ax.set_ylabel('Waktu (detik)')
            st.pyplot(fig)

        # --- Penjelasan Teoretis ---
        st.divider()
        st.subheader("📝 Analisis Kompleksitas")
        
        tab1, tab2 = st.tabs(["Kompleksitas Waktu", "Kompleksitas Ruang"])
        
        with tab1:
            st.write("Kedua algoritma memiliki kompleksitas waktu yang sama, yaitu:")
            st.latex(r"O(d) \text{ dimana } d = \text{jumlah digit}")
            st.write("Karena setiap digit harus dikunjungi tepat satu kali.")

        with tab2:
            st.write("Di sinilah perbedaan utamanya:")
            st.markdown("""
            * **Iteratif:** $O(1)$ - Hanya menggunakan sedikit variabel tambahan.
            * **Rekursif:** $O(d)$ - Membutuhkan *memory stack* untuk setiap pemanggilan fungsi.
            """)

    except ValueError:
        st.error("Mohon masukkan angka bulat yang valid.")
    except RecursionError:
        st.error("Angka terlalu panjang! Rekursi mencapai batas maksimum (Stack Overflow).")