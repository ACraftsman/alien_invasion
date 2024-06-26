class Settings():
    """存储alien_invasion项目所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""
        #屏幕设置
        self.screen_width = 1500
        self.screen_height = 750
        self.bg_color = (230,230,230)
        #飞船的设置
        self.ship_limit = 3
        #子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 5
        #外星人设置
        self.fleet_drop_speed = 10
        #加快游戏节奏
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.1
        self.alien_speed_factor = 1
        # fleet_direction为1表示向右移动，为0表示向左移动
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)
        # print(self.alien_points)
