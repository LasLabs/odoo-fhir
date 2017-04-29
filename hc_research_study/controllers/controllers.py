# -*- coding: utf-8 -*-
from openerp import http

# class HcResearchStudy(http.Controller):
#     @http.route('/hc_research_study/hc_research_study/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_research_study/hc_research_study/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_research_study.listing', {
#             'root': '/hc_research_study/hc_research_study',
#             'objects': http.request.env['hc_research_study.hc_research_study'].search([]),
#         })

#     @http.route('/hc_research_study/hc_research_study/objects/<model("hc_research_study.hc_research_study"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_research_study.object', {
#             'object': obj
#         })