h = 183
w = 72
s = 15250
t = 55
def L1Calc(h,w,s,t):
	return 0.035 * w + ((s/t)**2 / h) * 0.029 * w

print(L1Calc(h,w,s,t))
# 879.710082644628
