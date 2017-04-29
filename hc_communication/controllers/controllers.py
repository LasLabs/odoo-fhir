# -*- coding: utf-8 -*-
from openerp import http

# class HcCommunication(http.Controller):
#     @http.route('/hc_communication/hc_communication/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_communication/hc_communication/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_communication.listing', {
#             'root': '/hc_communication/hc_communication',
#             'objects': http.request.env['hc_communication.hc_communication'].search([]),
#         })

#     @http.route('/hc_communication/hc_communication/objects/<model("hc_communication.hc_communication"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_communication.object', {
#             'object': obj
#         })