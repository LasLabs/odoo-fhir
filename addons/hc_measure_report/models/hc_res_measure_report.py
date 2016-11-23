# -*- coding: utf-8 -*-

from openerp import models, fields, api

# class hc_measure_report(models.Model):
#     _name = 'hc_measure_report.hc_measure_report'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100