import os

med_file = "medicines.txt"
cus_file = "customers.txt"
sales_file = "sales.txt"

def load_file(file):
    if not os.path.exists(file):
        return []
    f = open(file, "r")
    data = f.read().splitlines()
    f.close()
    return data

def save_file(file, data):
    f = open(file, "w")
    for line in data:
        f.write(line + "\n")
    f.close()

def add_medicine():
    mid = input("Medicine ID: ")
    name = input("Medicine Name: ")
    price = input("Price: ")
    qty = input("Quantity: ")
    exp = input("Expiry Date: ")

    meds = load_file(med_file)
    meds.append(mid + "," + name + "," + price + "," + qty + "," + exp)
    save_file(med_file, meds)
    print("Medicine added")

def show_medicines():
    meds = load_file(med_file)
    if len(meds) == 0:
        print("No medicines found")
        return
    for m in meds:
        print(m)

def add_customer():
    cid = input("Customer ID: ")
    name = input("Customer Name: ")
    phone = input("Contact: ")

    customers = load_file(cus_file)
    customers.append(cid + "," + name + "," + phone)
    save_file(cus_file, customers)
    print("Customer added")

def sale():
    mid = input("Medicine ID: ")
    qty = int(input("Quantity sold: "))

    meds = load_file(med_file)
    new_data = []
    found = False
    price = 0

    for m in meds:
        d = m.split(",")
        if d[0] == mid:
            found = True
            stock = int(d[3])
            price = float(d[2])
            if qty > stock:
                print("Not enough stock")
                return
            d[3] = str(stock - qty)
            new_data.append(",".join(d))
        else:
            new_data.append(m)

    if found == False:
        print("Medicine not found")
        return

    save_file(med_file, new_data)

    total = qty * price
    sales = load_file(sales_file)
    sales.append(mid + "," + str(qty) + "," + str(total))
    save_file(sales_file, sales)

    print("Sale complete. Total:", total)

def report():
    sales = load_file(sales_file)
    total = 0
    for s in sales:
        total += float(s.split(",")[2])
    print("Total Revenue:", total)

def low_stock():
    meds = load_file(med_file)
    for m in meds:
        d = m.split(",")
        if int(d[3]) <= 5:
            print(d[1], "Low stock:", d[3])

while True:
    print("""
1 Add Medicine
2 View Medicines
3 Add Customer
4 Sale
5 Sales Report
6 Low Stock Alert
7 Exit
""")
    try:
        ch = int(input("Choice: "))
    except:
        print("Invalid input")
        continue

    if ch == 1:
        add_medicine()
    elif ch == 2:
        show_medicines()
    elif ch == 3:
        add_customer()
    elif ch == 4:
        sale()
    elif ch == 5:
        report()
    elif ch == 6:
        low_stock()
    elif ch == 7:
        print("Program Ended")
        break
    else:
        print("Wrong choice")