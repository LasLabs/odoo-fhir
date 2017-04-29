# -*- coding: utf-8 -*-
from openerp import http

# class HcPatient(http.Controller):
#     @http.route('/hc_patient/hc_patient/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_patient/hc_patient/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_patient.listing', {
#             'root': '/hc_patient/hc_patient',
#             'objects': http.request.env['hc_patient.hc_patient'].search([]),
#         })

#     @http.route('/hc_patient/hc_patient/objects/<model("hc_patient.hc_patient"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_patient.object', {
#             'object': obj
#         })