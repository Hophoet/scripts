import re
pattern = '^[rR]etrait[\s-]([0-9]{8})[\s-]{1}([\d]{2,})$'
test_string = 'Retrait 99898899 400'
result = re.match(pattern, test_string)
if result:
    number = result.group(1)
    amount = result.group(2)
    print("Valid format.")
    print('Nubmer', number)
    print('Amount', amount)
else:
  print("Invalid format.")	
