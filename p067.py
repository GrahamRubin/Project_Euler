from joblib import Memory
from pip._internal.utils.appdirs import user_cache_dir
memory = Memory(cachedir=user_cache_dir('pip'), verbose=0)
big_triangle_file = open("D:\\graham_temp\\peuler\\maxpath.txt", "r")
big_triangle = big_triangle_file.read()


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



