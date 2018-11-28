print "You enter a dark room with four doors. Do you go through door #1, door #2, door #3 or door #4?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."

	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
 
elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")
	
	if insanity == '1' or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
elif door == "3":
	print "A friendly wizard stands before you!\nChoose your reward my friend.(1, 2 or 3)"
	print "1. Gold"
	print "2. Women"
	print "3. Invisibility cloak"
	
	reward = raw_input("> ")
	
	if reward == "1":
		print "The wizard rewards you with all the gold in the world."
	elif reward == "2":
		print "The wizard rewards you with any woman you may choose."
	elif reward == "3":
		print "The wizard hands you nothing. Stitch up!"
	else:
		print "You have upset the wizard. He disappears."
elif door == "4":
	print "A hustler shows you two closed fists\nHow do you react?"
	print "1. Attempt to challenge him in arm to arm combat."
	print "2. Speak with him"
	
	answer = raw_input("> ")
	
	if answer == "1":
		print "The hustler is an expert in martial arts. He destroys you."
	elif answer == "2":
		print "There is one million dollars in one of my hands.\nRight, Left or Random?"
		
		hand = raw_input("> ")
		
		if hand == "Right":
			print "Correct! (Hands you one million dollars.)"
		elif hand == "Left":
			print "Incorrect! (He swings his left fist at you!)"
		elif hand == "Random":
			print "You headbutt the hustler knocking him unconscious!\n(You recieve one million dollars.)"
		else:
			print "Nothing happens"
	else:
		print "You turn into a frog"
else:
	print "You stumble around and fall on a knife and die. Good job!"