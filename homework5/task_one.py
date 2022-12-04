code_opr_mts = {'291': 'МТС', '292': 'МТС', '293': 'МТС', '295': 'МТС',
                '296': 'МТС', '297': 'МТС', '298': 'МТС', '299': 'МТС',
                '33': 'МТС', '44': 'A1', '25': 'life', '29': 'МТС'}

code_opr_othr = {'33': 'МТС', '44': 'A1', '25': 'life'}

while True:
    result = {}
    error = False
    phone_number = input('Введите номер телефона: ')

    if len(phone_number) != 13:
        result['success'] = False
        result['description'] = "Number should contains only 13 symbols"
        error = True

    for char in phone_number[1:12]:
        if not char.isdigit():
            result['success'] = False
            result['description'] = "Number should contains only integers"
            error = True
            break

    if ("+") not in phone_number[0]:
        result['success'] = False
        result['description'] = "Number should start with a plus sign"
        error = True

    if len(phone_number) != 13:
        result['success'] = False
        result['description'] = "Number should contains only 13 symbols"
        error = True

    if phone_number[1:4] != ('375'):
        result['success'] = False
        result['description'] = 'Unknown country. Please try again'
        error = True
    if error:
        print(result)
    else:
        result['success'] = True
        result['phone'] = phone_number
        result['code_opr'] = code_opr_mts[phone_number[4:6]]
        print(result)

    exit_choice = input('Хотите проверить еще один номер (Y/N): ')
    if exit_choice == 'N':
        break
