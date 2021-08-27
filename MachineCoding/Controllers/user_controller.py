class UserController(object):
    def __init__(self, userService):
        self.userService = userService

    def add_user(self, id, name):
        return self.userService.add_user(id, name)
