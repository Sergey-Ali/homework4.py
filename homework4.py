tuple_ = 1,2,'a','b'
immutable_war = tuple_
print(tuple_)
print(type(immutable_war))
#tuple_[3] = 100
print(tuple_)
mutable_list=[1,2,'a','b','Modified']
print(mutable_list[3])
mutable_list[3] = 'c'
print(mutable_list)
