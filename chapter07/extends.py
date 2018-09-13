class Filter:
    def __init__(self):
        self.blocked = []

    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked]


class SPAMFilter(Filter):
    def __init__(self):
        super().__init__()
        self.blocked = ["SPAM"]


f = Filter()
f_filter = f.filter([1, 2, 3])
print(f_filter)
s = SPAMFilter()
s_filter = s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'SPAM', 'bacon', 'SPAM', 'SPAM'])
print(s_filter)
# zhengjuns-MacBook-Pro:chapter07 zhengjun$ python3 extends.py
# [1, 2, 3]
# ['eggs', 'bacon']
print(f"issubclass(SPAMFilter, Filter) = {issubclass(SPAMFilter, Filter)}")
# issubclass(SPAMFilter, Filter) = True
print(f"issubclass(Filter, SPAMFilter) = {issubclass(Filter, SPAMFilter)}")
# issubclass(Filter, SPAMFilter) = False
print(f"isinstance(f, Filter) = {isinstance(f, Filter)}")
# isinstance(f, Filter) = True
print(f"isinstance(f,SPAMFilter) = {isinstance(f, SPAMFilter)}")
# isinstance(f,SPAMFilter) = False
print(f"isinstance(s,SPAMFilter) = {isinstance(s, SPAMFilter)}")
# isinstance(s,SPAMFilter) = True
print(f"isinstance(s,Filter) = {isinstance(s, Filter)}")
# isinstance(s,Filter) = True

print(f"isinstance(s,str) = {isinstance(s, str)}")
# isinstance(s,str) = False
print(f"s.__class__ = {s.__class__}")
# s.__class__ = <class '__main__.SPAMFilter'>

print(f"SPAMFilter.__bases__ = {SPAMFilter.__bases__}")
# SPAMFilter.__bases__ = (<class '__main__.Filter'>,)
print(f"Filter.__bases__ = {Filter.__bases__}")
# Filter.__bases__ = (<class 'object'>,)

print(f"issubclass(SPAMFilter, (Filter, object)) = {issubclass(SPAMFilter, (Filter, object))}")
# issubclass(SPAMFilter, (Filter, object)) = True
print(f"issubclass(SPAMFilter, (int, object)) = {issubclass(SPAMFilter, (int, object))}")
# issubclass(SPAMFilter, (int, object)) = True
