# -*- coding: utf-8 -*-
from openerp import http

# class HcQuestionnaire(http.Controller):
#     @http.route('/hc_questionnaire/hc_questionnaire/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_questionnaire/hc_questionnaire/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_questionnaire.listing', {
#             'root': '/hc_questionnaire/hc_questionnaire',
#             'objects': http.request.env['hc_questionnaire.hc_questionnaire'].search([]),
#         })

#     @http.route('/hc_questionnaire/hc_questionnaire/objects/<model("hc_questionnaire.hc_questionnaire"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_questionnaire.object', {
#             'object': obj
#         })