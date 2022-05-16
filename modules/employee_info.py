
class EmployeeInfo:

    def __init__(self, employee_id=0, f_name="", l_name="", email="", position=""):
        self.employee_id = employee_id
        self.f_name = f_name
        self.l_name = l_name
        self.email = email
        self.position = position

    def __repr__(self):
        return str({
            'employee_id': self.employee_id,
            'f_name': self.f_name,
            'l_name': self.l_name,
            'email': self.email,
            'position': self.position
        })

    def json(self):
        return {
            'employee_id': self.employee_id,
            'f_name': self.f_name,
            'l_name': self.l_name,
            'email': self.email,
            'position': self.position
        }
