import random

# 定义红球和蓝球的范围
red_balls_pool_1 = [1, 2, 5, 6, 8, 10, 14, 17]
red_balls_pool_2 = list(range(18, 36))
blue_balls_pool_1 = [1, 2, 5, 6, 8, 10]

red_balls_pool_3 = list(range(1, 36))
blue_balls_pool_2 = list(range(1, 13))

# 随机选择红球和蓝球
def select_birthday_balls():
    ran = random.random()
    ball_count = 3 if ran < 0.6 else 4 if ran < 0.9 else 5

    red_balls_1 = random.sample(red_balls_pool_1, ball_count)
    red_balls_2 = random.sample(red_balls_pool_2, 5-ball_count)

    # 蓝球
    blue_balls = random.sample(blue_balls_pool_1, 2)

    balls = sorted(red_balls_1 + red_balls_2) + sorted(blue_balls)
    balls_str = ['0' + str(b) if b < 10 else str(b) for b in balls]

    result = '{0} + {1}'.format(', '.join(balls_str[0:5]), ', '.join(balls_str[5:7]))
    return result

def select_random_balls():
    red_balls_1 = random.sample(red_balls_pool_3, 5)
    blue_balls = random.sample(blue_balls_pool_2, 2)

    balls = sorted(red_balls_1) + sorted(blue_balls)
    balls_str = ['0' + str(b) if b < 10 else str(b) for b in balls]

    result = '{0} + {1}'.format(', '.join(balls_str[0:5]), ', '.join(balls_str[5:7]))
    return result

def get_balls():
    result = ''
    for i in range(0, 5):
        # result += select_birthday_balls() + '\n'
        result += select_random_balls() + '\n'
    return result 

print(get_balls())