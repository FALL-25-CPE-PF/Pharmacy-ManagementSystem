from management import *

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
