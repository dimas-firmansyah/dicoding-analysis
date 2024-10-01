import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

from os import path

script_dir = path.dirname(path.realpath(__file__))

st.title("Proyek Analisis Data: Bike Sharing Dataset")

###

st.header("Bagaimana petumbuhan transaksi pada tahun 2012 dibandingkan 2011?")

sum_per_year_df = pd.read_csv(f"{script_dir}/sum_per_year.csv")
sum_per_year_df.set_index("datetime", inplace=True)

fig, ax = plt.subplots()
sum_per_year_df[["casual", "registered"]].plot.bar(ax=ax)
plt.ticklabel_format(axis="y", style="plain")
plt.legend(["Casual", "Registered"])
plt.xticks(rotation=0)
plt.xlabel(None)
st.pyplot(fig)

st.markdown("""
Dari grafik diatas dapat dilihat bahwa terdapat pertumbuhan transaksi pada tahun 2012 dari tahun 2011.
""")

###

st.header("Bagaimana jumlah bulanan transaksi rental sepeda?")

sum_per_month_df = pd.read_csv(f"{script_dir}/sum_per_month.csv")
sum_per_month_df["datetime"] = pd.to_datetime(sum_per_month_df["datetime"])
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(
    sum_per_month_df["datetime"],
    sum_per_month_df["casual"],
    label="Casual",
    marker="o",
)
ax.plot(
    sum_per_month_df["datetime"],
    sum_per_month_df["registered"],
    label="Registered",
    marker="o",
)
ax.legend()
st.pyplot(fig)

st.markdown("""
Dari grafik diatas dapat dilihat bahwa transaksi paling tinggi ada disekitar bulan Juli-Oktober
dengan penurunan transaksi di sekitar bulan Januari.
""")

###

st.header("Bulan apa transaksi paling sering terjadi?")

avg_by_month_df = pd.read_csv(f"{script_dir}/avg_by_month.csv")
avg_by_month_df.set_index("month", inplace=True)

max_val = avg_by_month_df["cnt"].max()
colors = avg_by_month_df["cnt"].apply(
    lambda x: "#3A75B1" if x == max_val else "#D3D3D3"
)

fig, ax = plt.subplots()
avg_by_month_df["cnt"].plot.barh(color=colors, ax=ax)
ax.set_title("Avg. monthly transaction by month")
ax.set_ylabel(None)
st.pyplot(fig)

st.markdown("""
Dari grafik diatas dapat dilihat bahwa transaksi paling sering dilakukan pada bulan Agustus.
""")

###

st.header("Pertanyaan 4: Hari apa transaksi paling sering terjadi?")

avg_by_day_df = pd.read_csv(f"{script_dir}/avg_by_day.csv")
avg_by_day_df.set_index("day", inplace=True)

max_val = avg_by_day_df["cnt"].max()
colors = avg_by_day_df["cnt"].apply(lambda x: "#3A75B1" if x == max_val else "#D3D3D3")

fig, ax = plt.subplots()
avg_by_day_df["cnt"].plot.barh(color=colors, ax=ax)
ax.set_title("Avg. daily transaction by day of week")
ax.set_ylabel(None)
st.pyplot(fig)

st.markdown("""
Dari grafik diatas dapat dilihat bahwa transaksi paling sering dilakukan pada hari Jumat,
namun perbedaan dari hari lain hanya seberapa.
""")

###

st.header("Jam berapa transaksi paling sering terjadi?")

avg_by_hour_df = pd.read_csv(f"{script_dir}/avg_by_hour.csv")
avg_by_hour_df["hr"] = avg_by_hour_df["hr"].astype(str).str.pad(2, "left", "0")
avg_by_hour_df.set_index("hr", inplace=True)

max_val = avg_by_hour_df["cnt"].nlargest(3).values
colors = avg_by_hour_df["cnt"].apply(lambda x: "#3A75B1" if x in max_val else "#D3D3D3")

fig, ax = plt.subplots()
avg_by_hour_df["cnt"].plot.barh(color=colors, ax=ax)
ax.set_title("Avg. hourly transaction by hour")
ax.set_ylabel(None)
st.pyplot(fig)

st.markdown("""
Dari grafik diatas dapat dilihat bahwa transaksi paling sering dilakukan pada pukul 17, diikuti dengan pukul 18 dan 08.
Ini selaras dengan jam dimana orang-orang berangkat dan pulang melaksanakan aktifitas (sekolah, bekerja).
""")

###

st.markdown("""
## Kesimpulan
- Jumlah transaksi rental sepeda mengalami penaikan pada tahun 2012 dibanding tahun 2011.
- Secara keseluruhan, jumlah transaksi per bulan mengalami penaikan, namun terjadi penurunan di sekitar bulan Januari.
- Transaksi paling sering terjadi di bulan Agustus.
- Transaksi paling sering terjadi di hari Jumat, namun hanya selisih kecil dari hari lainnya.
- Transaksi paling sering terjadi di pukul 17, 18, dan 08. Ini selaras dengan jam orang-orang berangkat dan pulang melaksanakan aktifitas (sekolah, bekerja).
""")

st.caption("""
---
Dimas Firmansyah
[deirn.bai.lol](https://deirn.bai.lol)
""")
