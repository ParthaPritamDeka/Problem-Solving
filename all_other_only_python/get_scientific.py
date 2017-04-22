def get_decimal_scientific(data):

        q = float(data)
        r = format(q, '.5f')
        return r

print get_decimal_scientific('15.786378956345689')
