calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    string= str(string)
    a = (len(string),string.upper(),string.lower())
    count_calls()
    return a

def is_contains(string, list_to_search):
    count_calls()
    if string in list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)