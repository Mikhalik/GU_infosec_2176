'''
4. Реализуйте базовый класс Car.
у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.
'''
import random
from random import randint

class Car:
    speed = int()
    color = ()
    name = ()
    is_police = bool()
    direction = ()

    def go_stop(self, speed):
        if speed > 10:
            print('Машина в движении')
        elif speed < 10:
            print('Машина медленно двигается')
        elif speed == 0:
            print('Машина остановилась')

    def turn(self, direction):
        if direction == 'left':
            print('Машина повернула на лево')
        elif direction == 'right':
            print('Машина повернула на право')
        else:
            print('Неизвестно куда повернула')

    def show_speed(self, speed):
        print(f'Текущая скорость: {speed} км/ч')

class TownCar(Car):

    def show_speed(self, speed):
        if speed > 60:
           print(f'Превышение скорости машины на {speed - 60} км/ч')

class SportCar(Car):

    def color_name(self, name, color):
        print(f'Спорткар модель: {name}, цвет: {color}')

class WorkCar(Car):

    def show_speed(self, speed):
        if speed > 40:
            print(f'Превышение скорости рабочего автомобиля на {speed - 40} км/ч')

class PoliceCar(Car):

    def police(self, is_police):
         if is_police == True:
             print(f'Наряд полиции на месте')
         else:
             print(f'Наряд полиции выехал. Ожидайте')

name = random.choice(['Lada', 'Mazda', 'Porsche', 'Lambo', 'Nixao'])
color = random.choice(['red', 'yellow', 'gold', 'green', 'blue'])
direction = random.choice(['left', 'right', 'x'])
is_police = random.choice([True, False])
speed = randint(0,100)

auto = Car()
auto.show_speed(speed)
auto.turn(direction)
auto.go_stop(speed)

tauto = TownCar()
tauto.show_speed(speed)

sauto = SportCar()
sauto.color_name(name, color)

wauto = WorkCar()
wauto.show_speed(speed)

pauto = PoliceCar()
pauto.police(is_police)
