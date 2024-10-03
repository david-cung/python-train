import module

def getUser():
    checkLogin = module.login()
    if checkLogin == 'login successfully':
        print('User logged in successfully')
    print('Get list user successfully')