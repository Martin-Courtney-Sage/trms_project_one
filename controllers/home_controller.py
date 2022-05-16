# Place any/all Requests here that do not pertain to a specific Module


def route(app):

    @app.route("/home")
    def home():
        return "Welcome to TRMS, the Tuition Reimbursement Management System!!! :)"

    @app.route("/author")
    def author():
        return "Created by Courtney 'Sage' Martin. Email: courtney306@revature.net"



