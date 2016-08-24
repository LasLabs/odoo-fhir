# -*- coding: utf-8 -*-
from openerp import http

# class HcMedicationDispense(http.Controller):
#     @http.route('/hc_medication_dispense/hc_medication_dispense/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_medication_dispense/hc_medication_dispense/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_medication_dispense.listing', {
#             'root': '/hc_medication_dispense/hc_medication_dispense',
#             'objects': http.request.env['hc_medication_dispense.hc_medication_dispense'].search([]),
#         })

#     @http.route('/hc_medication_dispense/hc_medication_dispense/objects/<model("hc_medication_dispense.hc_medication_dispense"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_medication_dispense.object', {
#             'object': obj
#         })