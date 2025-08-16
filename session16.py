# string format
format_txt = 'My name is {name}, I am {age} years old'
print(format_txt.format(name='Saji', age='21'))
format_txt2 = 'My name is {0}, I am {1} years old'
print(format_txt2.format('Saji', 21))
format_txt3 = 'My name is {}, I am {} years old'
print(format_txt3.format('Saji', 21))
format_txt4 = 'My name is {:>10}'
print(format_txt4.format('Amir'))
format_txt5 = 'My name is {:<10}'
print(format_txt5.format('Amir'))
format_txt6 = 'My name is {:^12}'
print(format_txt6.format('amir'))
format_txt7 = 'I am {:d} years old'
print(format_txt7.format(21))
format_txt8 = 'I am {:b} binary years old'
print(format_txt7.format(10101))
format_txt9 = 'I am {:e} scientific years old'
print(format_txt9.format(9142487534957395))
format_txt10 = 'I am {:,} comma as a thousand seperator'
print(format_txt10.format(10203232))
format_txt11 = 'I am {:g} genenral format years old'  # scientific and round
print(format_txt11.format(123344353645))
