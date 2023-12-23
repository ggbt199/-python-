def w_move(): #向上
    global score 
    itemp=0
    New_num=0
    for i in range(4): #每排都要 
        temp=[0]*4 #臨時陣列 
        itemp=0
        for j in range(3): #一排中前三個 
            if table[j][i]!=0:
                no_plus=0 #兩個都不等於0時, no_plus=1 
                for t in range(j+1,4):
                    if table[t][i]!=0:				
                        no_plus=1
                        if table[j][i]==table[t][i]: #如果相等則須合併並複製到臨時陣列
                            temp[itemp]=table[j][i]*2 #合併 
                            itemp+=1
                            score+=table[j][i]*2 #計分 
                            table[j][i]=0
                            table[t][i]=0
                            break
						
                        else:
                            temp[itemp]=table[j][i] #如果不相等則需複製到臨時陣列 
                            itemp+=1
                            break
					
                if no_plus==0:
                        temp[itemp]=table[j][i]
                        itemp+=1

        temp[itemp]=table[3][i] #每排中最後一個 不用檢查 
		
		#檢查有沒有移動，如果有 New_num=1
        for j in range(4):
            if table[j][i]!=temp[j]:
                New_num=1
                break

        for j in range(4): #將臨時陣列覆蓋上去 
            table[j][i]=temp[j]
	
    if New_num==1: #如果有移動則新增一個2或4 
        new2or4()


def d_move(): #向下 
    global score
    itemp=0
    New_num=0
    for i in range(4):
        temp=[0]*4
        itemp=3
        for j in range(3,0,-1):
            if table[i][j]!=0:
                no_plus=0
                for t in range(j-1,-1,-1):
                    if table[i][t]!=0:				
                        no_plus=1
                        if table[i][j]==table[i][t]:
                            temp[itemp]=table[i][j]*2
                            itemp-=1
                            score+=table[i][j]*2
                            table[i][j]=0
                            table[i][t]=0
                            break
                            
                        else:
                            temp[itemp]=table[i][j]
                            itemp-=1
                            break
					
                if no_plus==0:
                        temp[itemp]=table[i][j]
                        itemp-=1

        temp[itemp]=table[i][0] #第一行
        for j in range(4):
            if table[i][j]!=temp[j]:
                New_num=1
                break
			
        for j in range(4):
            table[i][j]=temp[j]
	
    if New_num==1:
        new2or4()


def a_move(): #向左 
    global score
    itemp=0
    New_num=0
    for i in range(4):
        temp=[0]*4
        itemp=0
        for j in range(3):
            if table[i][j]!=0:
                no_plus=0
                for t in range(j+1,4):
                    if table[i][t]!=0:				
                        no_plus=1
                        if table[i][j]==table[i][t]:
                            temp[itemp]=table[i][j]*2
                            itemp+=1
                            score+=table[i][j]*2
                            table[i][j]=0
                            table[i][t]=0
                            break
						
                        else:
                            temp[itemp]=table[i][j]
                            itemp+=1
                            break
							
                if no_plus==0:
                    temp[itemp]=table[i][j]
                    itemp+=1
		
        temp[itemp]=table[i][3] #最後一行
        for j in range(4):
            if table[i][j]!=temp[j]:
                New_num=1
                break
			
        for j in range(4):
            table[i][j]=temp[j]
	
    if New_num==1:
        new2or4()


def s_move(): #向右 
    global score
    itemp=0
    New_num=0
    for i in range(4):
        temp=[0]*4
        itemp=3
        for j in range(3,0,-1):
            if table[j][i]!=0:
                no_plus=0
                for t in range(j-1,-1,-1):
                    if table[t][i]!=0:				
                        no_plus=1
                        if table[j][i]==table[t][i]:
                            temp[itemp]=table[j][i]*2
                            itemp-=1
                            score+=table[j][i]*2
                            table[t][i]=0
                            table[j][i]=0
                            break
					
                        else:
                            temp[itemp]=table[j][i]
                            itemp-=1
                            break
					
                if no_plus==0:
                    temp[itemp]=table[j][i]
                    itemp-=1

        temp[itemp]=table[0][i] #第一行
        for j in range(4):
            if table[j][i]!=temp[j]:
                New_num=1
                break
			
        for j in range(4):
            table[j][i]=temp[j]
	
    if New_num==1:
        new2or4()