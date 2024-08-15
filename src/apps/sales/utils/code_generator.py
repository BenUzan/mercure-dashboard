import re


def product_code_generator(product_code):
    product_code_prefix = 'ART-'
    product_code_suffix = ["-", "-0", "-00", "-000", "-0000"]

    # Extraction of the 6 latest charcater form product_code
    product_code = product_code[-6:]

    new_product_code = 0

    # loop for extract number from product_code
    for i in range(len(product_code_suffix)):
        x = re.split(product_code_suffix[i], product_code)
        print(x)

        try:
            if int(x[1]):
                new_product_code = int(x[1]) + 1
        except:
            pass

    if new_product_code == 0:  # create a new and the first product_code for the Table
        new_product_code = 'ART-00001'
    else:  # create a new product_code for the Table
        new_product_code = str(new_product_code)
        for x in range(4):
            if len(new_product_code) < 5:
                new_product_code = f'0{new_product_code}'
            else:
                new_product_code = f'{product_code_prefix}{new_product_code}'

    return new_product_code


def invoice_code_generator(invoice_code):
    invoice_code_prefix = 'FAC-'
    invoice_code_suffix = ["-", "-0", "-00", "-000", "-0000"]

    # Extraction of the 6 latest charcater form invoice_code
    invoice_code = invoice_code[-6:]

    new_invoice_code = 0

    # loop for extract number from invoice_code
    for i in range(len(invoice_code_suffix)):
        x = re.split(invoice_code_suffix[i], invoice_code)
        print(x)

        try:
            if int(x[1]):
                new_invoice_code = int(x[1]) + 1
        except:
            pass

    if new_invoice_code == 0:  # create a new and the first product_code for the Table
        new_invoice_code = 'FAC-00001'
    else:  # create a new product_code for the Table
        new_invoice_code = str(new_invoice_code)
        for x in range(4):
            if len(new_invoice_code) < 5:
                new_invoice_code = f'0{new_invoice_code}'
            else:
                new_invoice_code = f'{invoice_code_prefix}{new_invoice_code}'

    return new_invoice_code


v = product_code_generator("ART-00019")
print(v)
