
import streamlit as st
import pandas as pd


dset_rute = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
data_WalM = pd.read_csv(dset_rute)
data_vis = data_WalM.copy()

def showDataset(data):
    return st.dataframe(data)

apptitle = 'Datos de WalMart USA'
descrip = 'Se podran visualizar los datos de Walmart de una forma mas dinamica'

sidebar = st.sidebar

st.title(apptitle)
st.header(descrip)
st.markdown('___')


sidebar.title('Controles')

Categ= sidebar.selectbox('Categoría:', data_WalM['Category'].unique())

sidebar.markdown('___')


s_mode= sidebar.radio('Ship Mode:',data_WalM['Ship Mode'].unique())
sidebar.markdown('___')
optionals = sidebar.expander('Optional config',True)
disc_val = optionals.slider(
    'Select the Fare:',
    min_value= float(data_WalM['Discount'].min()),
    max_value= float(data_WalM['Discount'].max())

)


data_vis = data_WalM[(data_WalM['Ship Mode']==s_mode)&
    (data_WalM['Category']==Categ)&
    (data_WalM['Discount']==disc_val)
    ]
sidebar.markdown('___')

sidebar.header('Checkbox')
if sidebar.checkbox('¿Mostrar DataFrame?'):
    showDataset(data_vis)

st.write('Juan Luis Saenz A01562193')