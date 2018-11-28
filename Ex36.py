from sys import exit
goggles = False
flashlight = False
axe = False
rope = False
def forest():
	print "You approach the forest apprehensively."
	print "You spot a great tree golem rummaging in the bushes, it seems to be looking for something."
	print "The golem appears to be hiding his face from the sun."
	print "There is a vulnerable tree branch to the right of the golem."
	print "Do you wish to approach the golem? (Yes- 'Y' or Map- 'M')"
	answer = raw_input("> ")
	if answer.lower() == "y":
		forest2()
	elif answer.lower() == "m":
		map()
	else:
		"Not a viable option."
		forest()
def forest2():
	if goggles == True:	
		print "The golem notices your goggles and fucks you up for them. You are dead."
		dead()
	elif flashlight == True:
		print "The golem is blinded by the flashlight, you take it's treasure."
	elif axe == True:
		print "You cut down the branch and it pins the golem to the ground. You take it's treasure."
	elif rope == True:
		print "The rope is no value to you against the golem. Returning to map."
		map2()
	else:
		print "I suggest talking to Jax before approaching the golem."
		print "He may have an item of use to you."
		jax()
def pond():
	print "The pond is teaming with piranhas."
def cave():
	print "Darkness consumes you."
def sands():
	print "The suns rays begin to strengthn."
def jax():
	print "Welcome Stork, here are my wares. (You may only take one item at a time)"
	print "Goggles- 'G'\nFlashlight- 'F'\nAxe- 'A'\nRope- 'R'"
	print "Go back to map- 'M'"
	answer = raw_input()
	if answer.lower() == "g":
		goggles = True
		print "You are now wearing goggles."
		map2()
	elif answer.lower() == "f":
		flashlight = True
		print "You strap the flashlight to your belt."
		map2()
	elif answer.lower() == "a":
		axe = True
		print "You take the axe."
		map2()
	elif answer.lower() == "r":
		rope = True
		print "You tie the rope to your belt."
		map2()
	elif answer.lower() == "m":
		map2()
	else:
		print "Not a viable option."
		jax()
def map():
	print "Opening map:"
	print "Travel north through the 'Forest of doom' by pressing 'F'."
	print "Travel east to the 'Pond of sorrows' by pressing 'P'."
	print "Travel south into the 'Cave of despair' by pressing 'C'."
	print "Travel west across the 'Sands of time' by pressing 'S'."
	print "Speak to Jax:'J'"
	answer = raw_input()
	if answer.lower() == "f":
		forest()
	elif answer.lower() == "p":
		pond()
	elif answer.lower() == "c":
		cave()
	elif answer.lower() == "s":
		sands()
	elif answer.lower() == "j":
		jax()
	else:
		print "Not a viable option."
		map2()
def map2():
	print "Where to?"
	print "Forest- 'F'\nPond- 'P'\nCave- 'C'\nSands- 'S'\nJax- 'J'"
	answer = raw_input()
	if answer.lower() == "f":
		forest()
	elif answer.lower() == "p":
		pond()
	elif answer.lower() == "c":
		cave()
	elif answer.lower() == "s":
		sands()
	elif answer.lower() == "j":
		jax()
	else:
		print "Can't do that here."
		map2()
def start(): 
	print "Welcome to the adventures of Stork!"
	print 'If you would like to start exploring immediately press \'M\'\nalternatively, speak to Jax the vendor by pressing \'J\'.'
	
	answer = raw_input("M or J? \n> ")
	
	if answer.lower() == "m":
		map()
	elif answer.lower() == "j":
		jax()
	else:
		print "I do not understand."
		start()
		
def dead():
	print "Better luck next time Stork!"
	exit(0)
start()