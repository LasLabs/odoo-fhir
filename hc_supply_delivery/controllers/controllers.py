# -*- coding: utf-8 -*-
from openerp import http

# class HcSupplyDelivery(http.Controller):
#     @http.route('/hc_supply_delivery/hc_supply_delivery/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_supply_delivery/hc_supply_delivery/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_supply_delivery.listing', {
#             'root': '/hc_supply_delivery/hc_supply_delivery',
#             'objects': http.request.env['hc_supply_delivery.hc_supply_delivery'].search([]),
#         })

#     @http.route('/hc_supply_delivery/hc_supply_delivery/objects/<model("hc_supply_delivery.hc_supply_delivery"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_supply_delivery.object', {
#             'object': obj
#         })