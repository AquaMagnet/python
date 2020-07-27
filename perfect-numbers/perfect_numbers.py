def classify(number):
    """
    Determine if the number is a perfect, abundant, or deficient number
    using the aliquot sum of its factors not including the number itself:
    
    perfect if the number is equal to the aliquot sum
    abundant if the number is greater than the aliquot sum
    deficient if the number is less than the aliquot sum
    """
    if number <= 0:
        raise ValueError('Place a number greater than 0')
    
    aliquot = sum(set(factors for values in range(1, int(number**0.5)+1)
              for factors in (values, number//values)
              if number%values == 0)) - number
            
    if aliquot == number:
        return 'perfect'
    elif aliquot > number:
        return 'abundant'
    else:
        return 'deficient'

