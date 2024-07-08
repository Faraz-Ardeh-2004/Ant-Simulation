class Ant:
    def __init__(self, genes):
        self.genes = genes
        self.x = 0
        self.y = 0
        self.direction = 3  # 0: North, 1: West, 2: South, 3: East
        self.state = 0
        self.food_eaten = 0

    def move(self, environment):
        action = int(self.genes[self.state * 3])
        if action == 1:  # Move forward
            if self.direction == 0:
                self.y = (self.y - 1) % environment.height
            elif self.direction == 1:
                self.x = (self.x - 1) % environment.width
            elif self.direction == 2:
                self.y = (self.y + 1) % environment.height
            elif self.direction == 3:
                self.x = (self.x + 1) % environment.width
            
            if environment.grid[self.y][self.x] == '1':
                self.food_eaten += 1
                environment.grid[self.y][self.x] = '0'
        elif action == 2:  # Turn right
            self.direction = (self.direction - 1) % 4
        elif action == 3:  # Turn left
            self.direction = (self.direction + 1) % 4
        # Action 4: Do nothing

    def sense(self, environment):
        sense_x, sense_y = self.x, self.y
        if self.direction == 0:
            sense_y = (sense_y - 1) % environment.height
        elif self.direction == 1:
            sense_x = (sense_x - 1) % environment.width
        elif self.direction == 2:
            sense_y = (sense_y + 1) % environment.height
        elif self.direction == 3:
            sense_x = (sense_x + 1) % environment.width
        return environment.grid[sense_y][sense_x] == '1'

    def update_state(self, food_ahead):
        if food_ahead:
            self.state = int(self.genes[self.state * 3 + 2])
        else:
            self.state = int(self.genes[self.state * 3 + 1])
