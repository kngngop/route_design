#當前座標與方位相加
def list_add(a,b):             
    c = []
    for z in range(0,2):
        c.append(a[z]+b[z])
    return c	
#檢查使用者輸入錯誤
def check_error(c,width,height):	
	if c>=0 and c<height and c<width: #若輸入的數字大於0,並且不超過長寬，則輸入正確
		check_input=True
	else:
		print("Your input is out of range,please input again!")  #輸入錯誤
		check_input=False	
	return check_input

#檢查下一個方向的節點是否超過範圍	
def check_nextboundery(p,width,height):
	if p[1]+1 < width and p[0]+1 <height and p[1]-1 >= 0 and p[0]-1 >=0:
		nboundery = False    
	else:
		nboundery = True
	return nboundery

#檢查當前的節點是否超過範圍	
def check_boundery(p,width,height):
	if p[1] < width and p[0]<height and p[1] >= 0 and p[0] >=0:
		boundery = False
		return boundery    
	else:
		#print("不能走")
		boundery = True
		return boundery

#將map裡為障礙物之座標印出
def check_obstacle(map,width,height):
	obstacle_list=[]
	for x in range(0,width):
		for y in range(0,height):
			if map[x,y]==0:
				obstacle=([y,x])
				obstacle_list.append(obstacle)
			else:
				pass
	print("===========The coordinates of obstacle=================")		
	print (obstacle_list)
	return obstacle_list
#檢查節點是否遇到死結
#將當前節點checkp與四個方位directions分別檢查是否遇到障礙物0或走過的路2或遇到邊界boundery=True
#每遇到一個便由num記錄下來，若num=4則可以判斷遇到死結
def check_deadlock(map,checkp,directions,width,height):
	num=0
	for i in range(0,4):
		dir_temp = directions[i]
		newcheckp = list_add(checkp,dir_temp)
		boundery = check_boundery(newcheckp,width,height)
		if boundery==True:
			num = num+1
			pass
		else:
			x=newcheckp[0]
			y=newcheckp[1]
			if map[x,y]==0 or map[x,y]==2:
				num = num+1
			else:
				pass
	if num==4:
		print("Dead lock")
		return True	
	else:
		pass
