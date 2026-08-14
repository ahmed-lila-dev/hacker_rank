if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    scores = sorted(set(student[1] for student in students))
    second = scores[1]
    x = sorted([student[0] for student in students if student[1] == second])
    for name in x:
        print(name)
