data = [
    {'name':'test',
     'pwd' :'test1',
     'money': 0},
]

class Account:
    tmp = {}
    def __init__(self, name, password, deposit=0):
        self.tmp['name'] = name
        self.tmp['pwd'] = password
        self.tmp['money'] = 0
        data.append(tmp)

def withdraw(name, password, money):
    for acc in data:
        if acc['name'] == str(name):
            if acc['password'] == str(password):
                acc['money'] -= money
                break
            else:
                print("Wrong Password")
                break
        else:
            print('No such account')
    print(f'New balance: {self.tmp["money"]}')
def deposit(name, money):
    for acc in data:
        if acc['name'] == str(name):
            if acc['password'] == str(password):
                acc['money'] += money
                break
        else:
            print('No such account')
    print(f'New balance: {self.tmp["money"]}')
    
def change_password(name, oldPass, newPass):
    for acc in data:
        if acc['name'] == str(name):
            if acc['password'] == str(password):
                acc['pwd'] == (newPass)
                print('Password Changed!')
                break
            else:
                print('Your old password is wrong.')
        else:
            print('No such account')