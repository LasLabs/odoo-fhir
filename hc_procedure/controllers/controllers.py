# -*- coding: utf-8 -*-
from openerp import http

# class HcProcedure(http.Controller):
#     @http.route('/hc_procedure/hc_procedure/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_procedure/hc_procedure/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_procedure.listing', {
#             'root': '/hc_procedure/hc_procedure',
#             'objects': http.request.env['hc_procedure.hc_procedure'].search([]),
#         })

#     @http.route('/hc_procedure/hc_procedure/objects/<model("hc_procedure.hc_procedure"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_procedure.object', {
#             'object': obj
#         })