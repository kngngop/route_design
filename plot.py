import numpy as np 
import matplotlib.pyplot as plt  

#視覺化路徑結果，但是顯示座標為第一象限,程式結果為第二象限，因此對應位置稍微不太一樣

def drawthemap(width,height,printlist,obstacle_list,start,end):
	plt.grid(axis='x')				  #畫x軸
	plt.grid(axis='y')                #畫y軸
	plt.xlim(0,width) 				  #設定寬度	
	plt.ylim(0,height)				  #設定高度		
	for i in obstacle_list:			  #標示出障礙物 紅色叉叉	
		plt.plot(i[0],i[1],'rx')
	for i in printlist:		          
		plt.plot(i[0],i[1],'gd')      #標示出規劃路徑	 綠色+
	plt.plot(start[0],start[1],'y^')  #畫出起點 綠色三角形
	plt.plot(end[1],end[0],'bo')	  #畫出終點 藍色
	plt.show()