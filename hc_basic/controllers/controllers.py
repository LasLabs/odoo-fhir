# -*- coding: utf-8 -*-
from openerp import http

# class HcBasic(http.Controller):
#     @http.route('/hc_basic/hc_basic/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_basic/hc_basic/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_basic.listing', {
#             'root': '/hc_basic/hc_basic',
#             'objects': http.request.env['hc_basic.hc_basic'].search([]),
#         })

#     @http.route('/hc_basic/hc_basic/objects/<model("hc_basic.hc_basic"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_basic.object', {
#             'object': obj
#         })