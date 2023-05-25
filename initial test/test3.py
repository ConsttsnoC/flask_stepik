# -*- coding: utf-8 -*-
#https://stepik.org/lesson/534343/step/5?unit=527467

class Elevator():
    """Класс описывающий работу лифта"""
    def __init__(self, max_floor=5, floor=3):
        self.max_floor = int(max_floor)
        self.floor = int(floor)



    def max(self):
        return self.floor <= self.max_floor

    def up(self):
        '''Лифт движется вверх'''
        if self.floor < self.max_floor:
            self.floor += 1
            print(f'Лифт поднимается на {self.floor} этаж')
        else:
            print('Лифт не может подняться выше')

    def down(self):
        '''Лифт движется вниз'''
        if self.floor > 1:
            self.floor -= 1
            print(f'Лифт опускается на {self.floor} этаж')
        else:
            print('Лифт не может опуститься ниже')

elevator = Elevator()

# Движение лифта вверх
elevator.up()

# Движение лифта вниз
elevator.down()
elevator.up()
elevator.up()
elevator.up()
elevator.down()
elevator.down()
elevator.down()
elevator.down()
elevator.down()
elevator.down()




