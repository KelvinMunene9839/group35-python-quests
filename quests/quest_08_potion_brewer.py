# Quest 8: The Potion Brewer
# Concept: Basic Arithmetic Operators (+, -, *, /)
# We use * to calculate cost per item and + to get the total.

# Define the quantity and price of each ingredient
dragon_scales = 3       # Number of dragon scales needed
scale_price = 10        # Cost of one dragon scale in gold

elf_tears = 5           # Number of elf tears needed
tear_price = 3          # Cost of one elf tear in gold

# Calculate the cost of each ingredient using multiplication
cost_of_scales = dragon_scales * scale_price   # 3 x 10 = 30
cost_of_tears = elf_tears * tear_price         # 5 x 3 = 15

# Add both costs together to get the total
total_cost = cost_of_scales + cost_of_tears    # 30 + 15 = 45

# Display a clear breakdown of the costs
print("=== Potion Ingredients Bill ===")
print(f"Dragon Scales : {dragon_scales} x {scale_price} gold = {cost_of_scales} gold")
print(f"Elf Tears     : {elf_tears} x {tear_price} gold = {cost_of_tears} gold")
print(f"Total Cost    : {total_cost} gold")
