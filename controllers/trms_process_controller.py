from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from modules.trms_process import TRMSProcess
from repositories.trms_process.trms_process_repo_impl import TRMSProcessRepoImpl
from services.trms_process_service import TRMSProcessService

tr = TRMSProcessRepoImpl()
ts = TRMSProcessService(tr)


def route(app):

    @app.route("/employee/<employee_id>/trms", methods=['GET'])  # retrieve all trms documents for specific employee
    def all_trms(employee_id):
        try:
            return jsonify([trms_process.json() for trms_process in ts.all_trms(employee_id)]), 200
        except ValueError as e:
            return "Not an existing Employee ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/trms/<doc_id>", methods=['GET'])  # retrieve a specific trms document
    def get_trms(doc_id):
        try:
            return ts.get_trms(doc_id).json(), 200
        except ValueError as e:
            return "Not an existing Employee ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/trms", methods=['POST'])  # create a trms document for employee
    def post_trms():
        body = request.json
        trms = TRMSProcess(employee_id=body["employeeId"], f_status=body["fStatus"], documentation=body["documentation"],
                           r_type=body["rType"])
        trms = ts.create_trms(trms)

        return trms.json(), 201

    @app.route("/trms", methods=['PUT'])  # updates a trms document
    def put_trms():
        body = request.json
        trms = TRMSProcess(doc_id=body["documentId"], f_status=body["fStatus"], documentation=body["documentation"], r_type=body["rType"])
        trms = tr.update_trms(trms)

        try:
            return trms.json(), 201
        except ValueError as e:
            return "Not an existing TRMS Document ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/trms/<doc_id>", methods=['DELETE'])  # deletes a trms document
    def del_trms(doc_id):
        ts.delete_trms(doc_id)
        return f"{doc_id} has been deleted", 204
