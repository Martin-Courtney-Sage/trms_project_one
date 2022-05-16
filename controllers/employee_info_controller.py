from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from modules.employee_info import EmployeeInfo
from repositories.employee_info.employee_info_repo_impl import EmployeeInfoRepoImpl
from services.employee_info_service import EmployeeInfoService

er = EmployeeInfoRepoImpl()
es = EmployeeInfoService(er)


def route(app):

    @app.route("/employee/all", methods=['GET'])  # retrieve all employees
    def all_employee():
        try:
            return jsonify([employee_info.json() for employee_info in es.all_employee()]), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee/<employee_id>", methods=['GET'])  # retrieve specific employee
    def get_employee_by_id(employee_id):
        try:
            return es.get_employee(employee_id).json(), 200
        except ValueError as e:
            return "Not an existing Employee ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee", methods=['PUT'])  # update a specific employee
    def put_employee():
        body = request.json
        employee = EmployeeInfo(employee_id=body["employeeId"], f_name=body["fName"], l_name=body["lName"],
                                email=body["email"], position=body["position"])
        employee = es.update_employee(employee)

        try:
            return employee.json(), 201
        except ValueError as e:
            return "Not an existing Employee ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employee", methods=['POST'])  # create an employee
    def post_employee():
        body = request.json
        employee = EmployeeInfo(f_name=body["fName"], l_name=body["lName"],
                                email=body["email"], position=body["position"])
        employee = es.create_employee(employee)

        return employee.json(), 201

    @app.route("/employee/<employee_id>", methods=['DELETE'])  # delete an employee
    def del_employee(employee_id):
        es.delete_employee(employee_id)

        return f"{employee_id} has been deleted", 204
