# -*- coding: utf-8 -*-
from openerp import http

# class HcLibrary(http.Controller):
#     @http.route('/hc_library/hc_library/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_library/hc_library/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_library.listing', {
#             'root': '/hc_library/hc_library',
#             'objects': http.request.env['hc_library.hc_library'].search([]),
#         })

#     @http.route('/hc_library/hc_library/objects/<model("hc_library.hc_library"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_library.object', {
#             'object': obj
#         })