#data = [1, 3, 5, 7, 9] # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼
#with open('test.txt', 'w') as f:
#    for d in data:
#        f.write(str(d) + '\n')


products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是：', p[1])