
def main():
	#write your code here
	pass
	first_number = (input("Enter first number: "))
	second_number = (input("Enter second number: "))
	operations = input("Choose the operation (+,-,/,*): ")
	if first_number.isnumeric() == False or second_number.isnumeric() == False:
		print("numbers are invalid")
	else:
		if operations == "*":
			print("The answer is " + str(int(first_number) * int(second_number)))
		elif operations == "+":
			print("The answer is " + str(int(first_number) + int(second_number)))
		elif operations == "-":
			print("The answer is " + str(int(first_number) - int(second_number)))
		elif operations == "/":
			print("The answer is " + str(int(first_number) // int(second_number)))
		else:
			print("operation is invalid")



if __name__ == '__main__':
	main()
