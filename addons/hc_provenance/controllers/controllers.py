# -*- coding: utf-8 -*-
from openerp import http

# class HcProvenance(http.Controller):
#     @http.route('/hc_provenance/hc_provenance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_provenance/hc_provenance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_provenance.listing', {
#             'root': '/hc_provenance/hc_provenance',
#             'objects': http.request.env['hc_provenance.hc_provenance'].search([]),
#         })

#     @http.route('/hc_provenance/hc_provenance/objects/<model("hc_provenance.hc_provenance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_provenance.object', {
#             'object': obj
#         })