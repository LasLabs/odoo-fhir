# -*- coding: utf-8 -*-
from openerp import http

# class HcCarePlan(http.Controller):
#     @http.route('/hc_care_plan/hc_care_plan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_care_plan/hc_care_plan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_care_plan.listing', {
#             'root': '/hc_care_plan/hc_care_plan',
#             'objects': http.request.env['hc_care_plan.hc_care_plan'].search([]),
#         })

#     @http.route('/hc_care_plan/hc_care_plan/objects/<model("hc_care_plan.hc_care_plan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_care_plan.object', {
#             'object': obj
#         })