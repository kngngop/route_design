# 20190412
# @author Hsin-yu Lee 
'''目標：在地圖上規劃從指定起點到指定終點之路徑
限制：規劃出之路徑不可穿透障礙物，不可超出地圖範圍。路徑規劃只能橫向或縱向移動，不可斜向移動，例如不可由座標點 (2, 3) 直接移動到座標點 (3, 4)。
輸入 1：
一個包含障礙物的地圖檔案，地圖必定為矩形，長寬未限制。
地圖最左上角定義為座標原點，往右方為 X 軸方向，往下方為 Y 軸方向。例如 (2, 3) 代表原點右方第 2 格下方第 3 格之處。
每個座標點可能為 0 或 1；0 代表障礙物不能通過，1 代表可通過。X 軸座標點之間以空白隔開，Y 軸則使用換行表示。
輸入 2:
程式執行時期提示使用者輸入起點和終點座標。
輸出：
從起點至終點的路徑規劃，以座標表示，每一列代表一次移動。第一列必定為起點座標，最末列必定為終點座標，輸出範例如下：
2, 3
2, 4
3, 4
4, 4
4, 5'''
import matplotlib.pyplot as plt
import numpy as np 
import sys
from check_data import *
from method import *
from plot import *
#1可以走,0ˋ為障礙物, 2表示已拜訪節點

print("######################Program start######################")
option = input('How do you create the map? (1). Use the Built-in map (2). Upload the map  (3). Manual input :')
if option == '1':
	## 讀取txt檔案
	print("(1). Use the Built-in map")
	filename = 'map.txt'
elif option == '2':
	## 讀取自行輸入檔名之txt檔案
	print("(2). Upload the map")
	filename = input('Plese input your name of file (Example: map.txt): ')
elif option == '3':
	#手動輸入map大小,障礙物個數及位置
	print("(3). Manual input")
	create_width = input('Please input your width:')
	create_height = input('Please input your height:')
	create_width = int(create_width)
	create_height = int (create_height)
	create_onesmap = np.ones([create_height,create_width])
	print (create_onesmap)
	onstacle_num=input('How many obstacle do you want?')
	for i in range(0,int(onstacle_num)): 
		obstacle_x=input ('Please input your x coordinate of obstacle:')
		obstacle_y=input ('Please input your y coordinate of obstacle:')
		create_onesmap[int(obstacle_y),int(obstacle_x)]=0
		print(create_onesmap)	
else:pass

## 若為選項1 2 則讀取txt檔案
if option == '1' or option == '2':
	map_array = np.loadtxt(filename) 
	map_array_backup = np.loadtxt(filename)
else: #手動輸入則存取矩陣 
	map_array = create_onesmap
	map_array_backup = create_onesmap

print("=======================Start============================")
print ('Your map size is =', map_array.shape) #地圖大小
print (map_array)#印出地圖
#參數宣告
width  = (len(map_array)) # map_array列
height = (len(map_array[0])) # map_array行
plan=True 		#控制method之參數
plan2=False 	#控制是否進入死結之參數
nboundery=False	#控制下一個節點是否超出範圍之參數
boundery=False  #控制當前節點是否超出範圍之參數
check_input=False       #控制使用者輸入之參數
dead=False		#控制是否找到死結之參數
directions=[[0,1], [1,0], [0,-1],[-1,0]] #路徑方向 [0,1]右 [1,0]下 [0,-1]左 [-1,0]上
obstacle_list=check_obstacle(map_array,width,height) #呼叫check_obstacle()函式將map中的障礙物紀錄至obstacle_list中
	

#使用者輸入
while check_input==False:	#輸入起始座標之X軸
	print("========================================================")
	startx = input('Please input your initial x coordinate(input<'+str(width)+'):')
	startx = int(startx)							#將輸入之字串轉為數字
	check_input=check_error(startx,width,height)	#呼叫函式check_error()檢查範圍
else:
	check_input=False		
while check_input==False:	#輸入起始座標之Y軸
	starty = input('Please input your initial y coordinate(input<'+str(height)+'):')
	starty = int(starty)
	check_input=check_error(starty,width,height)
else:
	check_input=False
while check_input==False:	#輸入終點座標之X軸
	endx = input('Please input your terminal x coordinate(input<'+str(width)+'):')
	endx = int(endx)
	check_input=check_error(endx,width,height)
else:
	check_input=False
while check_input==False:	#輸入終點座標之Y軸
	endy = input('Please input your terminal y coordinate(input<'+str(height)+'):')
	endy = int(endy)
	check_input=check_error(endy,width,height)
else:
	check_input=False

start = [startx,starty] #起始座標
end = [endx,endy]		#終點座標

print("Your initial coordinate is ", start)							#印出起始座標與終點座標
print("Your end coordinate is ", end)
print("========================================================")

end =[endy,endx]				#終點
p = [starty,startx] 			#當前位置
map_array[p[0],p[1]] = 2 		#將起點標為已拜訪節點
a_list = [start]; 				#將每次紀錄之節點串聯起來
printlist = [start]; 			#將每次紀錄之節點串聯起來(印出使用)
ruledesign(map_array,p,end,width,height,directions,plan,plan2,nboundery,boundery,dead,a_list,printlist,map_array_backup) #路徑設計
drawthemap(width,height,printlist,obstacle_list,start,end) #畫出示意圖(僅供視覺化，座標位置與實際方位不大相同)
