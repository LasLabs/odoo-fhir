# -*- coding: utf-8 -*-

from openerp import models, fields, api

class EligibilityRequest(models.Model):    
    _name = "hc.res.eligibility.request"    
    _description = "Eligibility Request"        
    
    identifier_ids = fields.One2many(
        comodel_name="hc.eligibility.request.identifier", 
        inverse_name="eligibility_request_id", 
        string="Identifiers", 
        help="Business Identifier.")                
    outcome = fields.Selection(
        string="Eligibility Request Outcome", 
        required="True", 
        selection=[
            ("active", "Active"), 
            ("cancelled", "Cancelled"), 
            ("draft", "Draft"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="Transaction status: error, complete.")                
    ruleset_id = fields.Many2one(
        comodel_name="hc.vs.ruleset", 
        string="Ruleset", 
        help="Resource version.")                
    original_ruleset_id = fields.Many2one(
        comodel_name="hc.vs.ruleset", 
        string="Original Ruleset", 
        help="Original version.")                
    created = fields.Datetime(
        string="Eligibility Request Creation Date", 
        help="Creation date.")                
    insurer_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Insurer", 
        help="Target.")                
    provider_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Provider", 
        help="Responsible practitioner.")                
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Responsible organization.")                
    ruleset_id = fields.Many2one(
        comodel_name="hc.vs.process.priority", 
        string="Ruleset", 
        help="Desired processing priority.")                
    enterer_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Enterer", 
        help="Author.")                
    facility_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Facility", 
        help="Servicing Facility.")                
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="The subject of the Products and Services.")                
    coverage_id = fields.Many2one(
        comodel_name="hc.res.coverage", 
        string="Coverage", 
        help="Insurance or medical plan.")                
    business_arrangement = fields.Char(
        string="Eligibility Request Creation Date", 
        help="Business agreement.")                
    serviced_date = fields.Date(
        string="Serviced Date", 
        help="Code of estimated date or dates of service.")                
    ruleset_id = fields.Many2one(
        comodel_name="hc.vs.benefit.category", 
        string="Ruleset", 
        help="Benefit Category.")                
    ruleset_id = fields.Many2one(
        comodel_name="hc.vs.benefit.sub.category", 
        string="Ruleset", 
        help="Benefit Sub Category.")                

class EligibilityRequestIdentifier(models.Model):    
    _name = "hc.eligibility.request.identifier"    
    _description = "Eligibility Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    eligibility_request_id = fields.Many2one(
        comodel_name="hc.res.eligibility.request", 
        string="Eligibility Request", 
        help="Eligibility Request associated with this Eligibility Request Eligibility Request Identifier.")                

class Ruleset(models.Model):    
    _name = "hc.vs.ruleset"    
    _description = "Ruleset"        
    _inherit = ["hc.value.set.contains"]

class ProcessPriority(models.Model):    
    _name = "hc.vs.process.priority"    
    _description = "Process Priority"        
    _inherit = ["hc.value.set.contains"]

class BenefitCategory(models.Model):    
    _name = "hc.vs.benefit.category"    
    _description = "Benefit Category"        
    _inherit = ["hc.value.set.contains"]

class BenefitSubCategory(models.Model):    
    _name = "hc.vs.benefit.sub.category"    
    _description = "Benefit Sub Category"        
    _inherit = ["hc.value.set.contains"]
