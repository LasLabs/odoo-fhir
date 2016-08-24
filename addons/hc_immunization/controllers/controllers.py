# -*- coding: utf-8 -*-
from openerp import http

# class HcImmunization(http.Controller):
#     @http.route('/hc_immunization/hc_immunization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_immunization/hc_immunization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_immunization.listing', {
#             'root': '/hc_immunization/hc_immunization',
#             'objects': http.request.env['hc_immunization.hc_immunization'].search([]),
#         })

#     @http.route('/hc_immunization/hc_immunization/objects/<model("hc_immunization.hc_immunization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_immunization.object', {
#             'object': obj
#         })