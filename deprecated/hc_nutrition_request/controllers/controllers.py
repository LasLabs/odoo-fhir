# -*- coding: utf-8 -*-
from openerp import http

# class HcNutritionRequest(http.Controller):
#     @http.route('/hc_nutrition_request/hc_nutrition_request/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_nutrition_request/hc_nutrition_request/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_nutrition_request.listing', {
#             'root': '/hc_nutrition_request/hc_nutrition_request',
#             'objects': http.request.env['hc_nutrition_request.hc_nutrition_request'].search([]),
#         })

#     @http.route('/hc_nutrition_request/hc_nutrition_request/objects/<model("hc_nutrition_request.hc_nutrition_request"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_nutrition_request.object', {
#             'object': obj
#         })