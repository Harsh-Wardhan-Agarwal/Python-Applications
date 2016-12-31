def display():
	print(a[0]," |",a[1]," |",a[2])
	print("----------------")
	print(a[3]," |",a[4]," |",a[5])
	print("----------------")
	print(a[6]," |",a[7]," |",a[8])
	print("\n")
	return

def rules():
	result = ''
	if a[0]=='o' and a[4]=='o' and a[8]=='o' or a[2]=='o' and a[4]=='o' and a[6]=='o' or a[1]=='o' and a[4]=='o' and a[7]=='o' or a[3]=='o' and a[4]=='o' and a[5]=='o' or a[0]=='o' and a[3]=='o' and a[6]=='o' or a[0]=='o' and a[1]=='o' and a[2]=='o' or a[2]=='o' and a[5]=='o' and a[8]=='o' or a[6]=='o' and a[7]=='o' and a[8]=='o':
		result = 'o'
		return result
	elif a[0]=='x' and a[4]=='x' and a[8]=='x' or a[2]=='x' and a[4]=='x' and a[6]=='x' or a[1]=='x' and a[4]=='x' and a[7]=='x' or a[3]=='x' and a[4]=='x' and a[5]=='x' or a[0]=='x' and a[3]=='x' and a[6]=='x' or a[0]=='x' and a[1]=='x' and a[2]=='x' or a[2]=='x' and a[5]=='x' and a[8]=='x' or a[6]=='x' and a[7]=='x' and a[8]=='x':
		result = 'x'
		return result
	else:
		return result

def play_for_o():
	rules_return = ''
	input_o = int(input('o index:'))
	if input_o>=0 and input_o<9:
		if a[input_o] == "":
			a[input_o] = 'o'
			display()
			rules_return = rules()
		else:
			print('enter at an empty space')
			play_for_o()
	else:
		print('enter a valid input')
		play_for_o()
	return rules_return

def play_for_x():
	rules_return = ''
	input_x = int(input('x index:'))
	if input_x>=0 and input_x<9:
		if a[input_x] == "":
			a[input_x] = 'x'
			display()
			rules_return = rules()
		else:
			print('enter at an empty space')
			play_for_x()
	else:
		print('enter a valid input')
		play_for_x()
	return rules_return
	
def check(ans):
	if ans == 'o' or ans == 'x':
		return 1

a = []
for i in range(0,9):
		a.append('')

def tictactoe():
	for i in range(0,9):
		a[i] = ""
	display()
	print('Lets Play TIC - TAC -TOE!!')

	count = 0
	while count != 9:

		ans = play_for_o()
		count+=1
		if count == 9 :
			print ("MATCH DRAW")
			break
		if ans != '':
			check_return = check(ans)
			if check_return == 1:
				print(ans, "WINS!!!")
				break

		ans = play_for_x()
		count+=1
		if count == 9 :
			print ("MATCH DRAW")
			break
		if ans != '':
			check_return = check(ans)
			if check_return == 1:
				print(ans, "WINS!!!")
				break

	again = int(input("Play again (0/1):"))
	if again == 1:
		tictactoe()
	else:
		exit()

tictactoe()
