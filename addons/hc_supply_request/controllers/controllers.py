# -*- coding: utf-8 -*-
from openerp import http

# class HcSupplyRequest(http.Controller):
#     @http.route('/hc_supply_request/hc_supply_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_supply_request/hc_supply_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_supply_request.listing', {
#             'root': '/hc_supply_request/hc_supply_request',
#             'objects': http.request.env['hc_supply_request.hc_supply_request'].search([]),
#         })

#     @http.route('/hc_supply_request/hc_supply_request/objects/<model("hc_supply_request.hc_supply_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_supply_request.object', {
#             'object': obj
#         })