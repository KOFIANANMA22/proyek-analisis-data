import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#import all_data
all_df = pd.read_csv("all_data.csv")
#import data mean_review_df
mean_review_df = all_df.groupby(by='product_category_name').review_score.mean().sort_values(ascending=False).reset_index()
#import data sum_freight_value_df
sum_freight_value_df = all_df.groupby(by='customer_city').freight_value.sum().sort_values(ascending=False).reset_index()
sum_freight_value_df.rename(columns={
    'freight_value' : 'quantity' #mengubah nama column 'freight_value' menjadi 'quantity'
},inplace=True) 

st.header('E-Commerce Public Dashboard :sparkles:') #membuat judul nama toko

st.subheader("Rata-Rata Review Berdasarkan Product Category") #membuat judul utama visualisasi 1
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(40, 30)) #membuat figura dengan 2 column, 1 baris
colors = ["#00A9FF", "#00A9FF", "#00A9FF", "#00A9FF", "#00A9FF"] #setting warna bar
#membuat barplot ke-1 menggunakan seaborn
sns.barplot(x="review_score", y="product_category_name", data=mean_review_df.head(5), hue=colors, ax=ax[0])
ax[0].set_ylabel(None) #menghilangkan label y
ax[0].set_xlabel(None) #menghilangkan label x
ax[0].set_title("Review Terbaik", loc="center", fontsize=50) #membuat sub judul
ax[0].tick_params(labelsize=40) #setting ukuran label

#membuat barplot ke-2 menggunakan seaborn
sns.barplot(x="review_score", y="product_category_name", data=mean_review_df.sort_values(by="review_score", ascending=True).head(5), hue=colors, ax=ax[1])
ax[1].set_ylabel(None) #menghilangkan label y
ax[1].set_xlabel(None) #menghilangkan label x
ax[1].invert_xaxis() #membalik barplot
ax[1].yaxis.set_label_position("right") #setting posisi label
ax[1].yaxis.tick_right() #setting posisi bar plot
ax[1].set_title("Review Terburuk", loc="center", fontsize=50) #membuat sub judul
ax[1].tick_params( labelsize=40) #setting ukuran label
st.pyplot(fig) #menampilkan


st.subheader("Data Penjualan Berdasarkan Kota") #membuat judul utama visualisasi 2
fig2 =plt.figure(figsize=(10, 5)) #membuat canvas dengan ukuran 10,5
colors = ["#89CFF3", "#89CFF3", "#89CFF3", "#89CFF3","#89CFF3"] #setting warna
sns.barplot(
    y="quantity", 
    x="customer_city",
    data=sum_freight_value_df.sort_values(by="quantity", ascending=False).head(5),
    hue=colors
) #membuat barplot megunakan seaborn
plt.title("Tingkat Penjualan berdasarkan Kota", loc="center", fontsize=15) #membuat judul
plt.ylabel(None) #menghilangkan label y
plt.xlabel(None) #menghilangkan label x
plt.tick_params(axis='x', labelsize=12) #setting ukuran x

st.pyplot(fig2) #menampilkan 