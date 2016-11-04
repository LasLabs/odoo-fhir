# -*- coding: utf-8 -*-
from openerp import http

# class HcEnrollmentRequest(http.Controller):
#     @http.route('/hc_enrollment_request/hc_enrollment_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_enrollment_request/hc_enrollment_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_enrollment_request.listing', {
#             'root': '/hc_enrollment_request/hc_enrollment_request',
#             'objects': http.request.env['hc_enrollment_request.hc_enrollment_request'].search([]),
#         })

#     @http.route('/hc_enrollment_request/hc_enrollment_request/objects/<model("hc_enrollment_request.hc_enrollment_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_enrollment_request.object', {
#             'object': obj
#         })