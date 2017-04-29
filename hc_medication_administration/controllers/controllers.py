# -*- coding: utf-8 -*-
from openerp import http

# class HcMedicationAdministration(http.Controller):
#     @http.route('/hc_medication_administration/hc_medication_administration/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_medication_administration/hc_medication_administration/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_medication_administration.listing', {
#             'root': '/hc_medication_administration/hc_medication_administration',
#             'objects': http.request.env['hc_medication_administration.hc_medication_administration'].search([]),
#         })

#     @http.route('/hc_medication_administration/hc_medication_administration/objects/<model("hc_medication_administration.hc_medication_administration"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_medication_administration.object', {
#             'object': obj
#         })