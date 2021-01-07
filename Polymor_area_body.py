from Polymor_area_constr import Rectangle, Square, Circle

rect1 = Rectangle(3,4)  #  создаем два прямоугольника
rect2 = Rectangle(5,6)

squ1 = Square(4)        #  создаем два квадрата
squ2 = Square(7)

cir1 = Circle(3)        #  создаем два круга
cir2 = Circle(4)

print('Площадь первого прямоугольника =', rect1.area_rect())    #  выводим площадь
print('Площадь второго прямоугольника =', rect2.area_rect())
print('Площади двух квадратов', squ1.area_squ(), 'и', squ2.area_squ()) #  выводятся в одной строке
print('Площади двух кругов', cir1.area_cir(), 'и', cir2.area_cir())

# создаем список со всеми фигурами
figures = [rect1, rect2, squ1, squ2, cir1, cir2]
for elem in figures:
    if isinstance(elem, Square):  # если атрибут элемента списка принадлежит классу Square
        print('Это квадрат с площадью', elem.area_squ())
    elif isinstance(elem, Rectangle):
        print('Это прямоугольник с площадью', elem.area_rect())
    else:
        print('Это круг с площадью', elem.area_cir())
