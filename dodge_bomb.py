import os
import sys
import pygame as pg
import random as ra
import time as t

def check_round(obj_rct:pg.Rect) -> tuple[bool,bool]:
    """
    こうかとん、爆弾rectの画面内外判定用の関数
    引数:こうかとんrect,又は,爆弾rect
    戻り値:横方向、縦方向判定結果(True:画面内/False:画面内)
    """
    X,Y=True,True
    if obj_rct.left < 0 or WIDTH < obj_rct.right:
        X=False
    if obj_rct.top < 0 or HEIGHT < obj_rct.bottom:
        Y=False
    return X,Y

def rot_kk(kk_rot:tuple):
    """
    こうかとんの回転用関数
    引数:押されたボタンのタプル
    戻り値:角度の変数
    """
    return 0


def bomb_size(g_time:int):
    """
    爆弾を大きくする関数
    引数:ゲームの進行時間
    返り値:リストのタプル
    """
    return 0

def Bomb_follow(now_bomb,now_kk:pg.rect):
    """
    爆弾の追従をさせる関数
    引数:こうかとんの位置と爆弾の位置
    返り値:ベクトルのタプル
    """
    return 0

def GameOver(screen:pg.rect):
    """
    ゲームオーバー関数
    ゲームオーバーの画面を表示する
    引数:画面のオブジェクト
    返り値:無
    """
    screen.fill((0,0,0))            #画面を生成
    font = pg.font.Font(None,100)
    text = font.render("GAMEOVER",True,(255,255,255))
    screen.blit(text,(WIDTH/2-150,HEIGHT/2))
    kk_img=pg.transform.rotozoom(pg.image.load("fig/3.png"),0,2.8)
    kk_rct=kk_img.get_rect()
    kk_rct.center = 900,350
    screen.blit(kk_img,kk_rct)      #こうかとんの配置
    kk_rct.center = 700,350
    screen.blit(kk_img,kk_rct)
    pg.display.update()
    t.sleep(5)                      #5秒待機


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
    bg_img = pg.image.load("fig/pg_bg.jpg")         #こうかとんの前処理
    kk_img = pg.transform.rotozoom(pg.image.load("fig/3.png"), 0, 2.0)
    kk_rct = kk_img.get_rect()
    kk_rct.center = 900, 400
    clock = pg.time.Clock()

    bomb_img=pg.Surface((100,100))                  #爆弾の前処理
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
        
        if kk_rct.colliderect(bomb_rct):
            GameOver(screen)
            break
        screen.blit(bg_img, [0, 0])

        key_lst = pg.key.get_pressed()
        sum_mv = [0, 0]
        for k,v in key_mv.items():
            if key_lst[k]:
                sum_mv[0] += v[0]
                sum_mv[1] += v[1]
        
        kk_rct.move_ip(sum_mv)

        if check_round(kk_rct) != (True,True):
            kk_rct.move_ip(-sum_mv[0] , -sum_mv[1])

        fgx,fgy=check_round(bomb_rct)
        if not fgx:
            bomb_vx *= -1
        if not fgy:
            bomb_vy *= -1
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
