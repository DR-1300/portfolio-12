def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  if b == 0:
      return "cannot divide by zero"
  return a / b

def power(a, b):
  return a ** b

def menu():
  print("\nArithmetic Operations Menu:")
  print("1. Addition (+)")
  print("2. Subtraction (-)")
  print("3. Multiplication (×)")
  print("4. Division (÷)")
  print("5. Power (a^b)")
  print("6. Exit")

def get_input():
  while True:
      try:
          a = float(input("Enter first number: "))
          b = float(input("Enter second number: "))
          return a, b
      except ValueError:
          print(" enter valid numbers ")

def main():
  while True:
      menu()
      choice = input("Choose an option (1-6): ")

      if choice == '6':
          print(" Exiting ..")
          break

      if choice not in ['1', '2', '3', '4', '5']:
          print("Invalid choice. Please select a valid option.")
          continue

      a, b = get_input()

      if choice == '1':
          print(f"{a} + {b} = {add(a, b)}")
      elif choice == '2':
          print(f"{a} - {b} = {subtract(a, b)}")
      elif choice == '3':
          print(f"{a} × {b} = {multiply(a, b)}")
      elif choice == '4':
          print(f"{a} ÷ {b} = {divide(a, b)}")
      elif choice == '5':
          print(f"{a}^{b} = {power(a, b)}")

main()
