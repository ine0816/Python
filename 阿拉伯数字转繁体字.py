from decimal import Decimal
from decimal import getcontext
 
num_to_ch_dic = { 0:'零', '.':'点', 1:'壹', 2:'贰', 3:'叁', 4:'肆',5:'伍',6:'陆',7:'柒',8:'捌',9:'玖', 10:'z'}
li_dw = [ '萬','亿','萬']
character_num = ['壹', '贰', '叁', '肆','伍','陆','柒','捌','玖']
li_dot = [ '分','角']
li_mod = list("拾佰仟")
 
if __name__ == '__main__':
    str_num = input("Please Input a num: ")
    #str_num = "1000000001000001"
    final_str = ''
 
    detail_dw = list("分角元拾佰仟")
    for i in li_dw :
        detail_dw.append(i)
        for j in li_mod :
            detail_dw.append(j)
    detail_dw.reverse()
    print(detail_dw)
    max_len = len(detail_dw)
 
    li_num = list(str(int(Decimal(str_num) * 100)).rjust(max_len, '0'))
    print(li_num)
    li_dw.append('元')
    index_tmp = 0
    while index_tmp < max_len :
        if detail_dw[index_tmp] in li_dw :
            if li_num[index_tmp] == '0':
                li_num[index_tmp] = '10'
        li_num[index_tmp] = num_to_ch_dic[int(li_num[index_tmp])]
        index_tmp = index_tmp + 1
    print(li_num)
    li_num_str = ''.join(li_num)
    print(li_num_str)
    li_num_str = li_num_str.replace('零零零z','---z')
    li_num_str = li_num_str.replace('零零z', '--z')
    li_num_str = li_num_str.replace('z零零', 'z--')
    li_num_str = li_num_str.replace('z零', 'z-')
    li_num_str = li_num_str.replace('零z', '-z')
    print(li_num_str)
    li_num = list(li_num_str)
    index_tmp = 0
 
    start_sign = 0
    while index_tmp < max_len:
        if start_sign == 0:
            if li_num[index_tmp] in character_num:
                start_sign = 1
                final_str = li_num[index_tmp] + detail_dw[index_tmp]
        elif start_sign == 1:
            if li_num[index_tmp] == 'z':
                final_str = final_str + detail_dw[index_tmp]  + '零'
            elif li_num[index_tmp] == '-':
                final_str = final_str + ''
            elif li_num[index_tmp] == '零':
                final_str = final_str + '零'
            else:
                final_str = final_str + li_num[index_tmp] + detail_dw[index_tmp]
        index_tmp = index_tmp + 1
    if start_sign == 0:
        final_str = '零元零分整'
    else:
        print(final_str)
        final_str = final_str .replace('零零', '零')
        final_str = final_str.replace('亿萬', '亿零')
        final_str = final_str + '整'
        final_str = final_str .replace('圆零整', '圆整')
        final_str = final_str .replace('角零整', '角整')
        final_str = final_str .replace('零零', '零')
    print(final_str)
