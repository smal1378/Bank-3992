class User: #mother class for all users(boss, employees and customers)
    
    def __init__(self, first_name, last_name, username, password, national_code, address, access_level):
        self.first_name = first_name #str
        self.last_name = last_name #str
        self.username = username #str
        self.password = password #str
        self.national_code = national_code #int
        self.address = address #str
        self.access_level = access_level #int
