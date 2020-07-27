RAINDROPS = ((3,'Pling'),(5,'Plang'),(7,'Plong'))


def convert(number):
    """A function that converts number into a string that contains
    raindrop sounds. The function will return the following:
    
    Pling if the number is a factor of 3
    Plang if the number is a factor of 5
    Plong if the number is a factor of 7
    """
 
    output = ''.join(word for item, word in RAINDROPS if not number % item) 
    return output if output else str(number)


