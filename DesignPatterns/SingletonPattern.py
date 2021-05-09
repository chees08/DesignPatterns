class sPatternMeta(type):
   
    #Singleton Pattern (sPattern) with metaclass
   
    _samples = {}

    def __call__(cls, *args, **kwargs):
      
        if cls not in cls._samples:
            sample = super().__call__(*args, **kwargs)
            cls._samples[cls] = sample
        return cls._samples[cls]


class sPattern(metaclass=sPatternMeta):
    def variable(self):
        ''

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

#Client
if __name__ == "__main__":

    s1 = sPattern()
    s2 = sPattern()

    if id(s1) == id(s2):
        print(bcolors.OKGREEN + 'Works, all variables has same samples.' + bcolors.ENDC)
    else:
        print(bcolors.WARNING + 'Fail, variables has different samples.' + bcolors.ENDC)
