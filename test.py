from DS import *
core = Core()
core.set_admin('hamed', '3333')
core.create_customer('hamed', 'saraji', 'hamed',
                     '2222', 'asfjasf', 'as;dfjjasdlf')
core.create_employee('ali', 'rezaei', 'ali', '1111',
                     'adfads', 'adfladf', 2000000)
core.create_account('hamed')
core.create_manager('ali', 'rezaei', 'ali', '1111',
                    'adfads', 'adfladf', 2000000)
core.create_branch('branche', 'adlfkjalddfjasfd')
print(core.search_user('ali', 'customers'))
print(core.users)
