# -*- coding: utf-8 -*-
from openerp import http

# class HcDeviceUseRequest(http.Controller):
#     @http.route('/hc_device_use_request/hc_device_use_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_device_use_request/hc_device_use_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_device_use_request.listing', {
#             'root': '/hc_device_use_request/hc_device_use_request',
#             'objects': http.request.env['hc_device_use_request.hc_device_use_request'].search([]),
#         })

#     @http.route('/hc_device_use_request/hc_device_use_request/objects/<model("hc_device_use_request.hc_device_use_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_device_use_request.object', {
#             'object': obj
#         })