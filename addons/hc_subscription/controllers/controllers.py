# -*- coding: utf-8 -*-
from openerp import http

# class HcSubscription(http.Controller):
#     @http.route('/hc_subscription/hc_subscription/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_subscription/hc_subscription/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_subscription.listing', {
#             'root': '/hc_subscription/hc_subscription',
#             'objects': http.request.env['hc_subscription.hc_subscription'].search([]),
#         })

#     @http.route('/hc_subscription/hc_subscription/objects/<model("hc_subscription.hc_subscription"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_subscription.object', {
#             'object': obj
#         })