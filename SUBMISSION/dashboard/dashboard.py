import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "day.csv")

day_df = pd.read_csv(DATA_PATH)
day_df["dteday"] = pd.to_datetime(day_df["dteday"])

# =========================
# MAPPING KATEGORI
# =========================
day_df["season"] = day_df["season"].map({
    1: "Spring",
    2: "Summer",
    3: "Fall",
    4: "Winter"
})

day_df["workingday"] = day_df["workingday"].map({
    0: "Weekend/Holiday",
    1: "Working Day"
})

# =========================
# SIDEBAR FILTER
# =========================
st.sidebar.header("Filter Data")

season_filter = st.sidebar.multiselect(
    "Pilih Musim",
    options=day_df["season"].unique(),
    default=day_df["season"].unique()
)

workingday_filter = st.sidebar.multiselect(
    "Pilih Jenis Hari",
    options=day_df["workingday"].unique(),
    default=day_df["workingday"].unique()
)

# 🔥 INI YANG TADI HILANG
filtered_df = day_df[
    (day_df["season"].isin(season_filter)) &
    (day_df["workingday"].isin(workingday_filter))
]

# =========================
# TITLE & KPI
# =========================
st.title("🚲 Dashboard Analisis Bike Sharing")

col1, col2 = st.columns(2)

total_rentals = int(filtered_df["cnt"].sum())
avg_rentals = int(filtered_df["cnt"].mean())

col1.metric("Total Peminjaman", f"{total_rentals:,}")
col2.metric("Rata-rata Peminjaman Harian", f"{avg_rentals:,}")

# =========================
# VISUALISASI INTERAKTIF
# =========================
col3, col4 = st.columns(2)

# =========================
# 1️⃣ MUSIM
# =========================
with col3:
    st.subheader("Rata-rata Peminjaman Berdasarkan Musim")

    season_avg = (
        filtered_df.groupby("season")["cnt"]
        .mean()
        .reset_index()
        .sort_values("cnt", ascending=False)
    )

    fig_season = px.bar(
        season_avg,
        x="season",
        y="cnt",
        color="season",
        text="cnt",
        title="Perbandingan Musim"
    )

    fig_season.update_traces(texttemplate="%{text:.0f}", textposition="outside")
    fig_season.update_layout(showlegend=False)

    st.plotly_chart(fig_season, use_container_width=True)

    if not season_avg.empty:
        top_season = season_avg.iloc[0]["season"]
        st.caption(f"📌 Insight: Musim dengan rata-rata tertinggi adalah **{top_season}**.")

# =========================
# 2️⃣ WORKING DAY
# =========================
with col4:
    st.subheader("Rata-rata Peminjaman: Hari Kerja vs Akhir Pekan")

    workingday_avg = (
        filtered_df.groupby("workingday")["cnt"]
        .mean()
        .reset_index()
        .sort_values("cnt", ascending=False)
    )

    fig_work = px.bar(
        workingday_avg,
        x="workingday",
        y="cnt",
        color="workingday",
        text="cnt",
        title="Perbandingan Jenis Hari"
    )

    fig_work.update_traces(texttemplate="%{text:.0f}", textposition="outside")
    fig_work.update_layout(showlegend=False)

    st.plotly_chart(fig_work, use_container_width=True)

    if not workingday_avg.empty:
        top_day = workingday_avg.iloc[0]["workingday"]
        st.caption(f"📌 Insight: Peminjaman lebih tinggi pada **{top_day}**.")

# =========================
# 3️⃣ TREND WAKTU
# =========================
st.subheader("Trend Peminjaman dari Waktu ke Waktu")

time_series = (
    filtered_df.groupby("dteday")["cnt"]
    .sum()
    .reset_index()
)

fig_time = px.line(
    time_series,
    x="dteday",
    y="cnt",
    title="Trend Total Peminjaman Harian"
)

st.plotly_chart(fig_time, use_container_width=True)

st.caption("📌 Insight: Terlihat pola musiman dan fluktuasi sepanjang periode observasi.")