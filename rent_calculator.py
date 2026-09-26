print("|==========================================================|\n")
print("|======================RENT CALCULATOR=====================|\n")
print("|==========================================================|\n")

# here we are taking inputs for different expenxes
rent=int(input("| Input your rent : "))
electricity_unit=int(input("| Input your Electricity Unit : "))
food_bill=int(input("| Input your food bill : "))
other=int(input("| Input your other expences : "))
electric_per_unit=int(input("| Input your electric charge per unit : "))

#total elecric bill calculater through unit*charge per unit
total_Electric_bill=electricity_unit * electric_per_unit

#total rent by adding all the expences
total_rent = rent+food_bill+other+total_Electric_bill

print("|==========================================================|\n")
print(f"|Your rent is {rent}\n")
print(f"|Your Eectricity bill is {total_Electric_bill}\n")
print(f"|Your food expences is {food_bill}\n")
print(f"|Your other expences is {other}\n")
print(f"|Your total calculated rent is {total_rent}\n")
print("|==========================================================|\n")