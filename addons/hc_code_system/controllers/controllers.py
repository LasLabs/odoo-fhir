# -*- coding: utf-8 -*-
from openerp import http

# class HcCodeSystem(http.Controller):
#     @http.route('/hc_code_system/hc_code_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_code_system/hc_code_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_code_system.listing', {
#             'root': '/hc_code_system/hc_code_system',
#             'objects': http.request.env['hc_code_system.hc_code_system'].search([]),
#         })

#     @http.route('/hc_code_system/hc_code_system/objects/<model("hc_code_system.hc_code_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_code_system.object', {
#             'object': obj
#         })