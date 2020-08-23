from numpy import *

a = [['Fri', 10, 20, 30],['Sat', 15, 25, 35],['Sun', 5, 15, 25]]
m = reshape(a, (3, 4))

print(m)
print(type(m))

print(m[2])
print(m[1][0])

m_row = append(m, [['Mon', 2, 20, 50]], 0)
print(m_row)

m_col = insert(m_row, [4], [[1],[2],[3],[4]],1)
print(m_col)