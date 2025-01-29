import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('DifferentRoyters.csv')

try:
   #counting brands
   tplink = df[df['Brand'] == 'TPLINK']['Brand'].count()
   dlink = df[df['Brand'] == 'DLINK']['Brand'].count()
   mercusys = df[df['Brand'] == 'Mercusys ']['Brand'].count()
   tenda = df[df['Brand'] == 'TENDA']['Brand'].count()
   prolink = df[df['Brand'] == 'PROLINK']['Brand'].count()
   linksys = df[df['Brand'] == 'LINKSYS']['Brand'].count()
   planet = df[df['Brand'] == 'Planet']['Brand'].count()
   cudy = df[df['Brand'] == 'Cudy']['Brand'].count()
   asus = df[df['Brand'] == 'ASUS']['Brand'].count()
   google = df[df['Brand'] == 'Google']['Brand'].count()
   
   #changing price column to float 
   df['Price'] = df['Price'].str.replace('$', '')
   df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
   
   #routers avg prices
   a_tplink = df[df['Brand'] == 'TPLINK']['Price'].mean()
   a_dlink = df[df['Brand'] == 'DLINK']['Price'].mean()
   a_mercusys = df[df['Brand'] == 'Mercusys ']['Price'].mean()
   a_tenda = df[df['Brand'] == 'TENDA']['Price'].mean()
   a_prolink = df[df['Brand'] == 'PROLINK']['Price'].mean()
   a_linksys = df[df['Brand'] == 'LINKSYS']['Price'].mean()
   a_planet = df[df['Brand'] == 'Planet']['Price'].mean()
   a_cudy = df[df['Brand'] == 'Cudy']['Price'].mean()
   a_asus = df[df['Brand'] == 'ASUS']['Price'].mean()
   a_google = df[df['Brand'] == 'Google']['Price'].mean()
   
   #setting sub data frames
   graph1 = {'x_axis': ['TPLINK' ,'DLINK', 'Mercusys ', 'TENDA', 'PROLINK', 'LINKSYS', 'Planet', 'Cudy', 'ASUS', 'Google'],
            'y1': [tplink, dlink, mercusys, tenda, prolink, linksys, planet, cudy, asus, google]}
   df1 = pd.DataFrame(graph1)
   
   graph2 = {'x_axis': ['TPLINK' ,'DLINK', 'Mercusys ', 'TENDA', 'PROLINK', 'LINKSYS', 'Planet', 'Cudy', 'ASUS', 'Google'],
            'y2': [a_tplink, a_dlink, a_mercusys, a_tenda, a_prolink, a_linksys, a_planet, a_cudy, a_asus, a_google]}
   df2 = pd.DataFrame(graph2)
   
   #ploting graphs
   fig, (ax1, ax2)= plt.subplots(1,2)
   
   df1.plot(kind='bar', ax=ax1, x='x_axis', y='y1', title='nb of routers')
   df2.plot(kind='bar', ax=ax2, x='x_axis', y='y2', title="routers mean price")
   
   plt.tight_layout()
   plt.show()
   
except Exception as e:
    print(f'error: {e}')