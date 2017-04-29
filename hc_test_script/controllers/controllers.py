# -*- coding: utf-8 -*-
from openerp import http

# class HcTestScript(http.Controller):
#     @http.route('/hc_test_script/hc_test_script/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_test_script/hc_test_script/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_test_script.listing', {
#             'root': '/hc_test_script/hc_test_script',
#             'objects': http.request.env['hc_test_script.hc_test_script'].search([]),
#         })

#     @http.route('/hc_test_script/hc_test_script/objects/<model("hc_test_script.hc_test_script"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_test_script.object', {
#             'object': obj
#         })