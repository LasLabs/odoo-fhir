# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Basic(models.Model):    
    _name = "hc.res.basic"    
    _description = "Basic"        

    identifier_ids = fields.One2many(
        comodel_name="hc.basic.identifier", 
        inverse_name="basic_id", 
        string="Identifiers", help="Business identifier.")                
    code_id = fields.Many2one(
        comodel_name="hc.vs.basic.resource.type", 
        string="Code", 
        required="True", 
        help="Kind of Resource.")                
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Practitioner", "Practitioner"), 
            ("Device", "Device")], 
            help='Type of resource instance that is the "focus" of this resource.')                
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help='Identifies the patient, practitioner, device or any other resource that is the "focus" of this resource.')                
    subject_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Subject Patient", 
        help='Patient that is the "focus" of this resource.')                
    subject_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Subject Practitioner", 
        help='Practitioner that is the "focus" of this resource.')                
    subject_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Subject Device", 
        help='Device that is the "focus" of this resource.')                
    created = fields.Date(
        string="Basic Creation Date", 
        help="When created.")                
    author_type = fields.Selection(
        string="Author Type", 
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Patient", "Patient"), 
            ("Related Person", "Related Person")], 
        help="Type of who created.")                
    author_name = fields.Char(
        string="Author", 
        compute="_compute_author_name", 
        store="True", 
        help="Who created.")                
    author_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Author Practitioner", 
        help="Practitioner who created.")                
    author_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Author Patient", 
        help="Patient who created.")                
    author_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Author Related Person", 
        help="Related Person who created.")                

class BasicIdentifier(models.Model):    
    _name = "hc.basic.identifier"    
    _description = "Basic Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]
    
    basic_id = fields.Many2one(
        comodel_name="hc.res.basic", 
        string="Basic", 
        help="Basic associated with this Basic Identifier." )                

class BasicResourceType(models.Model):    
    _name = "hc.vs.basic.resource.type"    
    _description = "Basic Resource Type"        
    _inherit = ["hc.value.set.contains"]
