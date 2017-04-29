# -*- coding: utf-8 -*-
from openerp import http

# class HcValueSet(http.Controller):
#     @http.route('/hc_value_set/hc_value_set/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_value_set/hc_value_set/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_value_set.listing', {
#             'root': '/hc_value_set/hc_value_set',
#             'objects': http.request.env['hc_value_set.hc_value_set'].search([]),
#         })

#     @http.route('/hc_value_set/hc_value_set/objects/<model("hc_value_set.hc_value_set"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_value_set.object', {
#             'object': obj
#         })