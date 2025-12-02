# 24S1020031 - Mai Đăng Khoa
products = []

def add_product(name, price, quantity):
    product = {
        'name': name,
        'price': price,
        'qty': quantity
    }
    products.append(product)

def view_inventory():
    if not products:
        print("Kho hiện đang trống!")
        return
    print('Danh sách sản phẩm trong kho:')
    stt = 1
    for p in products:
        print(f"{stt}. Sản phẩm: {p['name']}, giá: {p['price']}, số lượng: {p['qty']}")
        stt += 1

def  check_low_stock():
    if not products:
        print("Kho hiện tại đang trống")
        return
    print('Danh sách sản phẩm có số lượng dưới 5: ')
    print('--------------------------')
    stt = 1
    for p in products:
        if p['qty'] < 5:
            print(f"{stt}. Sản phẩm: {p['name']}, giá: {p['price']}, số lượng: {p['qty']}")
            stt += 1

def main():
    print('Menu quản lý Inventory:')
    print('--------------------------')
    print('1. Thêm sản phẩm')
    print('2. Xem danh sách sản phẩm')
    print('3. Duyệt danh sách sản phẩm có số lượng dưới 5')
    print('4. Thoát chương trình!!!')
    print('--------------------------')
