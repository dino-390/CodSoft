import random

loop = False
while not loop:
    user = str(input("Rock , Paper , Scissors or Quit : ")).capitalize()
    cpu = random.randint(1,3)

    if cpu == 1:
        cpu = "Rock"
    elif cpu == 2:
        cpu = "Paper"
    elif cpu == 3:
        cpu = "Scissors"
    print("Cpu: ", cpu)

    if(user == cpu):
        print("It's a tie")
    elif(user == "Rock" and cpu == "Scissors") or (user == "Paper" and cpu == "Rock") or (user == "Scissors" and cpu == "Paper"):
        print("You win!")
    elif(cpu == "Rock" and user == "Scissors") or (cpu == "Paper" and user == "Rock") or (cpu == "Scissors" and user == "Paper"):
        print("cpu wins")
    elif(user == "Quit"):
        loop = True
    else:
        print("Invalid input")

