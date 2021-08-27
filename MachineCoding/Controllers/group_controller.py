class GroupController(object):
    def __init__(self, groupService):
        self.groupService = groupService

    def add_group(self, id, name, members):
        return self.groupService.add_user(id, name, members)
