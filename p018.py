from joblib import Memory
from pip._internal.utils.appdirs import user_cache_dir
memory = Memory(cachedir=user_cache_dir('pip'), verbose=0)
big_triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def triangle_array(triangle):
    array = [line.split(" ") for line in triangle.split("\n")]
    sub_arrays = []
    for l in array:
        sub_arrays.append(list(map(int, l)))
    return sub_arrays

@memory.cache
def max_path(array):
    if len(array)==1:
        return array[0][0]
    else :
        top = array[0][0]
        left = []
        right = []
        for sub_array in array:
            if len(sub_array) > 1:
                left.append(sub_array[:-1])
                right.append(sub_array[1:])
        var = max(max_path(left)+top, max_path(right)+top)

        return var



print(max_path(triangle_array(big_triangle)))



