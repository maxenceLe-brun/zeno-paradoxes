def test1():
	n = 100000.0
	rest = 100000.0
	Turtle = 0.0
	Human = 0.0
	turn = 0
	while True:
		sleep(0.1)
		turn += 1
		Human = Turtle
		rest /= 2
		Turtle += rest
		print("turn n"+str(turn)+"\ndistance Tortue : "+str(Turtle)+"\ndistance humain : "+str(Human)+"\ndistance restant : " + str(rest) + "\n")
test1()
