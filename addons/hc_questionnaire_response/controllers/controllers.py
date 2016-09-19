# -*- coding: utf-8 -*-
from openerp import http

# class HcQuestionnaireResponse(http.Controller):
#     @http.route('/hc_questionnaire_response/hc_questionnaire_response/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_questionnaire_response/hc_questionnaire_response/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_questionnaire_response.listing', {
#             'root': '/hc_questionnaire_response/hc_questionnaire_response',
#             'objects': http.request.env['hc_questionnaire_response.hc_questionnaire_response'].search([]),
#         })

#     @http.route('/hc_questionnaire_response/hc_questionnaire_response/objects/<model("hc_questionnaire_response.hc_questionnaire_response"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_questionnaire_response.object', {
#             'object': obj
#         })