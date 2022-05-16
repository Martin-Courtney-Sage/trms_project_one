# Route to the App to connect all the Controllers Here

from controllers import home_controller, trms_process_controller, employee_info_controller, reference_controller, login_controller


def route(app):
    # Call all the other controllers
    home_controller.route(app)
    employee_info_controller.route(app)
    trms_process_controller.route(app)
    reference_controller.route(app)
    login_controller.route(app)
