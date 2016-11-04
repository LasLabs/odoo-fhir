# -*- coding: utf-8 -*-
from openerp import http

# class HcExplanationOfBenefit(http.Controller):
#     @http.route('/hc_explanation_of_benefit/hc_explanation_of_benefit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_explanation_of_benefit/hc_explanation_of_benefit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_explanation_of_benefit.listing', {
#             'root': '/hc_explanation_of_benefit/hc_explanation_of_benefit',
#             'objects': http.request.env['hc_explanation_of_benefit.hc_explanation_of_benefit'].search([]),
#         })

#     @http.route('/hc_explanation_of_benefit/hc_explanation_of_benefit/objects/<model("hc_explanation_of_benefit.hc_explanation_of_benefit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_explanation_of_benefit.object', {
#             'object': obj
#         })