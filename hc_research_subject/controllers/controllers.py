# -*- coding: utf-8 -*-
from openerp import http

# class HcResearchSubject(http.Controller):
#     @http.route('/hc_research_subject/hc_research_subject/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_research_subject/hc_research_subject/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_research_subject.listing', {
#             'root': '/hc_research_subject/hc_research_subject',
#             'objects': http.request.env['hc_research_subject.hc_research_subject'].search([]),
#         })

#     @http.route('/hc_research_subject/hc_research_subject/objects/<model("hc_research_subject.hc_research_subject"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_research_subject.object', {
#             'object': obj
#         })