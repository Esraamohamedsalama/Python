product_list=[]
cost_list=[]
Amount_list=[]
customar_product=[]
customar_cost=[]
customar_amount=[]

def Print_list():
	print(product_list[::1])
	print(cost_list[::1])
	print(Amount_list[::1])

def print_Bill():
    cost =0
    for i in range(len(customar_product)):
        print(customar_product[i],"	     ",customar_amount[i],"     ",customar_cost[i])
        cost+=customar_cost[i]
    print("Total Cost------>",cost)
    

product_list.append("tomato")
cost_list.append(12)
Amount_list.append(60)
product_list.append("strawbarry")
cost_list.append(12)
Amount_list.append(90)
product_list.append("orange")
cost_list.append(16)
Amount_list.append(900)
product_list.append("mango")
cost_list.append(30)
Amount_list.append(50)
product_list.append("blue barry")
cost_list.append(33)
Amount_list.append(69)
cost_list[3]=20

product_list.append("apple")
cost_list.append(22)
Amount_list.append(36)
product_list.append("apple")
cost_list.append(22)
Amount_list.append(36)
product_list.append("apple")
cost_list.append(22)
Amount_list.append(6)
