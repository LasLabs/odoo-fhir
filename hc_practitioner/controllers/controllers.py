# -*- coding: utf-8 -*-
from openerp import http

# class HcPractitioner(http.Controller):
#     @http.route('/hc_practitioner/hc_practitioner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_practitioner/hc_practitioner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_practitioner.listing', {
#             'root': '/hc_practitioner/hc_practitioner',
#             'objects': http.request.env['hc_practitioner.hc_practitioner'].search([]),
#         })

#     @http.route('/hc_practitioner/hc_practitioner/objects/<model("hc_practitioner.hc_practitioner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_practitioner.object', {
#             'object': obj
#         })