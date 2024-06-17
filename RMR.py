#作者：欧阳治华，2024年6月15日, zxo102@qq.com
import numpy as np
import pandas as pd
import cv2
import matplotlib.pyplot as plt

# interpolate a value
def find_point_between_Z_values(x1, y1, Z1, x2, y2, Z2, Z3):
    # Calculate the parameter t
    t = (Z3 - Z1) / (Z2 - Z1)

    # Calculate the coordinates of the point (x3, y3)
    x3 = x1 + t * (x2 - x1)
    y3 = y1 + t * (y2 - y1)

    return x3, y3

# Read the CSV file
df1 = pd.read_csv('RMR/RMR-curve1.csv')
x1 = df1['x']
y1 = df1['Curve1']
df2 = pd.read_csv('RMR/RMR-curve2.csv')
x2 = df2['x']
y2 = df2['Curve2']

p00 = pd.read_csv('RMR/RMR-polygon00.csv')
xp00 = p00['x']
yp00 = p00['Polygon00']
p20 = pd.read_csv('RMR/RMR-polygon20.csv')
xp20 = p20['x']
yp20 = p20['Polygon20']
p30 = pd.read_csv('RMR/RMR-polygon30.csv')
xp30 = p30['x']
yp30 = p30['Polygon30']
p40 = pd.read_csv('RMR/RMR-polygon40.csv')
xp40 = p40['x']
yp40 = p40['Polygon40']
p50 = pd.read_csv('RMR/RMR-polygon50.csv')
xp50 = p50['x']
yp50 = p50['Polygon50']
p60 = pd.read_csv('RMR/RMR-polygon60.csv')
xp60 = p60['x']
yp60 = p60['Polygon60']
p70 = pd.read_csv('RMR/RMR-polygon70.csv')
xp70 = p70['x']
yp70 = p70['Polygon70']
p80 = pd.read_csv('RMR/RMR-polygon80.csv')
xp80 = p80['x']
yp80 = p80['Polygon80']
p90 = pd.read_csv('RMR/RMR-polygon90.csv')
xp90 = p90['x']
yp90 = p90['Polygon90']
p100 = pd.read_csv('RMR/RMR-polygon100.csv')
xp100 = p100['x']
yp100 = p100['Polygon100']



# Set the width and height of the plot
width = 10  # Width in inches
height = 6  # Height in inches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(width, height))

ax.set_xlim(0.1, 550000)
ax.set_ylim(0.5, 28.25)

ax.plot(x1, y1, marker='None', linestyle='-',color='black')
ax.plot(x2, y2, marker='None', linestyle='-',color='black')

# Set the scales to logarithmic
ax.set_xscale('log')
ax.set_yscale('log')

# Set the tick values and labels for the X axis
ax.set_xticks([0.1, 1, 10, 100, 1000, 10000, 100000])
ax.set_xticklabels(['0.1', '1', '10', '$10^2$', '$10^3$', '$10^4$', '$10^5$'])

# Set the tick values and labels for the Y axis
ax.set_yticks([1, 2, 4, 6, 8, 10, 15, 20])
ax.set_yticklabels(['1', '2', '4', '6', '8', '10', '15', '20'])

#Set the ticks to point inwards
plt.tick_params(axis='both', which='both',direction='in',bottom=True, top=True, left=True, right=True, labelleft=True, labelbottom=True, labeltop=False, labelright=False)

# Add grid for major ticks
ax.grid(which='major', linestyle='-', linewidth='0.5', color='gray')

# Write Chinese text on the plot
plt.text(1, 15, '瞬间\n垮塌', fontproperties='SimHei', fontsize=16) 
plt.text(1000, 1, '无需\n支护', fontproperties='SimHei', fontsize=16) 
plt.text(800, 1.8, 'RMR分值', fontproperties='SimHei', fontsize=12, rotation=20) 
plt.text(5, 7, 'RMR分值', fontproperties='SimHei', fontsize=12,rotation=35) 
# Add labels and title
ax.set_xlabel('采空区稳定时间(小时)',fontproperties='SimHei', fontsize=12)
ax.set_ylabel('采空区顶板跨度(米)',fontproperties='SimHei', fontsize=12)
#ax.set_title('岩体质量评分',fontproperties='SimHei', fontsize=12)

# Draw a line from (x1, y1) to (x2, y2)
plt.plot([x1[1], x2[1]], [y1[1], y2[1]], linestyle='--',color='black')  # Draw a line between two points
plt.text(x1[1]-0.05,y1[1]+0.15, '20') 
plt.text(x2[1],y2[1]-0.1, '20') 

plt.plot([x1[2], x2[2]], [y1[2], y2[2]], linestyle='--',color='black') 
plt.plot([x1[4], x2[4]], [y1[4], y2[4]], linestyle='--',color='black') 
plt.plot([x1[6], x2[6]], [y1[6], y2[6]], linestyle='--',color='black') 

plt.plot([x1[3], x2[3]], [y1[3], y2[3]], linestyle='--',color='black')  # Draw a line between two points
plt.text(x1[3]-1,y1[3]+0.5, '40') 
plt.text(x2[3],y2[3]-0.2, '40') 

plt.plot([x1[5], x2[5]], [y1[5], y2[5]], linestyle='--',color='black')  # Draw a line between two points
plt.text(x1[5]-1,y1[5]+1, '60') 
plt.text(x2[5],y2[5]-0.4, '60') 

plt.plot([x1[7], x2[7]], [y1[7], y2[7]], linestyle='--',color='black')  # Draw a line between two points
plt.text(x1[7]-2,y1[7]+1.3, '80') 
plt.text(x2[7],y2[7]-0.5, '80') 

plt.text(24,31, '1天', fontproperties='SimHei', fontsize=12) 
plt.text(168,31, '1星期', fontproperties='SimHei', fontsize=12) 
plt.text(720,31, '1月', fontproperties='SimHei', fontsize=12) 
plt.text(8760,31, '1年', fontproperties='SimHei', fontsize=12) 
plt.text(87600,31, '10年', fontproperties='SimHei', fontsize=12) 

plt.fill(xp00, yp00, color='red', alpha=0.5)
plt.fill(xp20, yp20, color='grey', alpha=0.8)
plt.fill(xp30, yp30, color='grey', alpha=0.7)
plt.fill(xp40, yp40, color='grey', alpha=0.6)
plt.fill(xp50, yp50, color='grey', alpha=0.5)
plt.fill(xp60, yp60, color='grey', alpha=0.4)
plt.fill(xp70, yp70, color='grey', alpha=0.3)
plt.fill(xp80, yp80, color='grey', alpha=0.2)
plt.fill(xp90, yp90, color='grey', alpha=0.1)
plt.fill(xp100, yp100, color='yellow', alpha=0.2)

"""
#RMR0 < 80
RMR0 = 63
Z3 = RMR0
RMR1 = int(RMR0/10) * 10
RMR2 = (int(RMR0/10)+1) * 10
x11,y11,Z1 = x1[int(RMR0/10)-1],y1[int(RMR0/10)-1],RMR1
x12,y12,Z2 = x1[int(RMR0/10)],y1[int(RMR0/10)],RMR2
x10, y10 = find_point_between_Z_values(x11, y11, Z1, x12, y12, Z2, Z3)

x21,y21,Z1 = x2[int(RMR0/10)-1],y2[int(RMR0/10)-1],RMR1
x22,y22,Z2 = x2[int(RMR0/10)],y2[int(RMR0/10)],RMR2
x20, y20 = find_point_between_Z_values(x21, y21, Z1, x22, y22, Z2, Z3)

xi = [x10,x20]
yi = [y10,y20]
ax.plot(xi, yi, marker='o', linestyle='-',color='red')
plt.text(xi[0]-2,yi[0]+1.3, '%s'%RMR0) 
plt.text(xi[1],yi[1]-0.5, '%s'%RMR0) 
"""


plt.savefig('output/RMR.pdf')
plt.savefig('output/RMR.png')
# Show the plot
plt.show()

