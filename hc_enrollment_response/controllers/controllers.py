# -*- coding: utf-8 -*-
from openerp import http

# class HcEnrollmentResponse(http.Controller):
#     @http.route('/hc_enrollment_response/hc_enrollment_response/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_enrollment_response/hc_enrollment_response/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_enrollment_response.listing', {
#             'root': '/hc_enrollment_response/hc_enrollment_response',
#             'objects': http.request.env['hc_enrollment_response.hc_enrollment_response'].search([]),
#         })

#     @http.route('/hc_enrollment_response/hc_enrollment_response/objects/<model("hc_enrollment_response.hc_enrollment_response"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_enrollment_response.object', {
#             'object': obj
#         })