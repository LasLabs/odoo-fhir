# -*- coding: utf-8 -*-
from openerp import http

# class HcDeviceUseStatement(http.Controller):
#     @http.route('/hc_device_use_statement/hc_device_use_statement/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_device_use_statement/hc_device_use_statement/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_device_use_statement.listing', {
#             'root': '/hc_device_use_statement/hc_device_use_statement',
#             'objects': http.request.env['hc_device_use_statement.hc_device_use_statement'].search([]),
#         })

#     @http.route('/hc_device_use_statement/hc_device_use_statement/objects/<model("hc_device_use_statement.hc_device_use_statement"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_device_use_statement.object', {
#             'object': obj
#         })