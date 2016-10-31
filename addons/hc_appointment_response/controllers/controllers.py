# -*- coding: utf-8 -*-
from openerp import http

# class HcAppointmentResponse(http.Controller):
#     @http.route('/hc_appointment_response/hc_appointment_response/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_appointment_response/hc_appointment_response/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_appointment_response.listing', {
#             'root': '/hc_appointment_response/hc_appointment_response',
#             'objects': http.request.env['hc_appointment_response.hc_appointment_response'].search([]),
#         })

#     @http.route('/hc_appointment_response/hc_appointment_response/objects/<model("hc_appointment_response.hc_appointment_response"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_appointment_response.object', {
#             'object': obj
#         })