
def main():
	#write your code here
	pass
	first_number = (input("Enter first number: "))
	second_number = (input("Enter second number: "))
	if first_number.isnumeric() == False or second_number.isnumeric() == False:
		print("numbers are invalid")
	operations = input("Choose the operation (+,-,/,*): ")
	if operations != "*" and operations != "+" and operations != "-" and operations != "/":
		print("operation is invalid")
	if operations == "*":
		print(float(first_number) * float(second_number))
	elif operations == "-":
		print(float(first_number) - float(second_number))
	elif operations	== "+":
		print(float(first_number) + float(second_number))
	elif operations == "/":
		print(float(first_number) / float(second_number))




if __name__ == '__main__':
	main()
