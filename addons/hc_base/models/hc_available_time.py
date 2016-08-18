# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AvailableTime(models.Model):  
    _name = "hc.available.time" 
    _description = "Available Time"
     
    days_of_week_ids = fields.Many2many(
        comodel_name="hc.vs.days.of.week",
        string="Days Of Week", 
        help="The days of the week.")        
    is_all_day = fields.Boolean(
        string="All Day", 
        help="Always available? (e.g. 24 hour service).")       
    available_start_time = fields.Char(
        string="Available Start Time", 
        help="Opening time of day (ignored if allDay = true).")       
    available_end_time = fields.Char(
        string="Available End Time", 
        help="Closing time of day (ignored if allDay = true).") 

class NotAvailableTime(models.Model):   
    _name = "hc.not.available.time" 
    _description = "Not Available Time"     

    description = fields.Text(
        string="Description", 
        help="Reason presented to the user explaining why time not available.")             
    not_available_start_time = fields.Char(
        string="Not Available Start Time", 
        help="Start of the period service not available from this date.")             
    not_available_end_time = fields.Char(
        string="Not Available End Time", 
        help="End of the period service not available from this date.")