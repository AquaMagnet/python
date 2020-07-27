def reverse(input=''):
    output = ''
    for c in input:
      print("ITEM:" + c)
      print(output)
      output = c + output
    print(output)

reverse('cool')