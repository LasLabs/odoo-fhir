# -*- coding: utf-8 -*-

from openerp import models, fields, api

class SampledData(models.AbstractModel):    
    _name = "hc.sampled.data"    
    _description = "Sampled Data"

    origin = fields.Float(
        string="Origin", 
        required="True", 
        help="Zero value and units.")        
    origin_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Origin UOM", 
        required="True", 
        help="Origin unit of measure.")        
    period = fields.Float(
        string="Period", 
        required="True",
        default="0", 
        help="Number of milliseconds between samples.")        
    factor = fields.Float(
        string="Factor", 
        help="Multiply data by this before adding to origin.")        
    lower_limit = fields.Float(
        string="Lower Limit", 
        help="Lower limit of detection.")        
    upper_limit = fields.Float(
        string="Upper Limit", 
        help="Upper limit of detection.")        
    dimensions = fields.Integer(
        string="Dimensions", 
        required="True",
        default="1", 
        help="Number of sample points at each time point.")        
    data_type = fields.Selection(
        string="Data Type", 
        required="True", 
        selection=[
            ("Code", "Code"), 
            ("Series", "Series")], 
        help="Type of Who is responsible for the observation.")
    data_name = fields.Char(
        string="Data", 
        compute="compute_data_name", 
        help='Decimal values with spaces, or "E" | "U" | "L".')        
    data_code = fields.Selection(string="Data Code", 
        selection=[
            ("E", "E (Error)"), 
            ("L","L (Below Detected Limit)"), 
            ("U","U (Above detected limit)")], 
        help='The special values "E" (error), "L" (below detection limit) and "U" (above detection limit) can also be used in place of a decimal value.')        
    data_series = fields.Char(
        string="Data Series", 
        help="A series of data points which are decimal values separated by a single space (character u20).")        
