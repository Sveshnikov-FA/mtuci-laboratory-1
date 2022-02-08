HEIGHT = 183
WEIGHT = 72
STEPS = 15250
TIME = 55
def L1Calc(h,w,s,t):
	return 0.035 * w + ((s/t)**2 / h) * 0.029 * w

print(f"Калорий сожжено: {L1Calc(HEIGHT,WEIGHT,STEPS,TIME)}\nПройденная дистанция: {STEPS/TIME}")

# Калорий сожжено: 879.71
# Пройденная дистанция: 277.27
