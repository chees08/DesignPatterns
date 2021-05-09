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


class DataB(object):
    services = {
                 'like': {'total': 1000, 'price': 2,},
                 'comment': {'total': 500, 'price': 10,},
                 'follower': {'total': 1000, 'price': 15,},
                 }

class Fake(object):
    def list_services(self, services):
        for insta in services:
            print(insta, ' ')
    
    def list_pricing(self, services):
        for insta in services:
            print(bcolors.WARNING + "For" , DataB.services[insta]['total'],insta + bcolors.ENDC, 
                                          "on instagram you pay $",DataB.services[insta]['price'])

class Controller(object):
    def __init__(self):
        self.DataB = DataB()
        self.Fake = Fake()
    
    def get_services(self):
        services = self.DataB.services.keys()
        return(self.Fake.list_services(services))

    def get_pricing(self):
        services = self.DataB.services.keys()
        return(self.Fake.list_pricing(services))
    
#client
class Client(object):
    controller = Controller()
    print(bcolors.OKCYAN + 'Service Offers:' + bcolors.ENDC)
    controller.get_services()
    print(bcolors.OKCYAN + 'Pricing for Services:' + bcolors.ENDC)
    controller.get_pricing()
    
if __name__ == '__main__':
    
    c = Client()