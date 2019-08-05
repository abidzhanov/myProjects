class Settings():
    ''' This class holds all the settings of Alien Invasion game '''

    def __init__(self):
        ''' Initializing all the settings '''
        # Initialize screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
