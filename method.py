import numpy as np 
from check_data import *
#路徑規劃
def ruledesign(map_array,p,end,width,height,directions,plan,plan2,nboundery,boundery,dead,a_list,printlist,map_array_backup):
	while plan == True:

		check_nextboundery(p,width,height)                    		#檢查下一個節點是否為邊界
		if nboundery == False:
			for i in range(0,4):                              		#檢查四周位置			
				dir_temp = directions[i]                      		#按順序確認四周			
				nextp = list_add(p,dir_temp)  	              		#當前座標p 與路徑方向dir_temp 相加			
				boundery = check_boundery(nextp,width,height) 		#檢查相加之後的節點是否超過範圍 若無超出範圍則boundary=False,反之則為True
				if boundery == False:      					  		#if判斷式 無超出範圍	
					nx = nextp[0]                             		#將相加之後的節點座標x暫存到nx
					ny = nextp[1]                             		#將相加之後的節點座標y暫存到ny
				elif boundery == True: 								#elif判斷式 超出範圍 需換下一個方向		          		
					dir_temp = directions[i+1]				  		#朝下一個方向 並將其方位座標暫存至dir_temp
					nextp = list_add(p,dir_temp)  	          		#當前座標p 與路徑方向dir_temp 相加		
					boundery = check_boundery(nextp,width,height)	#檢查相加之後的節點是否超過範圍 若無超出範圍則boundary=False,反之則為True
				else:
					pass
				if boundery==False  and map_array[nx,ny] ==1 and nx>=0 and ny>=0 and nx < width and ny <height: #if判斷式 若下個節點無超出範圍(False)並且可以前進(=1)
					nx = nextp[0] 														 					    #將相加之後的節點座標x暫存到nx
					ny = nextp[1]                                                                               #將相加之後的節點座標y暫存到ny
					map_array[nx,ny] = 2 			#將節點座標值標為已拜訪節點(=2)				
					p = [nx,ny] 					#將節點更新至當前節點p
					dead=check_deadlock(map_array,p,directions,width,height)           #函式check_deadlock將檢查更新之節點是否遇到死結，dead=True 判斷死結, dead=False 無死結
					chang_p=[ny,nx]					#chande_p為印出節點的參數 將xy軸對調
					a_list.append(p)				#將每一次更新的節點串接到a_list路徑中
					printlist.append(chang_p)		#將每一次更新的節點(xy軸對調)串接到printlist路徑中,最後會印出路徑
					#print("current:",chang_p)		#印出每一次所更新之節點
					#print("update map")				
					#print(map_array)	            #印出每一次更新過後的map
					if p == end:     				#若當前位置與終點相同則停止
						plan = False  	 			#跳出while迴圈		
					break
				else:                               
					if dead == True:				#若判斷為死結,則跳出while迴圈,並且透過plan2參數導引至函式solve_deadlock(),以解決死結問題	
						plan2 = True
						plan = False				 	
					else:
						continue			#尚未到達終點則繼續for迴圈->檢查四周位置

	else:
		if plan2==True:						#節點確實遇到死結 呼叫函式solve_deadlock()
			#print("Dead lock")
			#print (printlist) 
			solve_deadlock(a_list,printlist,map_array_backup,end,width,height,directions)
		else:
			print("Finish!")
			print("========================================================")
			#print("The map")
			#print(map_array) 						    #印出更新過後的map
			print("====================The path============================")
			for i in printlist:
				print (i)                              #程式結束 印出路徑座標
			print("====================Terminal===========================")

#解決死結路徑問題
#透過函式check_deadlock()檢查是否遇到死結，接著從走到一半的路徑mylist中取得最後一個座標位置deadp標註起來，並且將路徑回到上一個節點p。
#將上一個節點p作為起始坐標，繼續與ruledesign的方法更新路徑，若遇到死結則循環此步驟直到走到終點
def solve_deadlock(mylist,printlist,map_array,endpoint,width,height,directions):
	lenth=(len(mylist))
	deadp = mylist[lenth-1] #死結座標
	map_array[deadp[0],deadp[1]] = 3
	p = mylist[lenth-2] 					#回到上一個節點
	mylist.append(p)    					#將上一個節點p串接到路徑mylist
	#print("終點",endpoint)
	printp=[p[1],p[0]]						#印出座標時xy軸對調
	printlist.append(printp)				#將xy軸對調之後的路徑串接至printlist,最後會印出路徑
	#print("回上一個節點:",printp)
	plan=True #控制while
	plan2=False
	nboundery=False
	boundery=False
	user=True
	dead=False
	end=endpoint

	while plan == True:
		check_nextboundery(p,width,height)                    		#檢查下一個節點是否為邊界
		if nboundery == False:
			for i in range(0,4):                              		#檢查四周位置			
				dir_temp = directions[i]                      		#按順序確認四周
				nextp = list_add(p,dir_temp)  	              		#當前座標p 與路徑方向dir_temp 相加			
				boundery = check_boundery(nextp,width,height) 		#檢查相加之後的節點是否超過範圍 若無超出範圍則boundary=False,反之則為True
				if boundery == False:      					  		#if判斷式 無超出範圍	
					nx = nextp[0]                             		#將相加之後的節點座標x暫存到nx
					ny = nextp[1]                             		#將相加之後的節點座標y暫存到ny
				elif boundery == True: 				          		#elif判斷式 超出範圍 需換下一個方向
					dir_temp = directions[i+1]				  		#朝下一個方向 並將其方位座標暫存至dir_temp
					nextp = list_add(p,dir_temp)  	          		#當前座標p 與路徑方向dir_temp 相加		
					boundery = check_boundery(nextp,width,height)	#檢查相加之後的節點是否超過範圍 若無超出範圍則boundary=False,反之則為True
				else:
					pass
				if boundery==False  and map_array[nx,ny] ==1 and nx>=0 and ny>=0 and nx < width and ny <height: #if判斷式 若下個節點無超出範圍(False)並且可以前進(=1)
					nx = nextp[0] 														 					   #將相加之後的節點座標x暫存到nx
					ny = nextp[1]                                                                              #將相加之後的節點座標y暫存到ny
					map_array[nx,ny] = 2 			#將節點座標值標為已拜訪節點(=2)				
					p = [nx,ny] 					#將節點更新至當前節點p
					chang_p=[ny,nx]
					dead=check_deadlock(map_array,p,directions,width,height)
					mylist.append(p)				#將每一次更新的節點串聯到a_list路徑中
					printlist.append(chang_p)
					#print("current:",chang_p)						#印出每一次所更新之節點
					#print("update map")				
					#print(map_array)	            #印出每一次更新過後的map
					if p == end:     				#若當前位置與終點相同則停止
						plan = False  	 			#跳出while迴圈		
					break
				else:
					if dead == True:					
						plan2 = True
						plan = False				 	
					else:
						continue			#尚未到達終點則繼續for迴圈->檢查四周位置

	else:
		if plan2==True:
			#print("dead lock")
			#print (printlist) 
			solve_deadlock(mylist,printlist,map_array,end,width,height,directions)
		else:
			print("dead lock solve, Finish!")
			#print("========================================================")
			#print("The map")
			#print(map_array) 						    #印出更新過後的map
			print("====================The path============================")
			for i in printlist:
				print (i)                              #程式結束 印出路徑座標
			print("====================Terminal===========================")