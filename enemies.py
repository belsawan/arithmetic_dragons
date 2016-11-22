# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

def get_prostota(a):
    for i in range(2, a):
        if a%i==0:
            return 'нет'
        else:
            return 'да'


class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'зелёный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'черный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x*y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'красный дракон'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class Troll_Evklid(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'Тролль-простое-число'

    def isPrime(self, n):
        if n % 2 == 0:
            return n == 2
        d = 3
        while d * d <= n and n % d != 0:
            d += 2

        return d * d > n

    def question(self):
        x = randint(1, 100)
        self.__quest = 'Простое ли число ' + str(x) + '?'
        if self.isPrime(x):
            self.set_answer('да')
        else:
            self.set_answer('нет')
        return self.__quest

class Troll_lucky(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'троль на удачу'
    def question(self):
        x=randint(1,2)
        self.__quest = 'Угадай число от 1 до 5!'
        self.set_answer(x)
        return self.__quest

class Troll_razlogatel(Dragon):
    def __init__(self):
        self._health = 100
        self._attack = 10
        self._color = 'троль-Эвклид'

    def get_answer(self, n):
        Ans = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                Ans.append(d)
                n //= d
            else:
                d += 1
        if n > 1:
            Ans.append(n)
        Ans.sort()
        res = ''
        for i in Ans:
            res += str(i)
            res += ','
        res = '1,' + res[0:-1]
        return res
    def question(self):
        x=randint(1,100)
        self.__quest = 'Напиши множители ' + str(x) + ' через запятую, смертный! (Не забудь единицу, холоп!)'
        self.set_answer(self.get_answer(x))
        return self.__quest



#enemy_types = [GreenDragon, RedDragon, BlackDragon, Troll_lucky, Troll_Evklid, Troll_razlogatel]
enemy_types=[Troll_lucky]