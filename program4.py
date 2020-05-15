cost_price=int(input("Enter Cost Price: "))
selling_price=int(input("Enter Selling Price: "))

profit=selling_price-cost_price
print("The Profit from sell is",profit)

new_price=1.05*profit+cost_price
print("Selling price at 5% profit is", new_price)