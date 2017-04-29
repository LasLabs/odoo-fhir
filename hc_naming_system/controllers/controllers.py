# -*- coding: utf-8 -*-
from openerp import http

# class HcNamingSystem(http.Controller):
#     @http.route('/hc_naming_system/hc_naming_system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_naming_system/hc_naming_system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_naming_system.listing', {
#             'root': '/hc_naming_system/hc_naming_system',
#             'objects': http.request.env['hc_naming_system.hc_naming_system'].search([]),
#         })

#     @http.route('/hc_naming_system/hc_naming_system/objects/<model("hc_naming_system.hc_naming_system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_naming_system.object', {
#             'object': obj
#         })