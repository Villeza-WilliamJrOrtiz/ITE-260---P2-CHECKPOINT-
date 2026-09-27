student = int(input("How many student?: "))

def activity(s1, s2, s3):
  return(s1+s2+s3)/3
  

while student <3:
  print("The program must process at least 3 students.")


for student in range(1, student + 1):
  print("student", student)
  name = input("Enter student name: ")
  
  
  a1 =float(input("Activity 1 score:  "))
  a2 =float(input("Activity 2 score:  "))
  a3 =float(input("Activity 3 score:  "))

  average = activity(a1, a2, a3)

  if average >=90:
    status=("Excellent ")
  elif average >=80:
    status=("Very good ")
  elif average >=75:
    status=("Passed ")
  else:
    status=("failed ")


  print("-----Activity Result-----")

  print("Activity 1: ", a1)
  print("Activity 2: ", a2)
  print("Activity 3: ", a3)
  print("Average:", average)
  print("Status:", status)


  print("-----------------------")