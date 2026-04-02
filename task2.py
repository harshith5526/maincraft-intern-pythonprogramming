import csv
import os
FILE_NAME="expenses.csv"

def initialize_file():
	if not os.path.exists(FILE_NAME):
		with open(FILE_NAME,"w",newline="") as file:
			writer=csv.writer(file)
			writer.writerow(["Description","Amount"])

def add_expense():
	desc=input("enter description:")
	amount=input("enter amonut:")
	with open(FILE_NAME,"a",newline="") as file:
		writer=csv.writer(file)
		writer.writerow([desc,amount])
	print("expense added successfully!\n")

def view_expense():
	with open(FILE_NAME,"r") as file:
		reader=csv.reader(file)
		for row in reader:
			print(row)

def total_expense():
	total=0
	with open(FILE_NAME,"r") as file:
		reader=csv.reader(file)
		next(reader)
		for row in reader:
                     try:
                        total+=float(row[1])
                     except:
                        continue
	print("total expense:",total,"\n")

def main():
   initialize_file()
   while True:
         print("1.add expense")
         print("2.view expense")
         print("3.total expense")
         print("4.exit")
         choice=input("enter choice:")
         if choice=="1":
            add_expense()
         elif choice=="2":
            view_expense() 
         elif choice=="3":
            total_expense()
         elif choice=="4":
            print("exiting")
            break 
         else:
            print("invalid choice!\n")
main()
