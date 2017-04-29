# -*- coding: utf-8 -*-
from openerp import http

# class HcBinary(http.Controller):
#     @http.route('/hc_binary/hc_binary/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_binary/hc_binary/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_binary.listing', {
#             'root': '/hc_binary/hc_binary',
#             'objects': http.request.env['hc_binary.hc_binary'].search([]),
#         })

#     @http.route('/hc_binary/hc_binary/objects/<model("hc_binary.hc_binary"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_binary.object', {
#             'object': obj
#         })