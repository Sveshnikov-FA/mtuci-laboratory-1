HEIGHT = 183
WEIGHT = 72
STEPS = 15250
TIME = 55
def CaloriesCalc(h,w,s,t):
	return 0.035 * w + ((s/t)**2 / h) * 0.029 * w

def DistanceCalc(h,s):
	return (((h/4 + 0.37) * s)/100)/1000

#print(f"Калорий сожжено: {CaloriesCalc(HEIGHT,WEIGHT,STEPS,TIME)}")

# Калорий сожжено: 879.71

print(f"Дистанция в км: {DistanceCalc(HEIGHT,STEPS)}")
# Дистанция в км: 7.03