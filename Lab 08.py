user = int(input("Please enter the number of the table you require: "))
count = 0
if user >=0:
    while count < 13:
        times_table = count * user
        print(count,"x ",user,"= ", times_table)
        count += 1
else:
        count = 12
        while count >=0:
            times_table = count * user
            print(count, "x ", user, "= ", times_table)
            count -= 1
