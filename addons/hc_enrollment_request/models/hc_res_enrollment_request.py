# -*- coding: utf-8 -*-

from openerp import models, fields, api

class EnrollmentRequest(models.Model):    
    _name = "hc.res.enrollment.request"    
    _description = "Enrollment Request"        

    identifier_ids = fields.One2many(
    	comodel_name="hc.enrollment.request.identifier", 
    	inverse_name="enrollment_request_id", 
    	string="Identifiers", 
    	help="Business Identifier.")                
    status = fields.Selection(
    	string="Status", 
    	selection=[
    		("active", "Active"), 
    		("suspended", "Suspended"), 
    		("inactive", "Inactive"), 
    		("entered in error", "Entered In Error")], 
    	help="Indicates whether the care team is currently active, suspended, inactive, or entered in error.")                
    ruleset_id = fields.Many2one(
    	comodel_name="hc.vs.ruleset", 
    	string="Ruleset", 
    	help="Resource version.")                
    original_ruleset_id = fields.Many2one(
    	comodel_name="hc.vs.ruleset", 
    	string="Original Ruleset", 
    	help="Original version.")                
    created = fields.Datetime(
    	string="Enrollment Request Creation Date", 
    	help="Creation date.")                
    target_id = fields.Many2one(
    	comodel_name="hc.res.organization", 
    	string="Target", 
    	help="Insurer.")                
    provider_id = fields.Many2one(
    	comodel_name="hc.res.practitioner", 
    	string="Provider", 
    	help="Responsible practitioner.")                
    organization_id = fields.Many2one(
    	comodel_name="hc.res.organization", 
    	string="Organization", 
    	help="Responsible organization.")                
    subject_id = fields.Many2one(
    	comodel_name="hc.res.patient", 
    	string="Subject", 
    	required="True", 
    	help="The subject of the Products and Services.")                
    coverage_id = fields.Many2one(
    	comodel_name="hc.res.coverage", 
    	string="Coverage", 
    	required="True", 
    	help="Insurance information.")                
    relationship_id = fields.Many2one(
    	comodel_name="hc.vs.enrollment.relationship", 
    	string="Relationship", 
    	required="True", 
    	help="Patient relationship to subscriber.")                

class EnrollmentRequestIdentifier(models.Model):    
    _name = "hc.enrollment.request.identifier"    
    _description = "Enrollment Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    enrollment_request_id = fields.Many2one(
    	comodel_name="hc.res.enrollment.request", 
    	string="Enrollment Request", 
    	help="Enrollment Request associated with this Enrollment Request Identifier.")                

class EnrollmentRelationship(models.Model):    
    _name = "hc.vs.enrollment.relationship"    
    _description = "Enrollment Relationship"        
    _inherit = ["hc.value.set.contains"]
