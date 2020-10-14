import random
import numpy as np
import pygame
import time


pygame.init()
width = 500
height = 500
row = 7
column = 4
pygame.display.set_caption("TimeTable")
win = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
red = (250, 51, 51)
green = (51, 250, 89)
total = 0


def writeIt(color, x, y, n):
    r = 3 * row
    c = 3 * column
    x = 3 * x+1
    y = 3 * y+1
    score = pygame.font.Font(
        'freesansbold.ttf', 20).render(str(n), True, color)
    win.blit(score, (y * width / c+3, x * height / r))


def colorIt(color, x, y):
    # pygame.time.delay(5)
    pygame.draw.rect(win, color, (2 + y * width / column, 2 + x *
                                  height / row, width / column - 2, height / row - 2))


def drawGrid(color, row, column):
    for i in range(1, column):
        if not i % 3:
            pygame.draw.line(win, color,
                             (i * width / column, 0), (i * width / column, height), 4)
        else:
            pygame.draw.line(win, color,
                             (i * width / column, 0), (i * width / column, height), 2)
    for i in range(1, row):
        if not i % 3:
            pygame.draw.line(win, color,
                             (0, i * height / row), (width, i * height / row), 4)
        else:
            pygame.draw.line(win, color,
                             (0, i * height / row), (width, i * height / row), 2)


def c(x):
    t = 0
    for i in range(7):
        t += ans[i].count(x)
        if t >= 3:
            break
    return t


def isValid(job, i):
    if i == 2:
        s = set(ans[0]+ans[1]+ans[2])
        if (len(s) >= 11 or job not in s) and job not in ans[2] and job not in ans[1]:
            return True
    elif job not in ans[i-1] and job not in ans[i] and (i < 6 or job not in ans[0]):
        if job == 'F' and c(job) == 0:
            return True
        if job != 'F' and c(job) < 3:
            return True
    return False


def solve():
    pygame.display.update()
    global ans, depth
    for i in range(7):
        for j in range(4):
            if not ans[i][j]:
                for job in jobs:
                    if isValid(job, i):
                        ans[i][j] = job
                        writeIt(black, i, j, job)
                        solve()
                        ans[i][j] = 0
                        colorIt(red, i, j)
                return
    print(np.matrix(ans))
    exit()


def main():
    win.fill(white)
    drawGrid(black, row, column)
    pygame.display.update()


main()
time.sleep(0.25)
jobs = ['GT', 'FSaA', 'C', 'PaS', 'PDE',
        'RoFG', 'FA', 'BA', 'N/G', 'F']
random.shuffle(jobs)
ans = [[0 for i in range(4)] for j in range(7)]
solve()
