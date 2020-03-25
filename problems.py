# ballista - тракетория падения тела при силах сопротивления в однородном поле
# kepler - рассчет траекторий движения в центральном поле
import math


# ввод параметров, проверка введено ли число
def input_parametrs(a):
    def check(number):
        if number.isdigit():
            return True
        else:
            try:
                float(number)
                return True
            except ValueError:
                return False

    while True:
        parametr = input(a)
        if check(parametr) == True:
            parametr = float(parametr)
            break
    return parametr


# тракетория падения тела при силах сопротивления в однородном поле g=1
def ballista():
    print('Построение траектории при даижении тела в однородном поле тяжести при действии сил сопротивления')
    v0 = input_parametrs('Введите начальную скорость: ')
    alfa = input_parametrs('Введите начальный угол: ')
    k1 = input_parametrs('Введите коэффициент сопротивления для силы трения: ')
    k2 = input_parametrs('Введите коэффициент сопротивления для силы лобового сопротивления: ')
    y = [0.0]
    x = [0.0]
    dt = 0.01
    t = [0.0]
    vx = [v0 * math.cos(alfa)]
    vy = [v0 * math.sin(alfa)]
    while True:
        x.append(x[-1] + vx[-1] * dt)
        y.append(y[-1] + vy[-1] * dt)
        v = math.sqrt(vx[-1] ** 2 + vy[-1] ** 2)
        vx.append(vx[-1] - (k1 * vx[-1] + k2 * v * vx[-1]) * dt)
        vy.append(vy[-1] - (1 + k1 * vy[-1] + k2 * v * vy[-1]) * dt)
        t.append(t[-1] + dt)
        if y[-1] <= 0.0:
            break
    return x, y


# рассчет траекторий движения в центральном поле
def kepler():
    vy = input_parametrs('Введите начальную скорость от 0.7 до 3: ')
    vx = 0.0
    y = [0.0]
    x = [1.0]
    dt = 0.01
    for i in range(2000):
        r = math.sqrt(x[-1] ** 2 + y[-1] ** 2)
        vx -= dt * x[-1] / r ** 3
        vy -= dt * y[-1] / r ** 3
        x.append(x[-1] + dt * 0.5 * vx)
        y.append(y[-1] + dt * 0.5 * vy)

    return x, y

    # vx:=vx-(x*dt/(r*sqr(r)))*(1+f/sqr(r));
    #           vy:=vy-(y*dt/(r*sqr(r)))*(1+f/sqr(r));
    #           x:=x+vx*dt; y:=y+vy*dt;
    #           r:=sqrt(sqr(x)+sqr(y));
    #           v:=sqrt(sqr(vx)+sqr(vy));
# Тутуттутут