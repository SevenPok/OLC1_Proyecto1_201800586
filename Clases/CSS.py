class CSS:

    reserve = {}
    operadores = {'>': 'GREATER', '<': 'MINOR', '/': 'DIGONAL','{':'LEFT_KEY','}':'RIGHT_KEY'}

    def __init__(self):
        self.tokens = []
