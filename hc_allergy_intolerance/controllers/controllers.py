# -*- coding: utf-8 -*-
from openerp import http

# class HcAllergyIntolerance(http.Controller):
#     @http.route('/hc_allergy_intolerance/hc_allergy_intolerance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_allergy_intolerance/hc_allergy_intolerance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_allergy_intolerance.listing', {
#             'root': '/hc_allergy_intolerance/hc_allergy_intolerance',
#             'objects': http.request.env['hc_allergy_intolerance.hc_allergy_intolerance'].search([]),
#         })

#     @http.route('/hc_allergy_intolerance/hc_allergy_intolerance/objects/<model("hc_allergy_intolerance.hc_allergy_intolerance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_allergy_intolerance.object', {
#             'object': obj
#         })