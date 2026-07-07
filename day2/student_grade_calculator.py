print("=" * 40)
print("Student Record Generator")
print("=" * 40)

name = input("Enter Student Name: ")
roll_number = input("Enter Roll Number: ")

print("\n--- Enter Marks for 5 Subjects (out of 100) ---")
sub1 = float(input("Subject 1: "))
sub2 = float(input("Subject 2: "))
sub3 = float(input("Subject 3: "))
sub4 = float(input("Subject 4: "))
sub5 = float(input("Subject 5: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) * 100

#Grade,GPA, and Pass/Fail Status based on percentage
if percentage >= 90:
    grade = "A+"
    gpa = 4.0
    status = "Pass"
elif percentage >= 80:
    grade = "A"
    gpa = 3.7
    status = "Pass"
elif percentage >= 70:
    grade = "B"
    gpa = 3.0
    status = "Pass"
elif percentage >= 60:
    grade = "C"
    gpa = 2.0
    status = "Pass"
else:
    grade = "F"
    gpa = 0.0
    status = "Fail"

#Final Report Card
print("\n" + "=" * 40)
print("FINAL REPORT CARD")
print("=" * 40)
print(f"Name:         {name}")
print(f"Roll Number:  {roll_number}")
print("-" * 40)
print(f"Total Marks:  {total_marks:.2f} / 500.00")
print(f"Percentage:   {percentage:.2f}%")
print(f"Grade:        {grade}")
print(f"GPA:          {gpa}")
print(f"Status:       {status}")
print("=" * 40)
