# -*- coding: utf-8 -*-
from openerp import http

# class HcFlag(http.Controller):
#     @http.route('/hc_flag/hc_flag/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_flag/hc_flag/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_flag.listing', {
#             'root': '/hc_flag/hc_flag',
#             'objects': http.request.env['hc_flag.hc_flag'].search([]),
#         })

#     @http.route('/hc_flag/hc_flag/objects/<model("hc_flag.hc_flag"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_flag.object', {
#             'object': obj
#         })