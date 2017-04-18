# -*- coding: utf-8 -*-
from openerp import http

# class HcNutritionOrder(http.Controller):
#     @http.route('/hc_nutrition_order/hc_nutrition_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_nutrition_order/hc_nutrition_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_nutrition_order.listing', {
#             'root': '/hc_nutrition_order/hc_nutrition_order',
#             'objects': http.request.env['hc_nutrition_order.hc_nutrition_order'].search([]),
#         })

#     @http.route('/hc_nutrition_order/hc_nutrition_order/objects/<model("hc_nutrition_order.hc_nutrition_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_nutrition_order.object', {
#             'object': obj
#         })