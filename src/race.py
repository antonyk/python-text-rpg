from body import Body, BodyPart


class Race:
    def __init__(self, name, body):
        self.name = name
        self.body = body


def init_races():
    # Human
    bodyParts = {
        'head': BodyPart('head', 'head', 5, True, False),
        'chest': BodyPart('chest', 'torso', 5, True, False),
        'rarm': BodyPart('rarm', 'limb', 5, True, False),
        'larm': BodyPart('larm', 'limb', 5, True, False),
        'rhand': BodyPart('rhand', 'limb', 5, True, True),
        'lhand': BodyPart('lhand', 'limb', 5, True, True),
        'rleg': BodyPart('rleg', 'limb', 5, True, False),
        'rfoot': BodyPart('rfoot', 'limb', 5, True, False),
        'lleg': BodyPart('lleg', 'limb', 5, True, False),
        'lfoot': BodyPart('lfoot', 'limb', 5, True, False),
    }

    # humanoid = Body("humanoid", parts)
    # human = Race()


# init_races()
