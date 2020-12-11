#Parent class Console
class Console:
    name ='system'
    user = ''
    price = ''
    supported_services = 'live gameplay'
    storage = '1 TB'
    feature = '4K Capable'
    connection = 'HDMI'
    password = 'gameon'

    def getLoginInfo(self):
        entry_user = input("Enter your name")
        entry_password = input("Enter your password")
        if(entry_user == self.user and entry_password == self.password):
            print("Enjoy your gaming experince, {}".format(entry_user))
        else:
            print("Incorrect login try again or click forgot password")

#Child Class PS5
class PS5(Console):
    vr_integration = True
    game_boost = True
    sessionID = ''

    def getLoginInfo(self):
        entry_user = input("Enter your name")
        entry_sessionID = input("Enter your sessionID")
        if(entry_user == self.user and entry_sessionID == self.sessionID):
            print("Be Moved, {}".format(entry_user))
        else:
            print("We do not recongize login info try again")

#Child Class XBOX
class XBOX(Console):
    iphone_streaming = True
    backwards_compatibility = False
    ipcheck = ''

    def getLoginInfo(self):
        (self):entry_user = input("Enter your name")
        entry_ipcheck = input("scan ip")
        if(entry_user == self.user and entry_ipcheck == self.ipcheck):
            print("Welcome to the worlds most powerful console experince, {}".format(entry_user))
        else:
            print("ipcheck failed please check connection ")

    
    
    
    
gammer = Console()
gammer.getLoginInfo()
    
    
    
