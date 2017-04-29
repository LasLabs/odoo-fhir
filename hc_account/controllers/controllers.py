# -*- coding: utf-8 -*-
from openerp import http

# class HcAccount(http.Controller):
#     @http.route('/hc_account/hc_account/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_account/hc_account/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_account.listing', {
#             'root': '/hc_account/hc_account',
#             'objects': http.request.env['hc_account.hc_account'].search([]),
#         })

#     @http.route('/hc_account/hc_account/objects/<model("hc_account.hc_account"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_account.object', {
#             'object': obj
#         })