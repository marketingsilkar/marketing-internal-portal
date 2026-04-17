import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from PIL import Image
import os


import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="Silkar Sales & Marketing Internal Hub",
    page_icon="🏢",
    layout="wide"
)
)

# --- 1. KONFIGURASI HALAMAN ---
st.set_page_config(page_title="PT SILKAR NATIONAL - Internal Portal", page_icon="🏢", layout="wide")

# ID GOOGLE SHEETS
SHEET_ID = "1KGAm1FdUKiKTPhahHSanbc194w2TlXrTJIOVCeAGUVQ"

# --- 2. FUNGSI LOAD GAMBAR LOKAL ---
def load_local_image(file_name):
    if os.path.exists(file_name):
        return Image.open(file_name)
    return None

# --- 3. SESSION STATE UNTUK NAVIGASI ---
if 'menu_index' not in st.session_state:
    st.session_state.menu_index = 0

# --- 4. CSS KUSTOM (ANTI-BLACK BLOCK) ---
st.markdown("""
    <style>
    /* Background Utama Putih */
    .stApp { background-color: #FFFFFF !important; }
    [data-testid="stSidebar"] { display: none !important; }
    
    /* Styling tombol MEP/SIPIL agar lebih besar dan di tengah */
    div.stButton > button {
        height: 5.5rem !important;
        font-size: 1.2rem !important;
        padding: 0px 60px !important;
    }
            
    /* Font & Teks */
    h1, h2, h3, h4, p, span, div, label { 
        color: #000000 !important; 
        font-family: 'Segoe UI', Arial, sans-serif;
    }

    /* MENGHILANGKAN BLOK HITAM DI UJUNG */
    .stElementContainer:has(iframe[title="streamlit_option_menu.option_menu"]) {
        width: 100% !important;
        background-color: #FFFFFF !important;
    }
    
    iframe[title="streamlit_option_menu.option_menu"] {
        width: 100% !important;
        background-color: #FFFFFF !important;
    }

    /* Styling Tombol Berwarna */
    .stButton [key="go_harga"] button {
        background-color: #1A365D !important;
        color: #FFFFFF !important;
        border-radius: 8px;
        font-weight: 700;
        height: 3.5rem;
    }
    
    .stButton [key="go_supp"] button {
        background-color: #B28950 !important;
        color: #FFFFFF !important;
        border-radius: 8px;
        font-weight: 700;
        height: 3.5rem;
    }

    /* Styling Tambahan untuk Tombol Kategori Baru (MEP/SIPIL/SUB) */
    div.stButton > button {
        background-color: #F8F9FA !important;
        color: #1A1A1A !important;
        border: 1px solid #DDDDDD !important;
        border-radius: 8px !important;
        font-weight: 600 !important;
        height: 3rem !important;
    }

    /* Metric & Card */
    .card-box {
        padding: 30px;
        border: 1px solid #F0F0F0;
        border-radius: 15px;
        background-color: #FFFFFF;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.03);
        margin-bottom: 10px;
    }
    [data-testid="stMetric"] {
        background-color: #F8F9FA;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #EEEEEE;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 5. HEADER (LOGO & INFO) ---
head_col1, head_col2 = st.columns([2, 1])
with head_col1:
    logo = load_local_image("logo.jpg")
    if logo:
        st.image(logo, width=700)
    else:
        st.subheader("PT SILKAR NATIONAL")

with head_col2:
    st.markdown("""
        <div style="text-align: right; padding-top: 30px;">
            <p style="font-size: 12px; color: #888888; margin: 0;">INTERNAL SYSTEM ACCESS</p>
            <p style="font-size: 11px; color: #AAAAAA;">Authorized Personnel Only</p>
        </div>
    """, unsafe_allow_html=True)

# --- 6. MENU NAVIGASI ATAS ---
selected = option_menu(
    menu_title=None,
    options=["HOME", "DATABASE HARGA", "DATABASE SUPPLIER"],
    icons=["house", "currency-dollar", "people-fill"],
    menu_icon="cast",
    default_index=st.session_state.menu_index,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#FFFFFF", "border-top": "1px solid #F0F0F0", "border-bottom": "1px solid #F0F0F0", "border-radius": "0", "width": "100%", "max-width": "100%", "margin": "0 auto"},
        "icon": {"color": "#D4AF37", "font-size": "18px"}, 
        "nav-link": {"font-size": "15px", "text-align": "center", "margin":"0px", "color": "#444444", "text-transform": "uppercase", "font-weight": "600", "background-color": "#FFFFFF"},
        "nav-link-selected": {"background-color": "#F8F9FA", "color": "#D4AF37", "border-bottom": "3px solid #D4AF37", "font-weight": "800"},
    }
)

# --- 7. LOGIKA DATA ---
@st.cache_data(ttl=600)
def load_data(sheet_name):
    try:
        url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
        df = pd.read_csv(url)
        return df.dropna(how='all', axis=1).dropna(how='all', axis=0)
    except:
        return None

# --- 8. HALAMAN HOME ---
if selected == "HOME":
    st.markdown("""
        <div style="padding: 30px 0px 10px 0px;">
            <h1 style="font-size: 45px; font-weight: 700; color: #1A1A1A !important; margin-bottom: 5px; letter-spacing: -1px;">SALES & MARKETING INTERNAL HUB</h1>
            <p style="font-size: 18px; color: #777777 !important; max-width: 900px;">
                Portal manajemen data strategis PT Silkar National. Monitoring harga pasar dan database kemitraan secara real-time.
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📊 System Overview")
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(label="Total Material Item", value="1,428", delta="↑ 12 New")
    with m2:
        st.metric(label="Verified Suppliers", value="512", delta="✓ Active")
    with m3:
        st.metric(label="Regional Coverage", value="34", delta="Provinces")
    with m4:
        st.metric(label="Last Data Sync", value="09:00", delta="WIB Today")

    st.markdown("<br>", unsafe_allow_html=True)
    gedung = load_local_image("gedung.jpg")
    if gedung: st.image(gedung, use_container_width=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    c1, c2 = st.columns(2, gap="large")
    with c1:
        st.markdown('<div class="card-box"><h2 style="font-weight: 800; margin-bottom: 10px;">DATABASE HARGA</h2><p style="font-size: 14px; color: #888888 !important; margin-bottom: 20px;">Akses katalog harga satuan material konstruksi terbaru.</p></div>', unsafe_allow_html=True)
        if st.button("TELUSURI HARGA MATERIAL", key="go_harga"):
            st.session_state.menu_index = 1
            st.rerun()
    with c2:
        st.markdown('<div class="card-box"><h2 style="font-weight: 800; margin-bottom: 10px;">DATABASE SUPPLIER</h2><p style="font-size: 14px; color: #888888 !important; margin-bottom: 20px;">Informasi lengkap kontak vendor dan rekanan terverifikasi.</p></div>', unsafe_allow_html=True)
        if st.button("TELUSURI DATA SUPPLIER", key="go_supp"):
            st.session_state.menu_index = 2
            st.rerun()

# --- 9. HALAMAN DATABASE HARGA ---
elif selected == "DATABASE HARGA":
    st.markdown(f"<h2 style='margin-top: 25px; font-weight: 800;'>{selected}</h2>", unsafe_allow_html=True)
    col_sel1, col_sel2 = st.columns([1, 2])
    with col_sel1:
        group = st.selectbox("KELOMPOK MATERIAL:", ["SIPIL & ARSITEKTUR", "MEP & INTERIOR"])
    
    kat_list = ["MATERIAL ALAM", "MATERIAL STRUKTUR", "MATERIAL ARSITEKTUR"] if group == "SIPIL & ARSITEKTUR" else ["MECHANICAL", "ELECTRICAL", "PLUMBING", "HVAC", "INTERIOR"]
    
    with col_sel2:
        kategori = st.radio("KATEGORI:", kat_list, horizontal=True)

    st.markdown("---")
    tab_name = "HARGA_" + kategori.replace(" ", "_")
    with st.spinner("Memuat data..."):
        df = load_data(tab_name)
    
    if df is not None:
        search = st.text_input(f"🔍 Cari di {kategori}:", placeholder="Masukkan kata kunci...")
        if search:
            df = df[df.apply(lambda r: r.astype(str).str.contains(search, case=False).any(), axis=1)]
        
        col_config = {col: st.column_config.NumberColumn(col, format="Rp %,.0f") for col in df.columns if any(x in col.upper() for x in ['HARGA', 'PRICE', 'NOMINAL'])}
        st.dataframe(df, use_container_width=True, hide_index=True, column_config=col_config)
    else:
        st.error(f"Tab '{tab_name}' tidak ditemukan di Google Sheets.")

# --- 10. HALAMAN DATABASE SUPPLIER ---
elif selected == "DATABASE SUPPLIER":
    st.markdown(f"<h2 style='margin-top: 25px; font-weight: 800;'>{selected}</h2>", unsafe_allow_html=True)

    if 'main_cat' not in st.session_state: st.session_state.main_cat = None
    if 'sub_cat' not in st.session_state: st.session_state.sub_cat = None

    if st.session_state.main_cat is None:
        st.markdown("<br><h3 style='text-align: center;'>Silakan pilih kategori utama:</h3><br>", unsafe_allow_html=True)
        col_left, c1, c2, col_right = st.columns([1, 2, 2, 1])
        if c1.button("MEP", use_container_width=True):
            st.session_state.main_cat = "MEP"
            st.rerun()
        if c2.button("SIPIL", use_container_width=True):
            st.session_state.main_cat = "SIPIL"
            st.rerun()
    else:
        if st.button("⬅ KEMBALI"):
            st.session_state.main_cat = None
            st.session_state.sub_cat = None
            st.rerun()
            
        st.markdown(f"<h3 style='text-align: center;'>Kategori: {st.session_state.main_cat}</h3>", unsafe_allow_html=True)
        subs = ["ELECTRICAL", "MECHANICAL", "PLUMBING", "HVAC"] if st.session_state.main_cat == "MEP" else ["MATERIAL ALAM", "STRUKTUR", "ARSITEKTUR", "INFRASTRUKTUR"]
        
        cols = st.columns(len(subs))
        for i, sub in enumerate(subs):
            if cols[i].button(sub, use_container_width=True):
                st.session_state.sub_cat = sub

        if st.session_state.sub_cat:
            st.markdown("---")
            search_query = st.text_input(f"🔍 Cari Spesifik di {st.session_state.sub_cat}:", placeholder="Ketik nama PT atau produk...")
            
            with st.spinner(f"Menarik data {st.session_state.sub_cat}..."):
                df_supp = load_data("SUPPLIER_MEP")
            
            if df_supp is not None:
                df_supp.columns = df_supp.columns.str.strip().str.upper()
                if 'SCOPE' in df_supp.columns:
                    df_display = df_supp[df_supp['SCOPE'].astype(str).str.contains(st.session_state.sub_cat, case=False, na=False)]
                    if search_query:
                        df_display = df_display[df_display.apply(lambda r: r.astype(str).str.contains(search_query, case=False).any(), axis=1)]
                    
                    st.write(f"Menampilkan **{len(df_display)}** data supplier untuk **{st.session_state.sub_cat}**")
                    st.caption("💡 Tips: Klik sel di tabel, lalu tekan Ctrl+C untuk menyalin data.")
                    # Menggunakan data_editor agar lebih mudah di-copy
                    st.data_editor(df_display, use_container_width=True, hide_index=True, disabled=True)
                else:
                    st.error("Kolom 'SCOPE' tidak ditemukan di database.")

# --- 11. FOOTER ---
st.markdown("""
    <div style="margin-top: 100px; padding: 30px; border-top: 1px solid #EEEEEE; text-align: center;">
        <p style="font-size: 14px; color: #AAAAAA; letter-spacing: 1px;">
            © 2026 SILKAR NATIONAL All Rights Reserved<br>
            Internal Application for Sales & Marketing Department
        </p>
    </div>
""", unsafe_allow_html=True)