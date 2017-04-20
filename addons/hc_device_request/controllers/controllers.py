# -*- coding: utf-8 -*-
from openerp import http

# class HcDeviceRequest(http.Controller):
#     @http.route('/hc_device_request/hc_device_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_device_request/hc_device_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_device_request.listing', {
#             'root': '/hc_device_request/hc_device_request',
#             'objects': http.request.env['hc_device_request.hc_device_request'].search([]),
#         })

#     @http.route('/hc_device_request/hc_device_request/objects/<model("hc_device_request.hc_device_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_device_request.object', {
#             'object': obj
#         })