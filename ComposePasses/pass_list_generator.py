country_code = '+1'
operator_codes = ['484', '814', '585', '610']

with open('pass_list.txt', 'w') as result:
    for code in operator_codes:
        for i in map(lambda num: result.write(country_code + code + str(num).rjust(7,'0') +'\n'), range(0, 9999999, 1)):
            pass
