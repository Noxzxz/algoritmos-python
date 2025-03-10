a = input('Digite 4 bits: ')

switch_case = {
    0b0000: lambda: print('0'),
    0b0001: lambda: print('1'),
    0b0010: lambda: print('2'),
    0b0011: lambda: print('3'),
    0b0100: lambda: print('4'),
    0b0101: lambda: print('5'),
    0b0110: lambda: print('6'),
    0b0111: lambda: print('7'),
    0b1000: lambda: print('8'),
    0b1001: lambda: print('9'),
    0b1010: lambda: print('10'),
    0b1011: lambda: print('11'),
    0b1100: lambda: print('12'),
    0b1101: lambda: print('13'),
    0b1110: lambda: print('14'),
    0b1111: lambda: print('15'),
}
 
 
try:
    a = int(a , 2)   
    if a in switch_case:
        switch_case[a]()
    else:
        print('input invalido')
except ValueError:
    print('input invalido')