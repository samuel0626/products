import os # operation system
# 讀取檔案
products = []

if os.path.isfile('products.csv'):
	print('找到檔案了！')
	with open('products.csv', 'r', encoding = 'big5') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)

else:
	print('紀錄之檔案不存在......')

# 讓使用者輸入
#products = []
while True:
	name = input('請輸入商品名稱：')
	if name == 'q':
		break
	price = input('請輸入商品價格：')
	products.append([name, price])
print(products)

# 印出所有商品紀錄
for p in products:
	print(p[0], '的價格是：', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding = 'big5') as f:
	f.write('商品,價格' + '\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
