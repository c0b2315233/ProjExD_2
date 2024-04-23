import os
import sys
import pygame as pg
import random as ra


WIDTH, HEIGHT = 1600, 900
os.chdir(os.path.dirname(os.path.abspath(__file__)))
key_mv :dict = {
    pg.K_UP:(0,-5),
    pg.K_DOWN:(0,5),
    pg.K_LEFT:(-5,0),
    pg.K_RIGHT:(5,0)
    }

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("fig/pg_bg.jpg")    
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    clock = pg.time.Clock()

    bomb_img=pg.Surface((100,100))
    bomb_img.set_colorkey((0,0,0))
    pg.draw.circle(bomb_img,(255,0,0),(50,50),10)
    bomb_rct=bomb_img.get_rect()
    bomb_rct.center=ra.randint(0,WIDTH),ra.randint(0,HEIGHT)
    bomb_vx=5
    bomb_vy=5


    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
        screen.blit(bg_img, [0, 0]) 
        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k,v in key_mv.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        kk_rct.move_ip(sum_mv)

        bomb_rct.move_ip(bomb_vx,bomb_vy)

        screen.blit(kk_img, kk_rct)
        screen.blit(bomb_img, bomb_rct)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
