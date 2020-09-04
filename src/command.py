
class Command:
    commands = {}

    @classmethod
    def add_command(cls, pattern, fn):
        cls.commands[pattern] = fn

    @classmethod
    def parse_command(cls, command, *args):
        for pattern, fn in cls.commands.items():
            if ')' in pattern:
                start, end = pattern.split(')')
                if command in [start, start + end]:
                    fn(*args)
            elif command == pattern:
                fn(*args)

#Command.add_command('say', lambda p, msg: print(f'You say, "{(msg(-1))} '))
