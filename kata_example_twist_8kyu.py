# This is an easy twist to the example kata (provided by Codewars when learning how to create your own kata).

# Add the value "codewars" to the array websites/Websites 1,000 times.


websites = []
count = 0
while count < 1000:
    websites.append('codewars')
    count += 1
print(len(websites))
