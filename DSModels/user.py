class User: #mother class for all users(boss, employees and customers)
    
    def __init__(self, firstName, lastName, userName, password, nationalCode, address, accessLevel):
        self.firstName = firstName #str
        self.lastName = lastName #str
        self.userName = userName #str
        self.password = password #str
        self.nationalCode = nationalCode #int
        self.address = address #str
        self.accessLevel = accessLevel #int
