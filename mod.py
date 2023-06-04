# import module1 as md
# print(md.diction)
# output:{'company_name': 'techArt', 'computer_users': {'paterson', 'edward', 'kate'}, 'login_password': 'TECHART39402@'}
# print(md.diction["computer_users"])
# output:{'kate', 'edward', 'paterson'}

# IMPORT FROM MODULE:
from module1 import diction
print(diction["login_password"])
# OR:
from module1 import*
print(diction["login_password"])
# output:TECHART39402@