a = [5, -6, 7]

streak = 0
current_best = 0

for number in a:
	if number < 0:
		current_best = max(streak, current_best)
		streak = 0
		continue
	streak += number
	
current_best = max(streak, current_best)

print(current_best)
