# -*- coding: utf-8 -*-
from openerp import http

# class HcAppointment(http.Controller):
#     @http.route('/hc_appointment/hc_appointment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_appointment/hc_appointment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_appointment.listing', {
#             'root': '/hc_appointment/hc_appointment',
#             'objects': http.request.env['hc_appointment.hc_appointment'].search([]),
#         })

#     @http.route('/hc_appointment/hc_appointment/objects/<model("hc_appointment.hc_appointment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_appointment.object', {
#             'object': obj
#         })