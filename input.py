INPUT:you are able to ask the user for input.
names = input("ENTER YOUR NAME: ")
print(f'{names},this is your fist input.')
# output:
# ENTER YOUR NAME: alison
# alison,this is your fist input.
ls = []
names = input("ENTER YOUR NAME: ")
for num in range(3):
    scores = float(input('enter your scores: '))
    ls.append(scores)
print(f'{names},your score is : {ls}')
# output:
# ENTER YOUR NAME: jack
# enter your scores: 78
# enter your scores: 90
# enter your scores: 56
# jack,your score is : [78.0, 90.0, 56.0]
