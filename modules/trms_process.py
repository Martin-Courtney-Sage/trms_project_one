
class TRMSProcess:

    def __init__(self, doc_id=0, employee_id=0, f_status="", documentation="", r_type=""):
        self.doc_id = doc_id
        self.employee_id = employee_id
        self.f_status = f_status
        self.documentation = documentation
        self.r_type = r_type

    def __repr__(self):
        return str({
            'doc_id': self.doc_id,
            'employee_id': self.employee_id,
            'f_status': self.f_status,
            'documentation': self.documentation,
            'r_type': self.r_type
        })

    def json(self):
        return {
            'doc_id': self.doc_id,
            'employee_id': self.employee_id,
            'f_status': self.f_status,
            'documentation': self.documentation,
            'r_type': self.r_type
        }
