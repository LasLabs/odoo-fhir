# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Period(models.AbstractModel):    
    _name = "hc.period"    
    _description = "Period"

    start = fields.Datetime(
    	string="Start Datetime", 
    	help="Starting time with inclusive boundary.")        
    end = fields.Datetime(
    	string="End Datetime", 
    	help="End time with inclusive boundary, if not ongoing.")        

# Constraints

# If present, start SHALL have a lower value than end.