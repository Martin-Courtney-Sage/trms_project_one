from flask import Flask, render_template, request, redirect, url_for, session, flash
from exceptions.resource_not_found import ResourceNotFound
from modules.login import Login
from repositories.login.login_repo_impl import LoginRepoImpl
from services.login_service import LoginService

lr = LoginRepoImpl()
ls = LoginService(lr)


def route(app):
    # Get Login
    @app.route("/login/<main_id>", methods=['GET'])  # retrieves a login
    def get_login(main_id):
        try:
            return ls.get_login(main_id).json(), 200
        except ValueError as e:
            return "Not an existing Login", 400
        except ResourceNotFound as r:
            return r.message, 404

    # Update Login
    @app.route("/login/<main_id>", methods=['PUT'])
    def put_login(main_id):
        body = request.json
        log = Login(main_id=main_id, employee_id=body['employeeId'], username=body['username'],
                    passcode=body['passcode'])
        log = ls.update_login(log)
        try:
            return log.json(), 201
        except ValueError as e:
            return "Not an existing Login", 400
        except ResourceNotFound as r:
            return r.message, 404

    # Delete Login
    @app.route("/login/<main_id>", methods=['DELETE'])
    def delete_login(main_id):
        ls.delete_login(main_id)
        return "Login has been deleted"

    # Register Route / Create Login
    @app.route("/register", methods=['POST'])
    def register():
        body = request.json
        log = Login(employee_id=body['employeeId'], username=body['username'], passcode=body['passcode'])
        log = ls.create_login(log)
        return log.json(), 201

    # Login Route - found in backup.py (experimental)
