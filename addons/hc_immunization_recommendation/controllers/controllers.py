# -*- coding: utf-8 -*-
from openerp import http

# class HcImmunizationRecommendation(http.Controller):
#     @http.route('/hc_immunization_recommendation/hc_immunization_recommendation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_immunization_recommendation/hc_immunization_recommendation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_immunization_recommendation.listing', {
#             'root': '/hc_immunization_recommendation/hc_immunization_recommendation',
#             'objects': http.request.env['hc_immunization_recommendation.hc_immunization_recommendation'].search([]),
#         })

#     @http.route('/hc_immunization_recommendation/hc_immunization_recommendation/objects/<model("hc_immunization_recommendation.hc_immunization_recommendation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_immunization_recommendation.object', {
#             'object': obj
#         })