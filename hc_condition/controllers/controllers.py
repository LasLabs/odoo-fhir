# -*- coding: utf-8 -*-
from openerp import http

# class HcCondition(http.Controller):
#     @http.route('/hc_condition/hc_condition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_condition/hc_condition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_condition.listing', {
#             'root': '/hc_condition/hc_condition',
#             'objects': http.request.env['hc_condition.hc_condition'].search([]),
#         })

#     @http.route('/hc_condition/hc_condition/objects/<model("hc_condition.hc_condition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_condition.object', {
#             'object': obj
#         })