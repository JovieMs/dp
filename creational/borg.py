class Borg:
    __shared_state = {}

    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'Init'

    def __str__(self):
        return self.state


class YourBorg(Borg):
    pass

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = Borg()

    rm1.state = 'Idle'
    rm2.state = 'Running'

    print(rm1)
    print(rm2)

    rm2.state = 'Dead'
    print(rm1)
    print(rm2)

    rm3 = YourBorg()

    print(rm1)
    print(rm2)
    print(rm3)