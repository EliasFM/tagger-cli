class c:
    def __init__(self):
        self.HEADER = '\033[95m'
        self.OKBLUE = '\033[94m'
        self.OKGREEN = '\033[92m'
        self.WARNING = '\033[93m'
        self.FAIL = '\033[91m'
        self.ENDC = '\033[0m'
        self.BOLD = '\033[1m'
        self.UNDERLINE = '\033[4m'

    def printHeader(self, str):
        return self.HEADER + str + self.ENDC

    def printBlue(self, str):
        return self.OKBLUE + str + self.ENDC

    def printGreen(self, str):
        return self.OKGREEN + str + self.ENDC

    def printWarn(self, str):
        return self.WARNING + str + self.ENDC

    def printFail(self, str):
        return self.FAIL + str + self.ENDC

    def printBold(self, str):
        return self.BOLD + str + self.ENDC

    def printUnderline(self, str):
        return self.UNDERLINE + str + self.ENDC
