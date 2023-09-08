def test3():
	cible  = random.randrange(10,1001)
	speed  = 5
	actual = 0
	turn   = 0
	while actual < cible:
		sleep(0.005)
		actual += speed
		turn += 1
		print("tour n"+str(turn)+";\ndistance actuel : "+str(actual)+";\ndistance restante : "+str(cible - actual)+";\n")
test3()
