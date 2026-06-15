import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Plotting Demo")

st.title('Analytics')

new_df = pd.read_csv('dataset/data_viz1.csv')
feature_text = pickle.load(open('dataset/feature_text.pkl','rb'))


group_df = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()

st.header('Sector Price per Sqft Geomap')
fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=700,hover_name=group_df.index)

st.plotly_chart(fig,use_container_width=True)

st.header('Features Wordcloud')

wordcloud_df = pd.read_pickle('df.pkl')
sector_wc_options = wordcloud_df['sector'].unique().tolist()
sector_wc_options.insert(0,'Overall')

selected_sector_wc = st.selectbox('Select Sector for Wordcloud', sector_wc_options)

if selected_sector_wc == 'Overall':
    text_to_plot = feature_text
else:
    s_df = wordcloud_df[wordcloud_df['sector'] == selected_sector_wc]
    text_list = []
    # Concatenate available categorical columns to form the text
    for col in ['property_type', 'furnishing_type', 'luxury_category', 'floor_category', 'agePossession']:
        if col in s_df.columns:
            text_list.extend(s_df[col].astype(str).tolist())
    text_to_plot = " ".join(text_list)

wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='black',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(text_to_plot)

fig, ax = plt.subplots(figsize = (8, 8), facecolor = None)
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad = 0)
st.pyplot(fig)

st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom",
                      title="Area Vs Price")

    st.plotly_chart(fig1, use_container_width=True)

st.header('Top 10 Sectors & BHK Pie Chart')

col1, col2 = st.columns(2)

with col1:
    st.subheader('Top 10 Sectors by Price per Sqft')
    # Group by sector and calculate mean price_per_sqft
    top_sectors = new_df.groupby('sector')['price_per_sqft'].mean().sort_values(ascending=False).head(10).reset_index()
    fig_bar = px.bar(top_sectors, x='price_per_sqft', y='sector', orientation='h', title='Top 10 Sectors by Price/Sqft')
    st.plotly_chart(fig_bar, use_container_width=True)

with col2:
    st.subheader('BHK Pie Chart')
    sector_options = new_df['sector'].unique().tolist()
    sector_options.insert(0,'overall')

    selected_sector = st.selectbox('Select Sector', sector_options)

    if selected_sector == 'overall':
        fig2 = px.pie(new_df, names='bedRoom')
        st.plotly_chart(fig2, use_container_width=True)
    else:
        fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
        st.plotly_chart(fig2, use_container_width=True)

st.header('Side by Side BHK price comparison')

fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')

st.plotly_chart(fig3, use_container_width=True)


st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)

st.header('Property Distribution Hierarchy')
st.info('Click on the segments to drill down into specific sectors and categories.')
fig_sun = px.sunburst(new_df, path=['sector', 'property_type', 'furnishing_type'], values='price',
                  color='price', color_continuous_scale='RdBu')
st.plotly_chart(fig_sun, use_container_width=True)

st.header('Feature Relationship Heatmap')
# Select only numeric columns for correlation
numeric_df = new_df.select_dtypes(include=['float64', 'int64'])
corr_matrix = numeric_df.corr()

fig_corr, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
st.pyplot(fig_corr)