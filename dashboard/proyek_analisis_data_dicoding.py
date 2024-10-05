import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Proyek analisis data dicoding menggunakan dataset air quality")
st.subheader("Pertanyaan bisnis:")
st.markdown("""
- Bagaimana hubungan antara suhu udara dengan konsentrasi ozon?
- Bagaimana temperatur mempengaruhi polutan
- Bagaimana musim mempengaruhi polutan?
""")

df = pd.read_csv("dashboard/filtered_data.csv")
st.write(df.head())

st.subheader("Pertanyaan 1")
fig, ax = plt.subplots()
sns.scatterplot(x=df['TEMP'], y=df['O3'], ax=ax)
ax.set_title("Hubungan antara temperatur dan Konsentrasi Ozon")
st.pyplot(fig)
st.subheader("Penjelasan")
st.markdown("""
            Bedasarkan data tersebut diketahui bahwa setiap kali temperatur naik maka konsentrasi ozon juga naik, hal ini disebabkan oleh: 
            - Pembentukan ozon di troposfer (lapisan atmosfer terendah) terjadi karena reaksi kimia antara nitrogen oksida (NOx), senyawa organik yang mudah menguap (VOC), dan sinar matahari. Sumber utama NOx dan VOC adalah emisi kendaraan, aktivitas industri, serta sumber alami seperti tumbuhan.
            - Suhu tinggi mempercepat reaksi kimia yang menghasilkan ozon. Cahaya matahari yang lebih intens pada hari-hari panas meningkatkan reaksi fotokimia, yang menyebabkan lebih banyak ozon terbentuk di dekat permukaan bumi.
            - Udara yang stagnan selama gelombang panas juga memerangkap polutan di satu tempat, sehingga mencegah penyebaran polutan tersebut dan menyebabkan konsentrasi ozon meningkat.
            """)

st.subheader("Pertanyaan 2")
fig, ax = plt.subplots()
sns.scatterplot(x=df['TEMP'], y=df['PM2.5'], ax=ax)
ax.set_title("Hubungan antara PM2.5 dan temperatur")
st.pyplot(fig)

fig, ax = plt.subplots()
sns.scatterplot(x=df['TEMP'], y=df['PM10'], ax=ax)
ax.set_title("Hubungan antara PM10 dan temperatur")
st.pyplot(fig)
st.subheader("Penjelasan")
st.markdown("""
            Dari grafik di atas disimpulkan bahwa tiap kali temperature menurun maka polutan akan naik, meskipun ada limitasi di temperatur tertentu, hal ini disebabkan oleh:
            - Inversi suhu terjadi ketika lapisan udara di permukaan bumi menjadi lebih dingin daripada lapisan udara di atasnya. Pada kondisi normal, udara panas di permukaan akan naik dan membawa polutan bersamanya, sehingga terjadi penyebaran polutan ke atmosfer yang lebih tinggi.
            - Di banyak daerah, saat suhu menurun (terutama pada musim dingin atau malam hari), orang cenderung menggunakan alat pemanas seperti pemanas ruangan atau pembakaran kayu, batu bara, dan bahan bakar fosil lainnya. Pembakaran ini menghasilkan polutan seperti PM2.5 dan PM10.
            - Udara dingin cenderung lebih stabil dan kurang bergerak dibandingkan udara panas. Saat suhu turun, angin yang bertugas menyebarkan polutan berkurang kecepatannya. Ini membuat polutan tidak tersebar luas dan terakumulasi di satu area. Polusi udara meningkat karena proses ini, terutama di area perkotaan.
            """)

st.subheader("Pertanyaan 3")
agg_df = df.groupby(["year", "season"])[["PM2.5", "PM10"]].median().reset_index()

melted_df = agg_df.melt(id_vars=['year', 'season'], value_vars=['PM2.5', 'PM10'],
                        var_name='Measurement', value_name='Value')

fig, ax = plt.subplots(figsize=(14, 8))
bar_plot = sns.barplot(data=melted_df, x='season', y='Value', hue='Measurement', ci=None, ax=ax)
ax.set_title('Seasonal Mean PM2.5 and PM10 Measurements')
ax.set_xlabel('Season')
ax.set_ylabel('Median Value')
ax.legend(title='Measurement')

for p in bar_plot.patches:
    bar_plot.annotate(format(p.get_height(), '.2f'),
                      (p.get_x() + p.get_width() / 2., p.get_height()),
                      ha='center', va='center',
                      xytext=(0, 9),
                      textcoords='offset points')

st.pyplot(fig)
st.markdown("""
            Spring (Musim Semi):
            - Selama musim semi, banyak pohon dan tanaman mulai berbunga, yang menyebabkan peningkatan signifikan dalam polusi serbuk sari (pollen). Meskipun serbuk sari bukan polutan kimia, dalam konteks kesehatan pernapasan, ini bisa dianggap sebagai polusi, terutama bagi penderita alergi.
            - Selain itu, di beberapa daerah, aktivitas pertanian seperti membajak tanah atau pembakaran sisa tanaman dapat menambah polusi partikulat (PM).
            """)
 
st.markdown("""
            Winter (Musim Dingin):
            - Pembakaran bahan bakar untuk pemanasan dan fenomena inversi suhu membuat polutan terperangkap di permukaan tanah. Polusi partikel halus (PM2.5) dan karbon monoksida biasanya lebih tinggi di musim dingin.
            """)

st.markdown("""
            Fall (Musim Gugur):
            - Di musim gugur, aktivitas seperti pembakaran daun kering dan sampah organik bisa menyebabkan peningkatan partikel debu di udara, meskipun umumnya lebih rendah dibanding musim dingin
            """)
st.markdown("""
            Summer (Musim Panas):
            - Meskipun ozon permukaan tanah cenderung meningkat di musim panas, angin yang lebih kuat dan suhu yang bervariasi bisa membantu mendispersikan polutan. Namun, di beberapa daerah, stagnasi udara juga bisa menyebabkan penumpukan ozon dan partikel lainnya.
            """)