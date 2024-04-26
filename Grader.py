grt = "Hello, Welcome to our Grader!"
print(grt)

print("To check results...")
name = str(input("Enter your Names: "))
mark = int(input("Enter your Mark: "))


if mark > 50:
    print("You got above average")

elif mark < 50:
    print("Sorry you've failed")

elif mark == 50:
    print("You got average!")

else:
    print("Please enter correct marks!")


