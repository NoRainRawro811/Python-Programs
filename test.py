grades = []

print("STUDENT GRADE CALCULATOR")

while True:
    print("\n1 Add grade\n2 Show report\n3 Quit")
    c = input("Choice: ")

    if c == '1':
        g = input("Grade (0-100)")
        if g.isdigit() and 0 <= int(g) <= 100:
            grades.append(int(g))
            print("Grade Added")
        else:
            print("Error")
    elif c == '2':
        if not grades:
            print("Error")
            continue
        avg = sum(grades) / len(grades)
        letter = 'FDCBA'[(avg >= 60) + (avg >= 70) + (avg >= 80) + (avg >= 90)]
        print("\nGrades", grades)
        print("Average", round(avg, 1))
        print("Letter", letter)
        print("High", max(grades), "Low", min(grades))
    elif c == '3':
        print("Bye")
        break
    else:
        print("1, 2, or 3.")
    