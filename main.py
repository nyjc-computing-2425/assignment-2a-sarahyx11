num = input('Enter a number (decimal or integer): ')
# type your code here
clean = num.strip()
clean = clean.replace(".","")
sf = len(clean.lstrip("0"))

 
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
