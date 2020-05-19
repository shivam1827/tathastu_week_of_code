CostPrice=float(input("Enter the cost price: "))
SellingPrice=float(input("Enter the selling price: "))
Profit=SellingPrice-CostPrice
IncreasedProfit=(1.05*(Profit)+CostPrice)
print("Profit is: ",Profit)
print("Profit increased by 5% is: ",IncreasedProfit)
