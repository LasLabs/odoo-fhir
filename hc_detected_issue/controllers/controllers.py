# -*- coding: utf-8 -*-
from openerp import http

# class HcDetectedIssue(http.Controller):
#     @http.route('/hc_detected_issue/hc_detected_issue/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_detected_issue/hc_detected_issue/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_detected_issue.listing', {
#             'root': '/hc_detected_issue/hc_detected_issue',
#             'objects': http.request.env['hc_detected_issue.hc_detected_issue'].search([]),
#         })

#     @http.route('/hc_detected_issue/hc_detected_issue/objects/<model("hc_detected_issue.hc_detected_issue"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_detected_issue.object', {
#             'object': obj
#         })