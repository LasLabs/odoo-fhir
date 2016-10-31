# -*- coding: utf-8 -*-
from openerp import http

# class HcSlot(http.Controller):
#     @http.route('/hc_slot/hc_slot/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_slot/hc_slot/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_slot.listing', {
#             'root': '/hc_slot/hc_slot',
#             'objects': http.request.env['hc_slot.hc_slot'].search([]),
#         })

#     @http.route('/hc_slot/hc_slot/objects/<model("hc_slot.hc_slot"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_slot.object', {
#             'object': obj
#         })