class Environment:
    def __init__(self, file_name):
        self.file_name = file_name
        self.original_grid, self.width, self.height = self.load_map(file_name)
        self.grid = [row[:] for row in self.original_grid]

    def load_map(self, file_name):
        with open(file_name, 'r') as f:
            dimensions = f.readline().strip().split()
            width, height = int(dimensions[0]), int(dimensions[1])
            grid = [list(line.strip()) for line in f.readlines()]
        return grid, width, height

    def reset(self):
        self.grid = [row[:] for row in self.original_grid]  # Reset to first state
