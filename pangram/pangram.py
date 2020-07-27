def is_pangram(sentence):
    letters = 'abcdefghijklnopqrstuvwxyz'
    status = True;
    for items in letters:
        if items in sentence.lower():
            status = status & True
        else:
            status = status & False
    return(status)
