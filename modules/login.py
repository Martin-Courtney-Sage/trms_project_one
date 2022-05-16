class Login:

    def __init__(self, main_id=0, employee_id=0, username="", passcode=""):
        self.main_id = main_id
        self.employee_id = employee_id
        self.username = username
        self.passcode = passcode

    def __repr__(self):
        return str({
            'main_id': self.main_id,
            'employee_id': self.employee_id,
            'username': self.username,
            'passcode': self.passcode
        })

    def json(self):
        return {
            'main_id': self.main_id,
            'employee_id': self.employee_id,
            'username': self.username,
            'passcode': self.passcode
        }
