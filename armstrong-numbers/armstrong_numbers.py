def is_armstrong_number(number):

    number = str(number)
    armstrong = 0
    for item in number:
        armstrong += int(item)**len(number)

    return(armstrong == int(number))
    
