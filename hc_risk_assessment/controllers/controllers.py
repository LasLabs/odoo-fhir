# -*- coding: utf-8 -*-
from openerp import http

# class HcRiskAssessment(http.Controller):
#     @http.route('/hc_risk_assessment/hc_risk_assessment/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_risk_assessment/hc_risk_assessment/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_risk_assessment.listing', {
#             'root': '/hc_risk_assessment/hc_risk_assessment',
#             'objects': http.request.env['hc_risk_assessment.hc_risk_assessment'].search([]),
#         })

#     @http.route('/hc_risk_assessment/hc_risk_assessment/objects/<model("hc_risk_assessment.hc_risk_assessment"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_risk_assessment.object', {
#             'object': obj
#         })