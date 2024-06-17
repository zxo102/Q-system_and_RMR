#作者：欧阳治华，2024年6月15日, zxo102@qq.com

import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# Read the CSV file
df1 = pd.read_csv('Q-system-1993/Q-curve1.csv')
x1 = df1['x']
y1 = df1['Curve1']

df2 = pd.read_csv('Q-system-1993/Q-curve2.csv')
x2 = df2['x']
y2 = df2['Curve2']

df3 = pd.read_csv('Q-system-1993/Q-curve3.csv')
x3 = df3['x']
y3 = df3['Curve3']

df4 = pd.read_csv('Q-system-1993/Q-curve4.csv')
x4 = df4['x']
y4 = df4['Curve4']

df5 = pd.read_csv('Q-system-1993/Q-curve5.csv')
x5 = df5['x']
y5 = df5['Curve5']

df6 = pd.read_csv('Q-system-1993/Q-curve6.csv')
x6 = df6['x']
y6 = df6['Curve6']

df7 = pd.read_csv('Q-system-1993/Q-curve7.csv')
x7 = df7['x']
y7 = df7['Curve7']

df8 = pd.read_csv('Q-system-1993/Q-curve8.csv')
x8 = df8['x']
y8 = df8['Curve8']

df9 = pd.read_csv('Q-system-1993/Q-curve9.csv')
x9 = df9['x']
y9 = df9['Curve9']

df10 = pd.read_csv('Q-system-1993/Q-curve10.csv')
x10 = df10['x']
y10 = df10['Curve10']

df11 = pd.read_csv('Q-system-1993/Q-curve11.csv')
x11 = df11['x']
y11 = df11['Curve11']

df12 = pd.read_csv('Q-system-1993/Q-curve12.csv')
x12 = df12['x']
y12 = df12['Curve12']


p9 = pd.read_csv('Q-system-1993/Q-polygon9.csv')
xp9 = p9['x']
yp9 = p9['Polygon9']
p8 = pd.read_csv('Q-system-1993/Q-polygon8.csv')
xp8 = p8['x']
yp8 = p8['Polygon8']
p7 = pd.read_csv('Q-system-1993/Q-polygon7.csv')
xp7 = p7['x']
yp7 = p7['Polygon7']
p6 = pd.read_csv('Q-system-1993/Q-polygon6.csv')
xp6 = p6['x']
yp6 = p6['Polygon6']
p5 = pd.read_csv('Q-system-1993/Q-polygon5.csv')
xp5 = p5['x']
yp5 = p5['Polygon5']
p4 = pd.read_csv('Q-system-1993/Q-polygon4.csv')
xp4 = p4['x']
yp4 = p4['Polygon4']
p3 = pd.read_csv('Q-system-1993/Q-polygon3.csv')
xp3 = p3['x']
yp3 = p3['Polygon3']
p2 = pd.read_csv('Q-system-1993/Q-polygon2.csv')
xp2 = p2['x']
yp2 = p2['Polygon2']


# Set the width and height of the plot
width = 11  # Width in inches
#height = 6  # Height in inches
height = 7  # Height in inches

# Create a figure and axis
#fig, axs = plt.subplots(nrows=1, ncols=1, sharex=False, sharey=False, figsize=None, dpi=None, subplot_kw=None, gridspec_kw=None)
#fig, ax = plt.subplots(figsize=(width, height))
#fig, (ax_top,ax) = plt.subplots(2, 1, figsize=(6, 20), sharex=True, gridspec_kw={'height_ratios': [5, 15], 'hspace': 0})
fig, (ax_top,ax) = plt.subplots(2, 1, figsize=(width,height), sharex=True, gridspec_kw={'height_ratios':[1,6],'hspace':0})

"""
fig = plt.figure()
gs  = fig.add_gridspec(2,hspace=0)
axs = gs.subplots(figsize=(width,height),sharex=True,gridspec_kw={'height_ratios': [1,90]})
ax_top = axs[0]
ax     = axs[1]
"""

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
ax.plot(x9, y9, marker='None', linestyle='-',color='black')
ax.plot(x10, y10, marker='None', linestyle='-',color='black')
ax.plot(x11, y11, marker='None', linestyle='-',color='black')
ax.plot(x12, y12, marker='None', linestyle='-',color='black')

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
#ax.grid(which='major', linestyle='-', linewidth='0.5', color='gray')
#plt.minorticks_on()
ax.grid(which='both', linestyle='-', linewidth='0.5', color='gray')

# Write Chinese text on the plot
#plt.text(1, 15, '瞬间\n垮塌', fontproperties='SimHei', fontsize=16) 
#plt.text(1000, 1, '无需\n支护', fontproperties='SimHei', fontsize=16) 
#plt.text(800, 1.8, 'RMR分值', fontproperties='SimHei', fontsize=12, rotation=20) 
#plt.text(5, 7, 'RMR分值', fontproperties='SimHei', fontsize=12,rotation=35) 

# Add labels and title
ax.set_xlabel(r'岩体质量$Q=\frac{RQD}{J_n}\times \frac{J_r}{J_a} \times \frac{J_w}{SRF}$',fontproperties='SimHei', fontsize=12)
ax.set_ylabel('跨度或高度(米)/ESR', fontproperties='SimHei',fontsize=12)
#ax.set_ylabel(r'$\frac{跨度或高度}{ESR}$', fontsize=12)
ax2.set_ylabel('锚杆长度(米) ESR=1', fontproperties='SimHei',fontsize=12)

#ylabel = r'$\frac{Y轴}{数值}$'  # LaTeX formatted string with Chinese characters
#ax.set_ylabel(ylabel, fontproperties=chinese_font)

#ax.set_title('岩体质量评分',fontproperties='SimHei', fontsize=12)

plt.fill(xp9, yp9, color='grey', alpha=0.9)
plt.fill(xp8, yp8, color='grey', alpha=0.8)
plt.fill(xp7, yp7, color='grey', alpha=0.7)
plt.fill(xp6, yp6, color='grey', alpha=0.6)
plt.fill(xp5, yp5, color='grey', alpha=0.5)
plt.fill(xp4, yp4, color='grey', alpha=0.4)
plt.fill(xp3, yp3, color='grey', alpha=0.3)
plt.fill(xp2, yp2, color='grey', alpha=0.2)

plt.figtext(0.2,0.455,"9",fontsize=13, bbox={"boxstyle" : "circle", "color":"yellow"})
plt.figtext(0.32,0.455,"8",fontsize=13, bbox={"boxstyle" : "circle", "color":"yellow"})
plt.figtext(0.42,0.455,"7",fontsize=13, bbox={"boxstyle" : "circle", "color":"yellow"})
plt.figtext(0.48,0.455,"6",fontsize=13, bbox={"boxstyle" : "circle", "color":"yellow"})
plt.figtext(0.55,0.455,"5",fontsize=13, bbox={"boxstyle" : "circle", "color":"yellow"})
plt.figtext(0.61,0.455,"4",fontsize=13, bbox={"boxstyle" : "circle", "color":"yellow"})
plt.figtext(0.665,0.455,"3",fontsize=13, bbox={"boxstyle" : "circle", "color":"yellow"})
plt.figtext(0.71,0.455,"2",fontsize=13, bbox={"boxstyle" : "circle", "color":"yellow"})
plt.figtext(0.85,0.455,"1",fontsize=13, bbox={"boxstyle" : "circle", "color":"yellow"})

#plt.text(0.0025, 5.7, '25 cm', fontsize=12,rotation=35) 
plt.text(0.0025, 5.7, '25 cm', fontsize=10, rotation=35, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(0.032, 5.7, '15 cm', fontsize=10, rotation=46, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(0.12, 5.7, '12 cm', fontsize=10, rotation=48, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(0.45, 5.7, '9 cm', fontsize=10, rotation=50, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(1.3, 5.7, '5 cm', fontsize=10, rotation=52, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.text(5, 5.7, '4 cm', fontsize=10, rotation=54, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))

plt.text(1.6, 1.5, '无喷浆锚杆间距', fontproperties='SimHei',fontsize=12,rotation=35,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.text(0.02, 35, '喷浆锚杆间距', fontproperties='SimHei',fontsize=12,rotation=20,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 

#plt.text(0.4, 1.5, '4 cm', fontsize=10, rotation=54, bbox=dict(boxstyle='round,pad=0.1', facecolor='lightblue', edgecolor='white'))
plt.plot([0.4, 0.4], [1.6,1.5], linestyle='-',color='black',linewidth=3) 
plt.text(0.32, 1.25, '1.0m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
plt.plot([1,1], [2.3,2.1], linestyle='-',color='black',linewidth=3)  
plt.text(0.8, 1.75, '1.3m', fontsize=10,rotation=0,bbox=dict(boxstyle='round,pad=0.1', facecolor='white', edgecolor='lightblue')) 
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
ax_top.text(0.55, yt3+0.1, '岩体质量与支护', fontproperties='SimHei',fontsize=14,rotation=0) 
#ax_top.plot([1000,1000], [yt1,yt4], linestyle='-',color='black',linewidth=0.5) 

#ax.text(0.001, -0.5, '无需支护',fontproperties='SimHei',fontsize=14,rotation=0)

# Adjust layout for no gap between subplots
#plt.subplots_adjust(hspace=0)

plt.savefig('output/Q-system-1993.pdf')
plt.savefig('output/Q-system-1993.png')
# Show the plot
plt.show()

