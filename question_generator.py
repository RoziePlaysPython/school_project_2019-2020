#dict_base={10:'A' , 11:'B' , 12:'C' , 13:'D' , 14:'E' , 15:'F'}


def num_to_numbase2to10(num, base):
    new_num=''
    while num>0:
        new_num=str(num%base)+new_num
        num//=base
    return new_num
    #функция переводит поступающее число в другую систему счисления
    #вроде работает без ошибок

#numbers=[a,b,base_a, base_b, result, base_result]
def numsys2_10(numbers, operation):
    num_bases={2:f'\N{SUBSCRIPT TWO}',3:f'\N{SUBSCRIPT THREE}',4:f'\N{SUBSCRIPT FOUR}',5:f'\N{SUBSCRIPT FIVE}',6:f'\N{SUBSCRIPT SIX}',7:f'\N{SUBSCRIPT SEVEN}',8:f'\N{SUBSCRIPT EIGHT}',9:f'\N{SUBSCRIPT NINE}', 10:f'\N{SUBSCRIPT ONE}\N{SUBSCRIPT ZERO}'}
    #operation= '+' or '-'
    a=numbers[0]
    b=numbers[1]
    base_a=numbers[2]
    base_b=numbers[3]
    result=numbers[4]
    base_result=numbers[5]
    #
    new_a=num_to_numbase2to10(a,base_a)
    new_b=num_to_numbase2to10(b,base_b)
    new_result=num_to_numbase2to10(result,base_result)
    answer=[str(new_a)+num_bases[base_a]+operation+str(new_b)+num_bases[base_b]+"=?"+num_bases[base_result], new_result]
    return answer
    #эта функция подготавливает "красивую" запись выражения, с подстрочным индексом и т.п.
    #её нужно перепроверить
    #тут всё странно выглядит
