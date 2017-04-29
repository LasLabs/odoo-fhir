# -*- coding: utf-8 -*-
from openerp import http

# class HcDevice(http.Controller):
#     @http.route('/hc_device/hc_device/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_device/hc_device/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_device.listing', {
#             'root': '/hc_device/hc_device',
#             'objects': http.request.env['hc_device.hc_device'].search([]),
#         })

#     @http.route('/hc_device/hc_device/objects/<model("hc_device.hc_device"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_device.object', {
#             'object': obj
#         })