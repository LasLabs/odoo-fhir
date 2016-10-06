# -*- coding: utf-8 -*-
from openerp import http

# class HcConsent(http.Controller):
#     @http.route('/hc_consent/hc_consent/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_consent/hc_consent/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_consent.listing', {
#             'root': '/hc_consent/hc_consent',
#             'objects': http.request.env['hc_consent.hc_consent'].search([]),
#         })

#     @http.route('/hc_consent/hc_consent/objects/<model("hc_consent.hc_consent"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_consent.object', {
#             'object': obj
#         })