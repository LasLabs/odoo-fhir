# -*- coding: utf-8 -*-
from openerp import http

# class HcPerson(http.Controller):
#     @http.route('/hc_person/hc_person/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hc_person/hc_person/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hc_person.listing', {
#             'root': '/hc_person/hc_person',
#             'objects': http.request.env['hc_person.hc_person'].search([]),
#         })

#     @http.route('/hc_person/hc_person/objects/<model("hc_person.hc_person"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hc_person.object', {
#             'object': obj
#         })