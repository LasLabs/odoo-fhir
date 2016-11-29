# -*- coding: utf-8 -*-
from openerp import http

# class HcMesssageDefinition(http.Controller):
#     @http.route('/hc_messsage_definition/hc_messsage_definition/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_messsage_definition/hc_messsage_definition/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_messsage_definition.listing', {
#             'root': '/hc_messsage_definition/hc_messsage_definition',
#             'objects': http.request.env['hc_messsage_definition.hc_messsage_definition'].search([]),
#         })

#     @http.route('/hc_messsage_definition/hc_messsage_definition/objects/<model("hc_messsage_definition.hc_messsage_definition"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_messsage_definition.object', {
#             'object': obj
#         })