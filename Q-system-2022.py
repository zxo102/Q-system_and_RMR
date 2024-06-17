#作者：欧阳治华，2024年6月15日, zxo102@qq.com

import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# Read the CSV file
df1 = pd.read_csv('Q-system-2022/Q-curve1.csv')
x1 = df1['x']
y1 = df1['Curve1']

df2 = pd.read_csv('Q-system-2022/Q-curve2.csv')
x2 = df2['x']
y2 = df2['Curve2']

df3 = pd.read_csv('Q-system-2022/Q-curve3.csv')
x3 = df3['x']
y3 = df3['Curve3']

df4 = pd.read_csv('Q-system-2022/Q-curve4.csv')
x4 = df4['x']
y4 = df4['Curve4']

df5 = pd.read_csv('Q-system-2022/Q-curve5.csv')
x5 = df5['x']
y5 = df5['Curve5']

df6 = pd.read_csv('Q-system-2022/Q-curve6.csv')
x6 = df6['x']
y6 = df6['Curve6']

df7 = pd.read_csv('Q-system-2022/Q-curve7.csv')
x7 = df7['x']
y7 = df7['Curve7']

df8 = pd.read_csv('Q-system-2022/Q-curve8.csv')
x8 = df8['x']
y8 = df8['Curve8']

df9 = pd.read_csv('Q-system-2022/Q-curve9.csv')
x9 = df9['x']
y9 = df9['Curve9']

df10 = pd.read_csv('Q-system-2022/Q-curve10.csv')
x10 = df10['x']
y10 = df10['Curve10']

df11 = pd.read_csv('Q-system-2022/Q-curve11.csv')
x11 = df11['x']
y11 = df11['Curve11']

df12 = pd.read_csv('Q-system-2022/Q-curve12.csv')
x12 = df12['x']
y12 = df12['Curve12']

df13 = pd.read_csv('Q-system-2022/Q-curve13.csv')
x13 = df13['x']
y13 = df13['Curve13']

df14 = pd.read_csv('Q-system-2022/Q-curve14.csv')
x14 = df14['x']
y14 = df14['Curve14']

df15 = pd.read_csv('Q-system-2022/Q-curve15.csv')
x15 = df15['x']
y15 = df15['Curve15']

df16 = pd.read_csv('Q-system-2022/Q-curve16.csv')
x16 = df16['x']
y16 = df16['Curve16']

df51 = pd.read_csv('Q-system-2022/Q-curve51.csv')
x51 = df51['x']
y51 = df51['Curve51']
df61 = pd.read_csv('Q-system-2022/Q-curve61.csv')
x61 = df61['x']
y61 = df61['Curve61']
df71 = pd.read_csv('Q-system-2022/Q-curve71.csv')
x71 = df71['x']
y71 = df71['Curve71']
df81 = pd.read_csv('Q-system-2022/Q-curve81.csv')
x81 = df81['x']
y81 = df81['Curve81']
df31 = pd.read_csv('Q-system-2022/Q-curve31.csv')
x31 = df31['x']
y31 = df31['Curve31']

p9 = pd.read_csv('Q-system-2022/Q-polygon9.csv')
xp9 = p9['x']
yp9 = p9['Polygon9']
p8 = pd.read_csv('Q-system-2022/Q-polygon8.csv')
xp8 = p8['x']
yp8 = p8['Polygon8']
p7 = pd.read_csv('Q-system-2022/Q-polygon7.csv')
xp7 = p7['x']
yp7 = p7['Polygon7']
p6 = pd.read_csv('Q-system-2022/Q-polygon6.csv')
xp6 = p6['x']
yp6 = p6['Polygon6']
p5 = pd.read_csv('Q-system-2022/Q-polygon5.csv')
xp5 = p5['x']
yp5 = p5['Polygon5']
#p4 = pd.read_csv('Q-system-2022/Q-polygon4.csv')
#xp4 = p4['x']
#yp4 = p4['Polygon4']
#p3 = pd.read_csv('Q-system-2022/Q-polygon3.csv')
#xp3 = p3['x']
#yp3 = p3['Polygon3']
#p2 = pd.read_csv('Q-system-2022/Q-polygon2.csv')
#xp2 = p2['x']
#yp2 = p2['Polygon2']

p22 = pd.read_csv('Q-system-2022/Q-polygon22.csv')
xp22 = p22['x']
yp22 = p22['Polygon22']

p33 = pd.read_csv('Q-system-2022/Q-polygon33.csv')
xp33 = p33['x']
yp33 = p33['Polygon33']



# Set the width and height of the plot
width = 11  # Width in inches
height = 7  # Height in inches

# Create a figure and axis
fig, (ax_top,ax) = plt.subplots(2, 1, figsize=(width,height), sharex=True, gridspec_kw={'height_ratios':[1,6],'hspace':0})

yt1 = 1
yt2 = 1.5
yt3 = 2
yt4 = 3

ax.set_xlim(0.001, 1000)
ax.set_ylim(1, 100)
ax_top.set_ylim(yt1,yt4)

ax.plot(x1, y1, marker='None', linestyle='-',color='black')
ax.plot(x2, y2, marker='None', linestyle='-',color='black')
ax.plot(x3, y3, marker='None', linestyle='-',color='black')
ax.plot(x4, y4, marker='None', linestyle='-',color='black')
ax.plot(x5, y5, marker='None', linestyle='-',color='black')
ax.plot(x6, y6, marker='None', linestyle='-',color='black')
ax.plot(x7, y7, marker='None', linestyle='-',color='black')
ax.plot(x8, y8, marker='None', linestyle='-',color='black')
#ax.plot(x9, y9, marker='None', linestyle='-',color='black')
#ax.plot(x10, y10, marker='None', linestyle='-',color='black')
#ax.plot(x11, y11, marker='None', linestyle='-',color='black')
#ax.plot(x12, y12, marker='None', linestyle='-',color='black')
ax.plot(x13, y13, marker='None', linestyle='-',color='black')
ax.plot(x14, y14, marker='None', linestyle='-',color='black')
ax.plot(x15, y15, marker='None', linestyle='-',color='black')
ax.plot(x16, y16, marker='None', linestyle='-',color='black')
ax.plot(x51, y51, marker='None', linestyle='--',color='black')
ax.plot(x61, y61, marker='None', linestyle='--',color='black')
ax.plot(x71, y71, marker='None', linestyle='--',color='black')
ax.plot(x81, y81, marker='None', linestyle='--',color='black')
ax.plot(x31, y31, marker='None', linestyle='--',color='black')

# Set the scales to logarithmic
ax.set_xscale('log')
ax.set_yscale('log')
ax_top.set_xscale('log')
ax_top.set_yscale('log')

# Set the tick values and labels for the X axis
ax.set_xticks([0.001, 0.004, 0.01, 0.04, 0.1, 0.4,1,4,10,40,100,400,1000])
ax.set_xticklabels(['0.001', '0.004', '0.01', '0.04', '0.1', '0.4','1','4','10','40','100','400','1000'])

# Set the tick values and labels for the Y axis
ax.set_yticks([1, 2, 5, 10, 20, 50,100])
ax.set_yticklabels(['1', '2', '5', '10', '20', '50','100'])

#Set the ticks to point inwards
plt.tick_params(axis='both', which='both',direction='in',bottom=True, top=True, left=True, right=True, labelleft=True, labelbottom=True, labeltop=False, labelright=True)

# Hide the bottom subplot's ticks and labels
ax_top.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=False)

# Create a second y-axis on the right side
# Set tick positions and labels for the right y-axis
ax2 = ax.twinx()
ax2.set_yscale('log')
ax2.set_ylim(1, 100)
ax2.set_yticks([2, 5, 10, 20,30, 50,100])
ax2.set_yticklabels(['1.5', '2.4', '3', '5','7', '11', '20'])

# Add grid for major ticks
ax.grid(which='both', linestyle='-', linewidth='0.5', color='gray')

# Add labels and title
ax.set_xlabel(r'岩体质量$Q=\frac{RQD}{J_n}\times \frac{J_r}{J_a} \times \frac{J_w}{SRF}$',fontproperties='SimHei', fontsize=12)
ax.set_ylabel('跨度或高度(米)/ESR', fontproperties='SimHei',fontsize=12)
ax2.set_ylabel('锚杆长度(米) ESR=1', fontproperties='SimHei',fontsize=12)


plt.fill(xp9, yp9, color='orange', alpha=0.7)
plt.fill(xp8, yp8, color='orange', alpha=0.6)
plt.fill(xp7, yp7, color='orange', alpha=0.5)
plt.fill(xp6, yp6, color='orange', alpha=0.4)
plt.fill(xp5, yp5, color='orange', alpha=0.3)
plt.fill(xp33, yp33, color='orange', alpha=0.2)
plt.fill(xp22, yp22, color='orange', alpha=0.1)
#plt.fill(xp4, yp4, color='grey', alpha=0.4)
#plt.fill(xp3, yp3, color='grey', alpha=0.3)
#plt.fill(xp2, yp2, color='grey', alpha=0.2)

ax.text(0.0037,40,"9",fontsize=13, bbox={"boxstyle" : "circle", "color":"red"})
ax.text(0.025,17,"8",fontsize=13, bbox={"boxstyle" : "circle", "color":"red"})
ax.text(0.14,17,"7",fontsize=13, bbox={"boxstyle" : "circle", "color":"red"})
ax.text(0.42,17,"6",fontsize=13, bbox={"boxstyle" : "circle", "color":"red"})
ax.text(1.35,17,"5",fontsize=13, bbox={"boxstyle" : "circle", "color":"red"})
ax.text(4,17,"4",fontsize=13, bbox={"boxstyle" : "circle", "color":"red"})
ax.text(22,17,"3",fontsize=13, bbox={"boxstyle" : "circle", "color":"red"})
ax.text(98,17,"2",fontsize=13, bbox={"boxstyle" : "circle", "color":"red"})
ax.text(194,3,"1",fontsize=13, bbox={"boxstyle" : "circle", "color":"red"})

ax.text(0.0037,11,"RRS III",rotation=31, fontsize=12, weight='bold',bbox={"boxstyle": "round", "facecolor": "orange"})
ax.text(0.035,11,"RRS II",rotation=31, fontsize=12, weight='bold',bbox={"boxstyle": "round", "facecolor": "orange"})
ax.text(0.17,11,"RRS I",rotation=31, fontsize=12, weight='bold',bbox={"boxstyle": "round", "facecolor": "orange"})


plt.text(0.06, 20, '25 cm', fontsize=10, rotation=31, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(0.29, 20, '15 cm', fontsize=10, rotation=48, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(0.78, 20, '12 cm', fontsize=10, rotation=48, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(2.7, 20, '9 cm', fontsize=10, rotation=50, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(7.5, 20, '6 cm', fontsize=10, rotation=51, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(54, 20, '4 cm', fontsize=10, rotation=63, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))

plt.text(0.0011, 1.2, 'E = 1000 J', fontsize=11, rotation=35,weight='bold')
plt.text(0.006, 1.2, 'E = 700 J', fontsize=11, rotation=36,weight='bold')
plt.text(0.0255, 1.2, 'E = 700 J', fontsize=11, rotation=39,weight='bold')
plt.text(0.09, 1.05, 'E = 500 J', fontsize=11, rotation=31,weight='bold')

plt.text(0.0011, 3, 'RRS c/c 1.0 m', fontsize=11, rotation=90,weight='bold')
plt.text(0.0041, 3, 'RRS c/c 1.7 m', fontsize=11, rotation=90,weight='bold')
plt.text(0.011, 3, 'RRS c/c 2.3 m', fontsize=11, rotation=90,weight='bold')
plt.text(0.041, 3, 'RRS c/c 2.9 m', fontsize=11, rotation=90,weight='bold')
plt.text(0.11, 3, 'RRS c/c 4.0 m', fontsize=11, rotation=90,weight='bold')

plt.text(1.6, 1.5, '无喷浆锚杆间距', fontproperties='SimHei',fontsize=12,rotation=35,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.text(0.02, 35, '喷浆锚杆间距', fontproperties='SimHei',fontsize=12,rotation=20,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 

plt.plot([4, 4], [3.8,3.5], linestyle='-',color='black',linewidth=3)  
plt.text(3.1, 3.0, '1.6m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([10, 10], [5.4,4.9], linestyle='-',color='black',linewidth=3) 
plt.text(8.0, 4.1, '2.0m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([40, 40], [9,8.3], linestyle='-',color='black',linewidth=3)  
plt.text(31, 7.0, '3.0m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([100,100], [12.8,11.5], linestyle='-',color='black',linewidth=3) 
plt.text(80, 9.5, '4.0m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 

plt.plot([0.01, 0.01], [22,20], linestyle='-',color='black',linewidth=3) 
plt.text(0.008, 24, '1.0m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([0.04,0.04], [28,26], linestyle='-',color='black',linewidth=3)  
plt.text(0.03, 30, '1.2m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([0.1, 0.1], [33,31], linestyle='-',color='black',linewidth=3)  
plt.text(0.08, 36, '1.3m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([0.4, 0.4], [43,40], linestyle='-',color='black',linewidth=3) 
plt.text(0.3, 46, '1.5m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([1,1], [50,47], linestyle='-',color='black',linewidth=3)  
plt.text(0.8,54, '1.7m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([4,4], [63,60], linestyle='-',color='black',linewidth=3) 
plt.text(3, 70, '2.1m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([10,10], [77,74], linestyle='-',color='black',linewidth=3) 
plt.text(8, 84, '2.3m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([40,40], [84,82], linestyle='-',color='black',linewidth=3) 
plt.text(30, 87, '2.5m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 



ax_top.plot([0.001,1000], [yt2,yt2], linestyle='-',color='black',linewidth=0.5) 
ax_top.plot([0.001,1000], [yt3,yt3], linestyle='-',color='black',linewidth=0.5) 
ax_top.text(0.0025, yt1+0.1, '超差', fontproperties='SimHei',fontsize=14,rotation=0) 
ax_top.text(0.003, yt2+0.05, 'G', fontproperties='SimHei',fontsize=14,rotation=0,weight='bold') 
ax_top.plot([0.01,0.01], [yt1,yt3], linestyle='-',color='black',linewidth=0.5) 
ax_top.text(0.025, yt1+0.1, '极差', fontproperties='SimHei',fontsize=14,rotation=0) 
ax_top.text(0.035, yt2+0.05, 'F', fontproperties='SimHei',fontsize=14,rotation=0,weight='bold') 
ax_top.plot([0.1,0.1], [yt1,yt3], linestyle='-',color='black',linewidth=0.5) 
ax_top.text(0.25, yt1+0.1, '很差', fontproperties='SimHei',fontsize=14,rotation=0) 
ax_top.text(0.33, yt2+0.05, 'E', fontproperties='SimHei',fontsize=14,rotation=0,weight='bold') 
ax_top.plot([1,1], [yt1,yt3], linestyle='-',color='black',linewidth=0.5) 
ax_top.text(1.8, yt1+0.1, '差', fontproperties='SimHei',fontsize=14,rotation=0) 
ax_top.text(1.9, yt2+0.05, 'D', fontproperties='SimHei',fontsize=14,rotation=0,weight='bold') 
ax_top.plot([4,4], [yt1,yt3], linestyle='-',color='black',linewidth=0.5) 
ax_top.text(5, yt1+0.1, '一般', fontproperties='SimHei',fontsize=14,rotation=0) 
ax_top.text(6, yt2+0.05, 'C', fontproperties='SimHei',fontsize=14,rotation=0,weight='bold') 
ax_top.plot([10,10], [yt1,yt3], linestyle='-',color='black',linewidth=0.5) 
ax_top.text(18, yt1+0.1, '好', fontproperties='SimHei',fontsize=14,rotation=0) 
ax_top.text(18.5, yt2+0.05, 'B', fontproperties='SimHei',fontsize=14,rotation=0,weight='bold') 
ax_top.plot([40,40], [yt1,yt3], linestyle='-',color='black',linewidth=0.5) 
ax_top.text(50, yt1+0.1, '很好', fontproperties='SimHei',fontsize=14,rotation=0) 
ax_top.plot([100,100], [yt1,yt2], linestyle='-',color='black',linewidth=0.5) 
ax_top.text(150, yt1+0.1, '极好', fontproperties='SimHei',fontsize=14,rotation=0) 
ax_top.plot([400,400], [yt1,yt2], linestyle='-',color='black',linewidth=0.5) 
ax_top.text(500, yt1+0.1, '超好', fontproperties='SimHei',fontsize=14,rotation=0) 
ax_top.text(200, yt2+0.05, 'A', fontproperties='SimHei',fontsize=14,rotation=0,weight='bold') 
ax_top.text(0.55, yt3+0.1, '岩体质量和支护', fontproperties='SimHei',fontsize=14,rotation=0) 
#ax_top.plot([1000,1000], [yt1,yt4], linestyle='-',color='black',linewidth=0.5) 

#ax.text(0.001, -0.5, '无需支护',fontproperties='SimHei',fontsize=14,rotation=0)

plt.savefig('output/Q-system-2022.pdf')
plt.savefig('output/Q-system-2022.png')
# Show the plot
plt.show()

