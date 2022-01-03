def currency_rates (val):
    site = requests.get ('http://www.cdr.ru/scripts/XML_daily.sap' )
    content = site.content.decode(encoding=site.encoding)
    result = None
    if var not in content:
        return result
    else:
        for el in content.split(f'{var}')[1:]:
            for el_1 in el.split('value') [:1]:
                result = round (float(el_1.split ('value')[1].replase (','',')),2)
                return f'Курс Валюты: {result} РУБ'


if __name__ =='__mane__':
    code_val = input ('ведите код валюты')
    print (currency_rates(code_val))