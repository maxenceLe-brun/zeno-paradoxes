def test2():
	total = 8
	travel = 8
	actual = 0
	turn = 0
	while True:
		sleep(.1)
		turn += 1
		actual += travel/2
		travel /= 2
		print("turn n"+str(turn)+"\nactuel : " + str(actual) + "\nrestant :" + str(travel) + "\npourcentage rapport total :" + str(actual / total * 100) +"%\n")
test2()
