class HouseScheme:
    def __init__(self, count_of_rooms, life_area, is_bathroom_included):
        if isinstance(count_of_rooms, int) and (life_area > 0) and isinstance(is_bathroom_included, bool):
            self.count_of_rooms = count_of_rooms
            self.life_area = life_area
            self.is_bathroom_included = is_bathroom_included
        else:
            raise ValueError('Invalid value')


class CountryHouse(HouseScheme):
    def __init__(self, count_of_rooms, life_area, is_bathroom_included, count_of_floors, site):
        super().__init__(count_of_rooms, life_area, is_bathroom_included)
        self.count_of_floors = count_of_floors
        self.site = site

    def __str__(self):
        return "Country House: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Количество " \
               "этажей {}, Площадь участка {}.".format(self.count_of_rooms, self.life_area,
                                                       self.is_bathroom_included, self.count_of_floors, self.site)

    def __eq__(self, other):
        if self.life_area == other.life_area and self.site == other.site and abs(
                self.count_of_floors - other.count_of_floors) <= 1:
            return True
        else:
            return False


class Apartment(HouseScheme):
    def __init__(self, count_of_rooms, life_area, is_bathroom_included, floor, windows):
        super().__init__(count_of_rooms, life_area, is_bathroom_included)
        self.floor = floor
        self.windows = windows
        if 16 > self.floor > 0 and self.windows in ['N', 'S', 'W', 'E']:
            pass
        else:
            raise ValueError('Invalid value')

    def __str__(self):
        return "Apartment: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Этаж {}, " \
               "Окна выходят на {}.".format(self.count_of_rooms, self.life_area, self.is_bathroom_included,
                                            self.floor, self.windows)


class CountryHouseList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def append(self, p_object):
        if isinstance(p_object, CountryHouse):
            self = super().append(p_object)
        else:
            raise TypeError("Invalid type {}".format(p_object.__class__))

    def total_square(self):
        sum_of_square = 0
        for i in self:
            sum_of_square += i.life_area
        return sum_of_square


class ApartmentList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def extend(self, iterable):
        for x in iterable:
            if x.__class__ == Apartment:
                self.append(x)

    def floor_view(self, floors, directions):
        for x in filter(lambda i: floors[0] <= i.floor <= floors[1] and i.windows in directions, self):
            print('{0}: {1}'.format(x.windows, x.floor))

