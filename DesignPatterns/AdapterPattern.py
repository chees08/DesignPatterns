# FOR COLORFUL PRINT
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#source interface

class EuropeanServer(object):
    
    def electricity(self):
        pass
    def pc(self):
        pass
    def MineCraft(self):
        pass
    def desktop(self):
        pass

# Target interface
class USAServer(object):
    def electricity(self):
        pass
    def pc(self):
        pass
    def MineCraft(self):
        pass

# Adaptee
class EuropeanS(EuropeanServer):
    def electricity(self):
        return 230
    def pc(self):
        return 1
    def MineCraft(self):
        return -1 

# client
class USAMinecraft(object):
    __power = None
    
    def __init__(self, power):
        self.__power = power
    
    def run(self):
        if self.__power.electricity() > 144:
            print(bcolors.OKGREEN + 'Electricity is ON' + bcolors.ENDC)
        else:
               if self.__power.pc() == 1 and self.__power.MineCraft() == -1:
                print(bcolors.OKBLUE + 'MineCraft is Ready To PLAY' + bcolors.ENDC)

               else:
                print(bcolors.WARNING + 'MineCraft is NOT Ready To PLAY' + bcolors.ENDC)

# Adapter
class Server(USAServer):
    __server = None
    
    def __init__(self, server):
        self.__server = server
    
    def electricity(self):
        return 144
    
    def pc(self):
        return self.__server.pc()
    
    def MineCraft(self):
        return self.__server.MineCraft()

if __name__ == '__main__':
    Eserver = EuropeanS()
    Sgame = USAMinecraft(Eserver)
    Sgame.run()
    
    Sgame2 = USAMinecraft(Server(Eserver))
    Sgame2.run()