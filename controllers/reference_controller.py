from flask import request, jsonify
from exceptions.resource_not_found import ResourceNotFound
from modules.reference import Reference
from repositories.reference.reference_repo_impl import ReferenceRepoImpl
from services.reference_service import ReferenceService

rr = ReferenceRepoImpl()
rs = ReferenceService(rr)


def route(app):

    @app.route("/employee/trms/<doc_id>/reference", methods=['GET'])  # retrieve all references for a trms document
    def all_reference(doc_id):
        try:
            return jsonify([reference.json() for reference in rs.all_reference(doc_id)])
        except ValueError as e:
            return "Not an existing TRMS Document ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/reference/<ref_id>", methods=['GET'])  # retrieve specific reference
    def get_reference(ref_id):
        try:
            return rs.get_reference(ref_id).json(), 200
        except ValueError as e:
            return "Not an existing Reference ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/reference", methods=['POST'])  # create a reference for a trms document
    def post_reference():
        body = request.json
        reference = Reference(doc_id=body["docId"], g_scale=body["gScale"], g_earned=body["gEarned"], p_needed=body["pNeeded"],
                              p_success=body["pSuccess"])
        reference = rs.create_reference(reference)

        return reference.json(), 201

    @app.route("/reference", methods=['PUT'])  # update a reference
    def put_reference():
        body = request.json
        reference = Reference(ref_id=body["rId"], g_scale=body["gScale"], g_earned=body["gEarned"], p_needed=body["pNeeded"],
                              p_success=body["pSuccess"])
        reference = rs.update_reference(reference)

        try:
            return reference.json(), 201
        except ValueError as e:
            return "Not an existing Reference ID", 400
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/reference/<ref_id>", methods=['DELETE'])  # delete a reference
    def del_reference(ref_id):
        rs.delete_reference(ref_id)
        return f"{ref_id} has been deleted", 204
