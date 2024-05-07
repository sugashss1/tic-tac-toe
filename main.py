import sys
import pygame as py
import numpy as np
import tree
def draw_line(surf,c, p1, p2, w,dx,dy):
    tempoint = p1
    if turn!=0:
        while tempoint < p2:
            py.draw.line(surf,c,p1,tempoint,w)
            ltempoint=list(tempoint)
            ltempoint[0]+=dx
            ltempoint[1]+=dy
            tempoint=tuple(ltempoint)
            py.display.update()
        if dx<0 or dy<0:
            while tempoint > p2:
                py.draw.line(surf, c, p1, tempoint, w)
                ltempoint = list(tempoint)
                ltempoint[0] += dx
                ltempoint[1] += dy
                tempoint = tuple(ltempoint)
                py.display.update()
    else:
        py.draw.line(surf, c, p1, p2, w)
mou=np.array([[0,0,0],[0,0,0],[0,0,0]])
turn=0
scene=0
mouse=0
con=0
status=0
game=False
ai=True
py.init()
clock=py.time.Clock()
s=py.display.set_mode((800,600))
back = py.image.load('image/sky.jpg')
icon=py.image.load('image/icon.png')
box= py.image.load('image/box 85.png')
fontObj = py.font.Font(None, 32)
cross=py.image.load('image/bigx.png')
o=py.image.load('image/o.png')
button1=py.image.load('image/AI-removebg-preview.png')
button2=py.image.load('image/PASS143.png')
button3=py.image.load('image/play 250.png')
draw=py.image.load('image/draw1.png')
py.display.set_caption('tic tac toe')
py.display.set_icon(icon)
while True:
        def start():
            global s
            for e in py.event.get():
                if e.type == py.QUIT:
                    sys.exit()
            s.blit(back, (0, 0))
            s.blit(button1, (320, 300))
            s.blit(button2, (320, 200))
            m = py.mouse.get_pos()
            ix, iy = m
            dis(ix, iy)
            py.display.update()
            clock.tick(60)

        def dis(x,y):
            X = fontObj.render(str(x), True, (255, 255, 255))
            Y = fontObj.render(str(y), True, (255, 255, 255))
            s.blit(X, (0, 0))
            s.blit(Y, (50, 0))
        while game:
            start()
        def reset():
            m = py.mouse.get_pos()
            ix, iy = m
            global scene,turn,back,mou
            s.blit(back,(0,0))
            for i in range(0, 3):
                for j in range(0, 3):
                    s.blit(box, (270 + (j * 80), 150 + (i * 80)))
            s.blit(button3, (270, 400))
            for e in py.event.get():
                if e.type==py.QUIT:
                    sys.exit()
                if e.type==py.MOUSEBUTTONDOWN:
                    if ix<520 and ix>270 and iy<520 and iy>400:
                        scene-=1
                        mou = np.zeros((3, 3), dtype=int)
            dis(ix,iy)
            elementup(mou)
            if (status != 0):
                draw_line(s, (0,0,0), slinepos, elinepos, 10,dx,dy)
            py.display.update()
            turn = 0
        while scene==1:
            reset()
        status=0
        m = py.mouse.get_pos()
        ix, iy = m
        p = py.mouse.get_pressed(3)
        s.blit(back, (0, 0))
        dis(ix,iy)
        for i in range(0, 3):
            for j in range(0, 3):
                s.blit(box, (270 + (j * 80), 150 + (i * 80)))
        for e in py.event.get():
            if e.type == py.QUIT:
                sys.exit()
        if p[0] and con==0:
            con+=1
            for i in range(0, 3):
                for j in range(0, 3):
                    if ix > 270 + (j * 80) and ix < 350 + (j * 80):
                        if iy > 150 + (i * 80) and iy < (230 + (i * 80)):

                            if mou[j][i] == 0 and turn % 2 == 0:
                                mou[j][i] += 1
                                turn += 1
                            if mou[j][i] == 0 and turn % 2 == 1:
                                mou[j][i] -= 1
                                turn += 1
        def mousecheck():
            global con
            if p[0]==False and con==1:
                con=0
        mousecheck()
        def elementup(mou):
            for i in range(0, 3):
                for j in range(0, 3):
                    if mou[j][i] == 1:
                        s.blit(cross, (280 + (j * 80), 160 + (i * 80)))
                    if mou[j][i] == -1:
                        s.blit(o, (280 + (j * 80), 160 + (i * 80)))
        elementup(mou)
        if mou[0][0] == mou[1][1] == mou[2][2] == 1 or mou[0][0] == mou[1][1] == mou[2][2] == -1:
            scene+=1
            slinepos=(290,170)
            elinepos=(495,375)
            dx=0.5
            dy=0.5
            if turn % 2 == 1:
                status+=1
            else:
                status-=1
        if mou[0][2] == mou[1][1] == mou[2][0] == 1 or mou[0][2] == mou[1][1] == mou[2][0] == -1:
            scene+=1
            slinepos = (490, 170)
            elinepos = (285, 375)
            dx=-0.2
            dy=0.2
            if turn % 2 == 1:
                status += 1
            else:
                status -= 1
        for i in range(0, 3):
            if mou[i][0] == mou[i][1] == mou[i][2] == 1 or mou[i][0] == mou[i][1] == mou[i][2] == -1:
                scene+=1
                slinepos = (310+80*i, 160)
                elinepos = (310+80*i, 375)
                dx=0
                dy=0.1
                if turn % 2 == 1:
                    status += 1
                else:
                    status -= 1
            if mou[0][i] == mou[1][i] == mou[2][i] == 1 or mou[0][i] == mou[1][i] == mou[2][i] == -1:
                scene+=1
                slinepos = (290,190+80*i)
                elinepos = (500, 190+80*i)
                dx=0.1
                dy=0
                if turn % 2 == 1:
                    status += 1
                else:
                    status -= 1
        if turn>=9 and status==0:
            scene += 1
        py.display.update()
        clock.tick(60)
        if turn%2==1 and scene==0 and ai:
            mou=tree.minmax(mou)
            turn+=1