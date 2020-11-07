import os # operation system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'big5') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
		print(products)
	return products

# 讓使用者輸入
#products = []
def user_input(products):
	while True:
		name = input('請輸入商品名稱：')
		if name == 'q':
			break
		price = input('請輸入商品價格：')
		products.append([name, price])
	print(products)
	return products

# 印出所有商品紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是：', p[1])


# 寫入檔案
def write_file(filename,products):
	with open(filename, 'w', encoding = 'big5') as f:
		f.write('商品,價格' + '\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')

def main():
	filename = 'products.csv'

	if os.path.isfile(filename):
		print('找到檔案了！')
		products = read_file(filename)
	else:
		print('找不到檔案！')

	products = user_input(products)
	print_products(products)
	write_file('products.csv',products)

main()