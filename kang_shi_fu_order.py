# asks for a kong shi fu order
# ian from ming dynasty
# 2/11/2023

total = 100.00
red_tea = input("would you like a bottle of red tea? If you don't I'll report u to the police: ").strip(".,?!")
if red_tea == "yes":
    total += 200.00
else: print("119")
instant_noodles = input("would you like instant noodles? If you don't I'll report u to the police: ").strip(".,?!")
if instant_noodles == "yes":
    total += 300.00
else: print("119")
print("your total is " + str(round(total, 2)) + "RMB")