def print_format_table():
    """
    prints table of formatted text format options
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

#  1;32;40  0;32;40
def print_c2(text, format='0;32;40'):
    print('\x1b[%sm %s \x1b[0m' % (format, text))
#print_format_table()

#def print_c(text, format='0;32;40', end="\n", sep=" "):
def print_c(text, format='0;32;40', end="", sep=" "):
    print('\x1b[%sm%s \x1b[0m' % (format, text), end, sep)

def format_c(text, format='0;32;40'):
    return '\x1b[%sm%s \x1b[0m' % (format, text)

def print_st_c( format='0;32;40', end="", sep=" "):
    print('\x1b[%sm' % (format,), end, sep)

def print_en_c( format='0;32;40', end="", sep=" "):
    print(' \x1b[0m' % (format, ), end, sep)

if __name__ == '__main__':
    print_format_table()
