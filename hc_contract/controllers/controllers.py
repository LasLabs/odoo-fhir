# -*- coding: utf-8 -*-
from openerp import http

# class HcContract(http.Controller):
#     @http.route('/hc_contract/hc_contract/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_contract/hc_contract/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_contract.listing', {
#             'root': '/hc_contract/hc_contract',
#             'objects': http.request.env['hc_contract.hc_contract'].search([]),
#         })

#     @http.route('/hc_contract/hc_contract/objects/<model("hc_contract.hc_contract"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_contract.object', {
#             'object': obj
#         })