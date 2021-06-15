class Node():

    def __init__(self, data, prev = None, next = None):
        self.__data = data
        self.__prev__ = prev
        self.__next__ = next

    def get_data(self):
        return self.__data

    def __str__(self):
        next = None
        prev = None
        if self.__next__ is not None:
            next = self.__next__.get_data()
        if self.__prev__ is not None:
            prev = self.__prev__.get_data()
        return 'data: {}, prev: {}, next: {}'.format(self.get_data(), prev, next)

class LinkedList():

    def __init__(self, first = None, last = None):
        self.__length = 0
        self.__first__ = first
        self.__last__ = last
        if first is None and last is not None:
            raise ValueError("invalid value for last")
        elif last is None and first is not None:
            self.__first__= Node(first)
            self.__last__ = self.__first__
            self.__length = 1
        elif first is not None and last is not None:
            self.__first__ = Node(first)
            self.__last__ = Node(last)
            self.__first__.__next__ = self.__last__
            self.__last__.__prev__ = self.__first__
            self.__length = 2

    def append(self, element):
        if self.__length == 0:
            self.__length = 1
            self.__first__ = Node(element)
            self.__last__ = self.__first__
        else:
            self.__length += 1
            self.__last__.__next__ = Node(element, self.__last__)
            self.__last__ = self.__last__.__next__

    def __len__(self):
        return self.__length


    def pop(self):
        if self.__length == 0:
            raise IndexError('LinkedList is empty!')
        self.__last__ = self.__last__.__prev__
        self.__last__.__next__ = None
        self.__length -= 1

    def __str__(self):
        if self.__length == 0:
            return 'LinkedList[]'
        else:
            s = self.__first__
            result = str(s)
            while s.__next__  is not None:
                s = s.__next__
                result += '; '+str(s)
            return 'LinkedList[length = {}, [{}]]'.format(self.__length, result)


    def clear(self):
        self.__first__ = Node(None)
        self.__last__ = Node(None)
        self.__length = 0

    def popitem(self, element):
        mid = self.__first__
        num = True
        while mid is not None:
            if element == mid.get_data():
                if self.__length == 1:
                    self.__first__ = Node(None)
                    self.__length = 0
                    self.__last__ = self.__first__
                    num = False
                    break
                if mid.__prev__ is None:
                    self.__first__ = self.__first__.__next__
                    self.__first__.__prev__ = None
                    self.__length -= 1
                elif mid.__next__ is None:
                    self.__last__ = self.__last__.__prev__
                    self.__last__.__next__ = None
                    self.__length -= 1
                else:
                    mid.__next__.__prev__ = mid.__prev__
                    mid.__prev__.__next__ = mid.__next__
                    self.__length -= 1
                num = False
                break
            mid = mid.__next__
        if num:
            raise KeyError("{} doesn't exist!".format(element))
