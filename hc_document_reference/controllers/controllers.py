# -*- coding: utf-8 -*-
from openerp import http

# class HcDocumentReference(http.Controller):
#     @http.route('/hc_document_reference/hc_document_reference/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_document_reference/hc_document_reference/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_document_reference.listing', {
#             'root': '/hc_document_reference/hc_document_reference',
#             'objects': http.request.env['hc_document_reference.hc_document_reference'].search([]),
#         })

#     @http.route('/hc_document_reference/hc_document_reference/objects/<model("hc_document_reference.hc_document_reference"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_document_reference.object', {
#             'object': obj
#         })