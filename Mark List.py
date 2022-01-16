
# Print the Name of 2nd Lowest Grade in Alphabetical Order:


if __name__ == '__main__':
    Mark_Sheet = {}
    Strength = int(input("Enter the total No. of students: "))
    for N in range(Strength):
        name = input("Name of the Student: ")
        score = float(input("Marks Scored: "))
        
        Mark_Sheet[name]=score

    print(Mark_Sheet)
        
    Marks = []
    for x, y in Mark_Sheet.items():

        Marks.append(y)

    minimum = min(Marks)
    sec = max(Marks)

    for a in Marks:

        if a > minimum or a <= sec:

            sec = a

    print(sec)

    Name_List = []

    for a in Mark_Sheet:

        if Mark_Sheet[a] == sec:

            Name_List.append(a)


    Name_List.sort()

    for a in Name_List:

        print(a)





    