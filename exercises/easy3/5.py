def triangle(num):
    # for each iterator from 1 to num,
    # print (num - iterator) spaces, followed by iterator *
    for idx in range(num + 1):
        print(((num - idx) * " ") + ("*" * idx))

triangle(5)
triangle(9)
    # if num = 3
    #print 2 spaces and 1 * at the end of the row
    #print 1 space and 2 * at the end of the row
    # print 0 space and 3 * at the end of the row
