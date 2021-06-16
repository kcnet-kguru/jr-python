from timeit import timeit

setup = 'from datetime import datetime'
statement = 'datetime.now()'
result = timeit(setup=setup, stmt=statement, number=1000)
print(f'Took an average of {result / 1000}s or {result}ms')

list_setup = 'import list_test'
list_stmt = 'list_test.get()'
list_result = timeit(setup=list_setup, stmt=list_stmt, number=10000)
print(f'List average of {list_result / 1000}s')

set_setup = 'import set_test'
set_stmt = 'set_test.get()'
set_result = timeit(setup=set_setup, stmt=set_stmt, number=10000)
print(f'Set average of {set_result / 1000}s')

