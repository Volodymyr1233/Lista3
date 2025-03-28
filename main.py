from sort_function import sort_log
from readLog import read


log2 = [(1, "error"), (2, "info"), (3, "warning")]

sortedlog1 = sort_log(log2, 1)

print(sortedlog1)