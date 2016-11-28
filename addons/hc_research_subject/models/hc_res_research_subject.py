# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ResearchSubject(models.Model):    
    _name = "hc.res.research.subject"    
    _description = "Research Subject"            

    identifier_id = fields.Many2one(
        comodel_name="hc.research.subject.identifier", 
        string="Identifier", 
        help="Business Identifer for event.")                    
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("candidate", "Candidate"), 
            ("enrolled", "Enrolled"), 
            ("active", "Active"), 
            ("suspended", "Suspended"), 
            ("withdrawn", "Withdrawn"), 
            ("completed", "Completed")], 
        help="The current state of the event.")                    
    period_start_date = fields.Datetime(
        string="Period Start Date", 
        help="Start of participation.")                    
    period_end_date = fields.Datetime(
        string="Period End Date", 
        help="End of participation.")                    
    study_id = fields.Many2one(
        comodel_name="hc.res.research.study", 
        string="Study", 
        required="True", 
        help="Study subject is part of.")                    
    individual_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Individual", 
        required="True", 
        help="Who is part of study.")                    
    assigned_arm = fields.Char(
        string="Assigned Arm", 
        help="What path should be followed.")                    
    actual_arm = fields.Char(
        string="Actual Arm", 
        help="What path was followed.")                    
    consent_id = fields.Many2one(
        comodel_name="hc.res.consent", 
        string="Consent", 
        help="Agreement to participate in study.")                    

class ResearchSubjectIdentifier(models.Model):    
    _name = "hc.research.subject.identifier"    
    _description = "Research Subject Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

