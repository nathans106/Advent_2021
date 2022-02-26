class Navigator:
    def forward(self, val: int):
        raise NotImplementedError

    def down(self, val: int):
        raise NotImplementedError

    def up(self, val: int):
        raise NotImplementedError


class AxisNavigator(Navigator):
    def __init__(self):
        self.pos = 0
        self.depth = 0

    def forward(self, distance):
        self.pos += distance

    def down(self, depth):
        self.depth += depth

    def up(self, depth):
        self.depth -= depth


class AimingNavigator(Navigator):
    def __init__(self):
        self.pos = 0
        self.depth = 0
        self.aim = 0

    def forward(self, val):
        self.pos += val
        self.depth += (self.aim * val)

    def down(self, val):
        self.aim += val

    def up(self, val):
        self.aim -= val


def execute_command(navigator, command):
    activities = {
        'forward ': navigator.forward,
        'down ': navigator.down,
        'up': navigator.up
    }

    for name in activities.keys():
        if command.startswith(name):
            activity = activities[name]
            val = int(command[len(name):])
            activity(val)
            return

    raise RuntimeError(f'Invalid command: {command}')


def execute_commands(navigator, commands):
    for command in commands:
        execute_command(navigator, command)
