# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ContactDetail(models.Model):    
    _name = "hc.contact.detail"    
    _description = "Contact Detail"            

    name = fields.Char(
        string="Name", 
        help="Name of an individual to contact.")               
    telecom_ids = fields.One2many(
        comodel_name="hc.contact.detail.telecom", 
        inverse_name="contact_detail_id", 
        string="Telecoms", 
        help="Contact details for individual or organization.")                    

class ContactDetailTelecom(models.Model):    
    _name = "hc.contact.detail.telecom"    
    _description = "Contact Detail Telecom"        
    _inherit = ["hc.telecom.contact.point"]    
    _inherits = {"hc.telecom": "telecom_id"}

    telecom_id = fields.Many2one(
        comodel_name="hc.telecom", 
        string="Telecom", 
        ondelete="restrict", 
        required="True", 
        help="Telecom associated with this contact detail telecom.")
    contact_detail_id = fields.Many2one(
        comodel_name="hc.contact.detail", 
        string="Contact Detail", 
        help="Contact Detail associated with this contact detail telecom.")
