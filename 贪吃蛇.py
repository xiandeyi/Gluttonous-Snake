'''贪吃蛇游戏
规定20为1单位长度
可以使用WSAD或方向键控制方向
空格表示暂停'''

import pygame
import time
import sys
import random
from pygame.locals import *

# 定义颜色
redColor = pygame.Color(255, 0, 0)
blackColor = pygame.Color(0, 0, 0)
whiteColor = pygame.Color(255, 255, 255)
greyColor = pygame.Color(150, 150, 150)


# 游戏结束函数
def game_over(playSurface, score):
    game_over_fonts = pygame.font.SysFont('arial', 54)  # 游戏结束字体和大小
    game_over_surf = game_over_fonts.render('Game Over!', True, greyColor)  # 游戏结束内容及颜色
    game_over_rect = game_over_surf.get_rect()
    game_over_rect.midtop = (300, 100)  # 显示位置
    playSurface.blit(game_over_surf, game_over_rect)
    score_font = pygame.font.SysFont('arial', 54)  # 得分显示
    score_surf = score_font.render('Score:' + str(score), True, greyColor)
    score_rect = score_surf.get_rect()
    score_rect.midtop = (300, 50)
    playSurface.blit(score_surf, score_rect)
    pygame.display.flip()  # 刷新显示页面
    time.sleep(5)
    pygame.quit()
    sys.exit()


def main():
    # 初始化pygame
    pygame.init()
    fpsClock = pygame.time.Clock()
    # 创建pygame显示层
    playSurface = pygame.display.set_mode((600, 460))  # 设置窗口大小
    pygame.display.set_caption('Snake Game')  # 设置窗口名称

    # 设置贪吃蛇和食物
    snake_position = [100, 100]  # 初始蛇头位置
    snake_segments = [[100, 100]]  # 蛇身长度 初始为1
    food_position = [300, 300]  # 食物的初始位置
    food_num = 1  # 食物的数目为1
    direction = 'right'  # 初始方向向右
    change_direction = direction
    score = 0  # 初始得分

    # 按键控制运动轨迹
    while(True):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:  # 判断键盘输入
                if event.key == K_RIGHT or event.key == ord('d'):
                    change_direction = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    change_direction = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    change_direction = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    change_direction = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # 判断是否输入了反方向
        if change_direction == 'right' and not direction == 'left':
            direction = change_direction
        if change_direction == 'left' and not direction == 'right':
            direction = change_direction
        if change_direction == 'up' and not direction == 'down':
            direction = change_direction
        if change_direction == 'down' and not direction == 'up':
            direction = change_direction
        # 根据方向移动蛇头坐标
        if direction == 'right':
            snake_position[0] += 20
        if direction == 'left':
            snake_position[0] -= 20
        if direction == 'up':
            snake_position[1] -= 20
        if direction == 'down':
            snake_position[1] += 20
        # 增加蛇的长度
        snake_segments.insert(0, list(snake_position))
        # 判断食物是否被吃掉
        if snake_position[0] == food_position[0] and snake_position[1] == food_position[1]:
            food_num = 0
        else:
            snake_segments.pop()  # 如果没有吃掉食物,最后1单位蛇身提出列表
        # 如果吃掉食物，则重新生成食物
        if food_num == 0:
            x = random.randrange(1, 30)  # 和游戏界面大小相关
            y = random.randrange(1, 23)
            food_position = [int(x*20), int(y*20)]
            food_num = 1
            score += 1
        # 判断是否死亡  包括撞墙和撞自身
        if snake_position[0] > 600 or snake_position[0] < 0:
            game_over(playSurface, score)  # 撞击左右边界，游戏结束
        if snake_position[1] > 460 or snake_position[1] < 0:
            game_over(playSurface, score)  # 撞击上下边界，游戏结束
        for snake_body in snake_segments[1:]:
            if snake_position[0] == snake_body[0] and snake_position[1] == snake_body[1]:
                game_over(playSurface, score)
        # 绘制pygame显示层
        playSurface.fill(blackColor)
        for position in snake_segments:
            pygame.draw.rect(playSurface, whiteColor, Rect(position[0], position[1], 20, 20))
            pygame.draw.rect(playSurface, whiteColor, Rect(food_position[0], food_position[1], 20, 20))
        # 刷新pygame显示层
        pygame.display.flip()
        # 控制游戏速度
        fpsClock.tick(5)


if __name__ == '__main__':
    main()
    time.sleep(3)