# Quest 9: The Greedy Goblin
# Concept: Modulo Operator (%) - gives the remainder after division.

total_gold = 27
friends = 4

each_friend_gets = total_gold // friends   # // is integer (whole number) division
goblin_keeps = total_gold % friends        # % gives the leftover remainder

print(f"Each friend receives: {each_friend_gets} gold pieces")
print(f"The goblin keeps: {goblin_keeps} gold pieces")
