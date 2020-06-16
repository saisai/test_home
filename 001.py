'''
1.จงเรียงล ำดับตัวเลขจำกน้อยไปหำมำก โดย input ที่ใช้เป็ น String =”1,5,55,3,90,7,8,2,80”
และ output เก็บอยู่ในรูปของอำร์เรย์โดยห้ำมใช้ function sort()

1. Sort the numbers in order from very little, with the input used as String = "1,5,55,3,90,7,8,2,80"
And the output is stored in an array, using function sort ().
'''


def sort_string():
    param = "1,5,55,3,90,7,8,2,80"

    convert_str_to_list = param.split(',')

    result = list(map(int, convert_str_to_list))
    result.sort()
    return result


if __name__ == '__main__':
    print(sort_string())
