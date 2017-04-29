# -*- coding: utf-8 -*-
from openerp import http

# class HcClinicalImpression(http.Controller):
#     @http.route('/hc_clinical_impression/hc_clinical_impression/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_clinical_impression/hc_clinical_impression/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_clinical_impression.listing', {
#             'root': '/hc_clinical_impression/hc_clinical_impression',
#             'objects': http.request.env['hc_clinical_impression.hc_clinical_impression'].search([]),
#         })

#     @http.route('/hc_clinical_impression/hc_clinical_impression/objects/<model("hc_clinical_impression.hc_clinical_impression"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_clinical_impression.object', {
#             'object': obj
#         })