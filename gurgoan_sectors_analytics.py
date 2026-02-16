

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/content/Gurgoan_Wrangled_Data_2.csv")

latlong=pd.read_csv("/content/latlong.csv")

latlong.head()

latlong['latitude'] = latlong['coordinates'].str.split(',').str.get(0).str.split('°').str.get(0).astype('float')
latlong['longitude'] = latlong['coordinates'].str.split(',').str.get(1).str.split('°').str.get(0).astype('float')

latlong.head()

latlong=latlong.drop('coordinates',axis=1)

latlong

latlong.shape

latlong.loc[130]=['badshahpur',77.0466318,28.3933996]

latlong.loc[130]

new_df=pd.merge(df,latlong,on='sector')

new_df.head()

new_df=new_df.drop('possession',axis=1)

group_df=new_df.groupby('sector').mean()[['price','area','price_per_sqft','longitude','latitude']]

group_df

import plotly.express as px
import plotly.graph_objects as go

fig = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size="area",
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                        mapbox_style="open-street-map", text=group_df.index)
fig.show()



from google.colab import files
group_df.to_csv("Gurgoan_Sectors_latlong.csv",index=False)
files.download("Gurgoan_Sectors_latlong.csv")

new_df.to_csv("data_viz1.csv",index=False)
files.download("data_viz1.csv")

"""## Word cloud"""

#df1=pd.read_csv("/content/residential-land - residential-land.csv")

#df1.head()

#df1.isnull().sum()

df1['features']

#df1['features']=df1['features'].replace('',np.nan)
#df1['features']=df1['features'].fillna('["Not Available"]')

#df1['features'].isnull().sum()

#df1['features']=df1['features'].apply(lambda x:' '.join(x)  )

#df1['features']

#df1['features'][2152]

#wordcloud_df=df1.merge(df,left_index=True,right_index=True)[['features','sector']]
#wordcloud_df.head()

#wordcloud_df.head()

#wordcloud_df.dtypes

#wordcloud_df['features']=wordcloud_df['features'].replace(' ',np.nan)

#index=wordcloud_df[wordcloud_df['features'].isna()].index


#print(index)



#wordcloud_df=wordcloud_df.drop(index=index)
#wordcloud_df=wordcloud_df.reset_index(drop=True)

#wordcloud_df.isnull().sum()

#import ast
#main=[]
#for item in wordcloud_df['features'].apply(ast.literal_eval):
#  main.extend(item)

#main

#from wordcloud import WordCloud

#main

#feature_text = ' '.join(main[0])

#feature_text=main

#feature_text

"""plt.rcParams["font.family"] = "Arial"

wordcloud = WordCloud(width = 800, height = 800,
                      background_color = 'white',
                      stopwords = set(['s']),
                      min_font_size = 10).generate(feature_text)

plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()

import pickle
pickle.dump(feature_text,open('feature_text.pkl','wb'))

files.download("feature_text.pkl")
"""