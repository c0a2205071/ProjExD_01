import pygame as pg
import sys

def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 1, 1.0), pg.transform.rotozoom(kk_img, 3, 1.0), pg.transform.rotozoom(kk_img, 5, 1.0), pg.transform.rotozoom(kk_img, 7, 1.0), pg.transform.rotozoom(kk_img, 9, 1.0), pg.transform.rotozoom(kk_img, 11, 1.0), pg.transform.rotozoom(kk_img, 13, 1.0), pg.transform.rotozoom(kk_img, 15, 1.0), pg.transform.rotozoom(kk_img, 17, 1.0), pg.transform.rotozoom(kk_img, 19, 1.0)]

    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x = tmr % 1600
        screen.blit(bg_img, [-x, 0])
        screen.blit(pg.transform.flip(bg_img, True,False), [1600-x, 0])
        screen.blit( kk_imgs[tmr%2], [300, 200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()