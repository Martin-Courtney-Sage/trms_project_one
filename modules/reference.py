
class Reference:

    def __init__(self, ref_id=0, doc_id=0, g_scale="", g_earned="", p_needed="", p_success=""):
        self.ref_id = ref_id
        self.doc_id = doc_id
        self.g_scale = g_scale
        self.g_earned = g_earned
        self.p_needed = p_needed
        self.p_success = p_success

    def __repr__(self):
        return str({
            'ref_id': self.ref_id,
            'doc_id': self.doc_id,
            'g_scale': self.g_scale,
            'g_earned': self.g_earned,
            'p_needed': self.p_needed,
            'p_success': self.p_success
        })

    def json(self):
        return{
            'ref_id': self.ref_id,
            'doc_id': self.doc_id,
            'g_scale': self.g_scale,
            'g_earned': self.g_earned,
            'p_needed': self.p_needed,
            'p_success': self.p_success
        }
