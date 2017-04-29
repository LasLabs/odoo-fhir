# -*- coding: utf-8 -*-
from openerp import http

# class HcBase(http.Controller):
#     @http.route('/hc_base/hc_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_base/hc_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_base.listing', {
#             'root': '/hc_base/hc_base',
#             'objects': http.request.env['hc_base.hc_base'].search([]),
#         })

#     @http.route('/hc_base/hc_base/objects/<model("hc_base.hc_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_base.object', {
#             'object': obj
#         })