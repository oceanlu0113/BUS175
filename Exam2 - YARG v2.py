# given
items = []
discounts = {"lipstick": .05, "eye": .03, "annual sale": .20, "skincare": .05}

def calculate_tax(total):
  # return total and tax
  return (total*1.15)

def calculate_discount(items):
  # iterate each item
  for row in range(len(items)):
    # new cost = cost * (1-discount(if found))
    items[row][2] = items[row][2] * (1-(if_discount(items[row][0])))

def calculate_total(items):
  # define total
  total = 0
  # iterate each item
  for row in range(len(items)):
    # new total = total of all items
    total = total + float(items[row][2])
  # return so can find in respects to tax
  return total

def if_discount(item_name):
  # define discount
  discount = 0
  # iterate each key in dictionary
  for key in discounts:
    # if key is in the item name
    if key in item_name:
      # return discount respective to the key
      discount = discounts[key]
    # return the first discounted value
    if discount!=0:
      break
  # return the discount value in relation to key
  return discount;

def print_receipt(items):
  # iterate each item
  for row in range(len(items)):
    # item  amount:cost
    print(items[row][0],"    ", items[row][1],": %.2f" %items[row][2])
  # print separator
  print ("--------------------------------------------------")

def main(): 
  while True:
    # ask the user to enter an item to buy (string)
    item = input("Item to buy: ")
    # ask the user to enter cost (float)
    cost = float(input("Item cost: "))
    # ask the user to enter amount bought (int)
    amount = int(input("Amount to buy: "))

    # add the items to the list, this becomes 2d list
    items.append([item, amount, (amount*cost)])

    # keep asking unless user enters other than yes
    end = input("Buy another item? (y/n): ")
    if end!="y":
      break

# call main method to gather items, cost, amounts
main()
# find the discounts, overwrite costs
calculate_discount(items)
# print out item with amount * discounted costs
print_receipt(items)
# define subtotal
subtotal = float(calculate_total(items))
# print subtotal
print ("Subtotal: %.2f" %subtotal)
# print total after tax respective to subtotal
print ("Total after tax: %.2f" %calculate_tax(subtotal))