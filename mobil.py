import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Class untuk kendaraan
class Vehicle:
    def __init__(self, make, model, year, purchase_price):
        self.make = make
        self.model = model
        self.year = year
        self.purchase_price = purchase_price
        self.selling_price = None
    def set_selling_price(self, selling_price):
        self.selling_price = selling_price
    def profit(self):
        if self.selling_price is not None:
            return self.selling_price - self.purchase_price
        return None
    
# Inisialisasi data kendaraan
if 'vehicles' not in st.session_state:
    st.session_state.vehicles = []
    
if 'sales' not in st.session_state:
    st.session_state.sales = []
    
# Judul aplikasi
st.title("🚗 Aplikasi Penjualan Kendaraan ")

# Navbar untuk memilih opsi
menu = [ "Dashboard", "🆕 Tambah Kendaraan", "💰 Proses Penjualan", "📈 Hitung Keuntungan", "📊 Tampilkan Grafik"]
choice = st.sidebar.selectbox("Pilih Opsi", menu)

if choice == "Dashboard":
    st.image("Project DDp.jpg", caption="", use_container_width=True)
    st.image("kelompok.jpg", caption="", use_container_width=True)
    st.write("Kami membuat aplikasi bertemakan “Penjualan Kendaraan” yang bertujuan untuk mengetahui keuntungan dari perolehan menjual kendaraan. Aplikasi ini dapat memudahkan perusahaan untuk menghitung keuntungan dengan mudah dan cepat. Kami membuat project aplikasi ini juga untuk memenuhi nilai project uas dalam mata kuliah DDP (Dasar-Dasar Pemograman) .")
    
    if st.session_state.vehicles:
        st.subheader("Data Kendaraan")
        for vehicle in st.session_state.vehicles:
            st.write(f"- {vehicle.make} {vehicle.model} ({vehicle.year}), Harga Beli: Rp {vehicle.purchase_price:,}")
    else:
        st.write("Belum ada data kendaraan.")

    st.subheader("Data Penjualan")
    sales = [v for v in st.session_state.vehicles if v.selling_price is not None]
    if sales:
        for vehicle in sales:
            st.write(f"- {vehicle.make} {vehicle.model} ({vehicle.year}) dijual dengan keuntungan Rp {vehicle.profit():,}")
    else:
        st.write("Belum ada data penjualan.")
        
    # Grafik keuntungan
    st.subheader("Grafik Keuntungan Penjualan")
    profits = [v.profit() for v in st.session_state.vehicles if v.profit() is not None]
    vehicle_names = [f"{v.make} {v.model} ({v.year})" for v in st.session_state.vehicles if v.profit() is not None]
    if profits:
        plt.figure(figsize=(10, 5))
        plt.bar(vehicle_names, profits, color='blue')
        plt.xlabel('Kendaraan')
        plt.ylabel('Keuntungan')
        plt.title('Keuntungan dari Penjualan Kendaraan')
        plt.xticks(rotation=45)
        st.pyplot(plt)
    else:
        st.write("🚫 Tidak ada keuntungan yang tersedia untuk ditampilkan.")
        
    

# Opsi untuk menambah kendaraan
if choice == "🆕 Tambah Kendaraan":
    st.header("Tambah Kendaraan")
    with st.form(key='vehicle_form'):
        make = st.text_input("Merek")
        model = st.text_input("Model")
        year = st.number_input("Tahun", min_value=1900, max_value=2024)
        purchase_price = st.number_input("Harga Beli", min_value=0)
        submit_button = st.form_submit_button("Tambah Kendaraan")
        
        if submit_button:
            vehicle = Vehicle(make, model, year, purchase_price)
            st.session_state.vehicles.append(vehicle)
            st.success("✅ Kendaraan berhasil ditambahkan!")
    # Menampilkan daftar kendaraan
    if st.session_state.vehicles:
        st.subheader("Daftar Kendaraan")
        for v in st.session_state.vehicles:
            st.write(f"{v.make} {v.model} ({v.year}) - Harga Beli: {v.purchase_price}")
# Opsi untuk memproses penjualan
elif choice == "💰 Proses Penjualan":
    st.header("Proses Penjualan Kendaraan")
    if st.session_state.vehicles:
        selected_vehicle = st.selectbox("Pilih Kendaraan", [f"{v.make} {v.model} ({v.year})" for v in st.session_state.vehicles])
        selling_price = st.number_input("Harga Jual", min_value=0)
        if st.button("Proses Penjualan"):
            vehicle = next(v for v in st.session_state.vehicles if f"{v.make} {v.model} ({v.year})" == selected_vehicle)
            vehicle.set_selling_price(selling_price)
            st.success(f"✅ Kendaraan {selected_vehicle} berhasil dijual dengan harga {selling_price}.")
    else:
        st.write("🚫 Tidak ada kendaraan yang tersedia untuk dijual.")
# Opsi untuk menghitung keuntungan
elif choice == "📈 Hitung Keuntungan":
    st.header("Hitung Keuntungan Penjualan")
    if st.session_state.vehicles:
        selected_vehicle = st.selectbox("Pilih Kendaraan", [f"{v.make} {v.model} ({v.year})" for v in st.session_state.vehicles])
        
        vehicle = next(v for v in st.session_state.vehicles if f"{v.make} {v.model} ({v.year})" == selected_vehicle)
        profit = vehicle.profit()
        
        if profit is not None:
            st.success(f"💵 Keuntungan dari penjualan {selected_vehicle} adalah {profit}.")
        else:
            st.warning("⚠️ Harga jual belum ditentukan untuk kendaraan ini.")
    else:
        st.write("🚫 Tidak ada kendaraan yang tersedia untuk menghitung keuntungan.")
# Opsi untuk menampilkan grafik
elif choice == "📊 Tampilkan Grafik":
    st.header("Grafik Keuntungan Penjualan")
    if st.session_state.vehicles:
        profits = [v.profit() for v in st.session_state.vehicles if v.profit() is not None]
        vehicle_names = [f"{v.make} {v.model} ({v.year})" for v in st.session_state.vehicles if v.profit() is not None]
        if profits:
            plt.figure(figsize=(10, 5))
            plt.bar(vehicle_names, profits, color='blue')
            plt.xlabel('Kendaraan')
            plt.ylabel('Keuntungan')
            plt.title('Keuntungan dari Penjualan Kendaraan')
            plt.xticks(rotation=45)
            st.pyplot(plt)
        else:
            st.write("🚫 Tidak ada keuntungan yang tersedia untuk ditampilkan.")
    else:
        st.write("🚫 Tidak ada kendaraan yang tersedia untuk menampilkan grafik.")