class Hotel:
    _prices = {"SGL": 100, "DBL": 200, "Junior Suite": 300, "Suite": 400} # Цены для каждого типа комнат
    _rooms = dict()

    def __init__(self, list_rooms):
        curr = list(self._prices.keys())
        _total = sum(list_rooms)
        for i in range(len(list_rooms)):
            self._rooms[curr[i]] = [True for _ in range(list_rooms[i])]

    # метод для бронирования номера по типу комнаты и уникальному значению в списке комнат данного типа
    def occupy(self, lux, room_id):
        if (self._rooms[lux][room_id]):
            self._rooms[lux][room_id] = False  # бронируем номер
        else:
            raise RuntimeError()

    # метод для освобождения номера по уникальному значению в списке
    def free(self, lux, room_id):
        self._rooms[lux][room_id] = True  # освобождаем номер

   # метод для стандартизированного вывода списка номеров и их состояния
    def __str__(self):
        res = str()
        for item in list(self._rooms.keys()):
            s = f"Тип {item}:" + "\n"
            for i in range(len(self._rooms[item])):
                s += "Номер " + str(i) + " - " + ("Свободен\n" if self._rooms[item][i] else "Занят\n")
            res += s
        return res

    # метод для занятия всех комнат одновременно
    def occupyAll(self):
        for item in list(self._rooms.keys()):
            for index in range(len(self._rooms[item])):
                self._rooms[item][index] = False

    # метод для освобождения всех комнат одновременно
    def freeAll(self):
        for item in list(self._rooms.keys()):
            for index in range(len(self._rooms[item])):
                self._rooms[item][index] = True

    # приватный метод для получения числа занятых комнат для данного типа
    def _numberOccupied(self, lux):
        return len(list(filter(lambda x: not x, self._rooms[lux])))

    # метод для подсчитывания заработка по установленным ценам
    def incomes(self):
        incomes = 0
        for item in list(self._rooms.keys()):
            incomes += self._numberOccupied(item) * self._prices[item]
        return incomes

    # метод для получения долей занаятости комнат каждого типа (вывод в виде словаря)
    def occupyShare(self):
        share = dict()
        for item in list(self._rooms.keys()):
            share[item] = str(round(self._numberOccupied(item) / len(self._rooms[item]), 2) * 100) + '%'
        return share


hotel = Hotel((5, 6, 1, 3))  # в нашем отеле, например, 5 SGL номеров, 6 DBl номеров, 1 Juniour Suite номер, 3 Suite номеров
hotel.occupy("SGL", 3) # Бронируем соотвествующий номер в SGL
hotel.occupy("DBL", 1) # Бронируем соотвествующий номер в DBL
print(hotel)  # Смотрим номера и их состояния
print(hotel.occupyShare()) # Считаем долю занятых по каждому типу
hotel.free("SGL", 3) # Освобождаем занятый номер
print(hotel.incomes()) # Считаем выручку с одним занятым номеров
hotel.occupyAll() # Занимаем все номера
print(hotel.occupyShare()) # Смотрим, что доля занятых везде 100%
print(hotel.incomes()) # Считаем максимальную выручку
hotel.freeAll() # Освобождаем все номера
print(hotel.occupyShare()) # Смотрим, что доля занятых везде 0%
