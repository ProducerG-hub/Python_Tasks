# creating a program that will loop the numbers in the list and then , give the sum, min and max
# NB: not using the built in functions sum(), min() and max()

marks = [1,2,3]
total = 0

if not marks:
    print("List is Empty")

else:
    min_num = marks[0]
    max_num = marks[0]

    for i in marks:
        #calculating sum
        total += i #(total = total + i)

        #determining the minimum number
        if i<min_num:
            min_num = i

        #determining the maximum number
        if i>max_num:
            max_num = i

    print(f"""
    Sum:{total}
    Minimum_Number:{min_num}
    Maximum_Number:{max_num}
    """)

    #prepared by mlue_tech