total_heights = 0
total_length = 0
student_heights = input("Input a list of students height ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    total_heights = student_heights[n] + total_heights
    total_length = n+1
average = total_heights/total_length
print(average)
