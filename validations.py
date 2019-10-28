def validate_add_params(params):
    """
    Validates the needed params for add function
    Raises ValueError for invalid parameters
    :param params: list of params
    :return:list of useful params
    """
    # no need to try/except int() because of regex parsing
    apartment = params[0]
    if apartment == '':
        raise ValueError('apartment')
    else:
        apartment = int(apartment)
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')
    type = params[1]
    if type not in types:
        raise ValueError('type')

    amount = params[2]
    if amount == '':
        raise ValueError('amount')
    else:
        amount = int(amount)

    return apartment, type, amount


def validate_remove_params(params):
    """
    Validates the needed params for remove function
    Raises ValueError for invalid parameters
    :param params: list of params
    :return:list of useful params
    """
    if params[0] is not '' and params[4] == 'to' and params[2] is not '':
        start_apart = int(params[0])
        end_apart = int(params[2])
        if start_apart > end_apart:
            return end_apart, start_apart
        else:
            return start_apart, end_apart
    elif params[0] is not '' and params[1] is '' and params[2] is '' and params[3] is None and params[4] is None:
        apartment1 = int(params[0])
        returnable = [apartment1]
        return tuple(returnable)
    elif params[0] is '' and params[1] is not '' and params[2] is '' and params[3] is None and params[4] is None:
        type = params[1]
        types = ['water',
                 'heating',
                 'electricity',
                 'gas',
                 'other']
        if type in types:
            return tuple([type])
        else:
            raise ValueError('type!')
    else:
        raise ValueError('parameters!')


def validate_replace_params(params):
    """
    Validates the needed params
    Raises ValueError for invalid parameters
    :param params: list of params
    :return:list of useful params
    """
    apartment = params[0]
    if apartment == '':
        raise ValueError('apartment')
    else:
        apartment = int(apartment)

    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')
    type = params[1]
    if type not in types:
        raise ValueError('type')

    amount = params[2]
    if amount == '':
        raise ValueError('amount')
    else:
        amount = int(amount)

    return apartment, type, amount


def validate_display_params(params):
    '''
    Validates the needed params for display function
    Raises ValueError for invalid parameters
    :param params: list of params
    :return:list of useful params
    '''

    if params[0] is not '' and params[1] in ['<', '>', '=', '>=', '<=']:
        amount = int(params[0])
        sign = params[1]
        return amount, sign
    elif params[0] is not '' and params[1] is '' and params[2] is '' and params[3] is None and params[4] is None:
        apartment = int(params[0])
        returnable = [apartment]
        return tuple(returnable)
    elif params[0] is '' and params[1] is '' and params[2] is '' and params[3] is None and params[4] is None:
        return ()
    else:
        raise ValueError('parameters!')


def validate_sum_of_expenses_params(params):
    """
    Validates the needed params for sum function
    Raises ValueError for invalid parameters
    :param params:
    :return:
    """
    type = params[1]
    types = ('water',
             'heating',
             'electricity',
             'gas',
             'other')
    if type in types and params[0] is '' and params[2] is '' and params[3] is None and params[4] is None:
        return tuple([type])
    else:
        raise ValueError('type!')


def validate_max_of_expenses_params(params):
    """
    Validates the needed params for max function
    Raises ValueError for invalid parameters
    :param params:
    :return:
    """
    apartment = params[0]
    if apartment is not '' and params[1] is '' and params[2] is '' and params[3] is None and params[4] is None:
        apartment = int(apartment)
        return tuple([apartment])
    else:
        raise ValueError('apartment!')


def validate_sort_expenses_params(params):
    """
    Validates the needed params for sort function
    Raises ValueError for invalid parameters
    :param params:
    :return:
    """

    if params[0] is '' and params[1] is not '' and params[2] is '' and params[3] is None and params[4] is None:
        type = params[1]
        return tuple([type])
    else:
        raise ValueError('apartment/type!')


def validate_filter_params(params):
    if params[0] is '' and params[1] is not '' and params[2] is '' and params[3] is None and params[4] is None:
        type = params[1]
        types = ('water',
                 'heating',
                 'electricity',
                 'gas',
                 'other')
        if type in types:
            return tuple([type])
        else:
            raise ValueError('type!')
    elif params[0] is not '' and params[1] is '' and params[2] is '' and params[3] is None and params[4] is None:
        amount = params[0]
        return tuple([amount])
    else:
        raise ValueError('amount/type!')


def validate_undo_params(params):
    print(params)
    if params[0] == '' and params[1] is '' and params[2] is '' and params[3] is None and params[4] is None:
        return []
    else:
        raise ValueError('parameters!(no parameters required!!)')


def validate_command(commands, cmd):
    try:
        return commands[cmd][0]
    except KeyError:
        return None
