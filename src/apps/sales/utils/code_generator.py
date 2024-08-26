import re


def code_generator(code, prefix):
    """_summary_

    Args:
        code (str): must be like that: "PRE-00000" or: ""
        prefix (str): must be like that: "PRE-"

    Returns:
        str: _description_
    """
    code_prefix = prefix
    code_suffix = ["-", "-0", "-00", "-000", "-0000"]

    # Extraction of the 6 latest charcater form invoice_code
    code = code[-6:]

    new_code = 0

    for i in range(len(code_suffix)): # loop for extract number from code
        x = re.split(code_suffix[i], code)
        print(x)

        try:
            if int(x[1]):
                new_code = int(x[1]) + 1
        except:
            pass

    if new_code == 0:  # create a new and the first code for the Table
        new_code = prefix + '00001'
    else:  # create a new code for the Table
        new_code = str(new_code)
        for x in range(5):
            if len(new_code) < 5:
                new_code = f'0{new_code}'

        new_code = f'{code_prefix}{new_code}'

    return new_code
