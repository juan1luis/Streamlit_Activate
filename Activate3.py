
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


dset_rute = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
data_WalM = pd.read_csv(dset_rute)
data_vis = data_WalM.copy()

apptitle = 'Graficas WalMart USA'
descrip = 'Aqui se mostraran los datos de manera grafica sobre WalMart USA.'

st.title(apptitle)
st.header(descrip)
st.markdown('___')

st.header('Histograma')
fig, ax = plt.subplots()
ax.hist(data_WalM.Region)
st.pyplot(fig)
st.markdown('___')




df = data_WalM[['Category','Profit']]
data_prof =dict(df.groupby(['Category'])['Profit'].sum())

st.header('Grafica de pie')
fig3, ax3 = plt.subplots()
ax3.pie(data_prof.values(),labels=data_prof.keys())
ax3.legend(title = "Categorías:")
ax3.set_title('Ganancia por categoría')
st.pyplot(fig3)
st.markdown('___')

st.header('Grafica de barras')
fig2, ax2 = plt.subplots()
y_p = data_WalM['Sub-Category']
x_p = data_WalM['Sales']
ax2.barh(y_p, x_p)
ax2.set_ylabel("Ship Mode")
ax2.set_xlabel("Sales")
ax2.set_title('Ventas por subcategoría')
st.pyplot(fig2)
st.markdown('___')

st.write('Juan Luis Saenz A01562193')