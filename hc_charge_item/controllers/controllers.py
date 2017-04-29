# -*- coding: utf-8 -*-
from openerp import http

# class HcChargeItem(http.Controller):
#     @http.route('/hc_charge_item/hc_charge_item/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_charge_item/hc_charge_item/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_charge_item.listing', {
#             'root': '/hc_charge_item/hc_charge_item',
#             'objects': http.request.env['hc_charge_item.hc_charge_item'].search([]),
#         })

#     @http.route('/hc_charge_item/hc_charge_item/objects/<model("hc_charge_item.hc_charge_item"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_charge_item.object', {
#             'object': obj
#         })