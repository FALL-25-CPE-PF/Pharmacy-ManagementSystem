from file_handler import load_file, save_file

med_file = "medicines.txt"
cus_file = "customers.txt"
sales_file = "sales.txt"

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

    