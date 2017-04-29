# -*- coding: utf-8 -*-
from openerp import http

# class HcImplementationGuide(http.Controller):
#     @http.route('/hc_implementation_guide/hc_implementation_guide/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_implementation_guide/hc_implementation_guide/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_implementation_guide.listing', {
#             'root': '/hc_implementation_guide/hc_implementation_guide',
#             'objects': http.request.env['hc_implementation_guide.hc_implementation_guide'].search([]),
#         })

#     @http.route('/hc_implementation_guide/hc_implementation_guide/objects/<model("hc_implementation_guide.hc_implementation_guide"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_implementation_guide.object', {
#             'object': obj
#         })