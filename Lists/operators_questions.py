# Question 1: Ask the user to enter their birth year, convert it to an integer, then calculate their age.
user_age = int(input("Enter your Year of Birth: "))
curent_year = 2026
age = curent_year - user_age

if user_age > curent_year:
    print("Year cannot be Greater than Current Year")
else:
    print(f"Hey You!, you are {age} Years Old.")
    

# Question 2: Create two variables x = 50 and y = 8.
#  Calculate addition, subtraction, multiplication, division, floor division, modulus, and power.
x, y = 50, 8
add = x+y
sub = x-y
mul = x*y
div = x/y
floor_div = x//y
mod = x % y
power = x**y

print(add)
print(sub)
print(mul)
print(div)
print(floor_div)
print(mod)
print(power)


# Question 3: A rectangle has a length of 25 and width of 12. Calculate its area.
length = 25
width = 12
area = length * width
print(area)


# Question 4: A laptop costs 850 USD. The exchange rate is 129. Calculate the price in Kenyan shillings.
usd_cost = 850
exchange_rate = 129
ksh_cost = usd_cost * exchange_rate
print(f"{ksh_cost:,} KSH")


# Question 5: A student scored 70, 85, 60, and 90 in four subjects. Calculate the total and average marks.
subs = [70, 85, 60, 90]
total_marks = sum(subs)
average_mark = total_marks / len(subs)
print(total_marks)
print(average_mark)


# Question 6: A shop sold an item for 2500 after buying it for 1800. Calculate the profit.
sp_cost = 2500
bp_cost = 1800
profit = sp_cost - bp_cost
print(profit)


# Question 7: A farmer harvested 250 mangoes. Each box holds 24 mangoes. Calculate the number of full boxes and remaining mangoes.
total_mangoes = 254
bucket_capacity = 24
full_boxes = total_mangoes // 24
remainders = total_mangoes % 24
print(full_boxes)
print(remainders)


# Question 8: A company made sales of 850000, paid expenses of 320000, and paid tax of 18% on profit. Calculate profit before tax, tax amount, and profit after tax.
sales = 850000
expenses = 320000
tax_rate = 0.18

# Profit Before Tax
profit = sales - expenses
print(profit)
# Tax Amount
tax_amount = (sales * .18)
print(tax_amount)

# Profit after Tax
profit_after_tax = (sales - tax_amount) - expenses
print(profit_after_tax)


# Question 9: An API provider gives 50,000 free requests. A company makes 350,000 requests. Each extra 1,000 requests costs $0.40. Calculate total cost in USD and KSh at an exchange rate of 129.
total_req = 350000
free_req = 50000
extra_req = 1000
extra_req_cost = 0.40
ksh_to_usd_rate = 129
usd_cost_incurred = (((total_req - free_req) * extra_req_cost)/extra_req)
ksh_cost_incurred = ksh_to_usd_rate * usd_cost_incurred
print(usd_cost_incurred)
print(ksh_cost_incurred)


# Question 10: A freelancer earned $2500. The exchange rate is 129, and Upwork charges a 10% service fee. Calculate the amount received in KSh after the fee.
usd_earnings = 2500
ksh_to_usd_rate = 129
service_fee_rate = 0.1
ksh_amount = (usd_earnings * .9) * ksh_to_usd_rate
print(f"Ksh {ksh_amount:,}")


# Question 11. You are given two lists. The first list contains the buying prices of BTC in USD, and the second list contains the selling prices of BTC in USD.
"""
Write a Python program that loops through both lists and counts:
 1. The number of profitable trades
 2. The number of loss-making trades
"""
btc_buy_prices_usd = [72000, 76000, 79000, 74000, 80000]
btc_sell_prices_usd = [75000, 78000, 77000, 81000, 83000]

profitable_trade = 0
loss_trade = 0
for price in range(len(btc_sell_prices_usd)):
    if btc_sell_prices_usd[price] > btc_buy_prices_usd[price]:
        profitable_trade += 1
    elif btc_sell_prices_usd[price] < btc_buy_prices_usd[price]:
        loss_trade += 1

print(f"No of Profitable Trades: {profitable_trade}")
print(f"No of Loss Trades: {loss_trade}")


# Question 12: Loop through the laptop prices and convert the prices to ksh
laptop_prices_usd = [500, 750, 1000, 1200, 1500]
usd_ksh_rate = 129

for price in laptop_prices_usd:
    print(f"{price * 129} Ksh")
