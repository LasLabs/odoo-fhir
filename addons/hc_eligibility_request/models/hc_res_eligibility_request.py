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
    status = fields.Char(
        string="Status", 
        selection=[
            ("active", "Active"), 
            ("cancelled", "Cancelled"), 
            ("draft", "Draft"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="The status of the resource instance.")
    priority_id = fields.Many2one(
        comodel_name="hc.vs.process.priority", 
        string="Priority", 
        help="Desired processing priority.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient",
        help="The subject of the Products and Services.")
    serviced_type = fields.Selection(
        string="Serviced Type", 
        selection=[
            ("date", "Date"), 
            ("period", "Period")], 
        help="Type of who recorded the sensitivity.")
    serviced_name = fields.Char(
        string="Serviced", 
        compute="_compute_serviced_name", 
        store="True", 
        help="Estimated date or dates of Service.")
    serviced_date = fields.Date(
        string="Serviced Date", 
        help="Code of estimated date or dates of service.")
    serviced_start_date = fields.Datetime(
        string="Serviced Start Date", 
        help="Start of estimated date or dates of service.")
    serviced_end_date = fields.Datetime(
        string="Serviced End Date", 
        help="End of estimated date or dates of service.")
    created = fields.Datetime(
        string="Created", 
        help="Creation date.")
    enterer_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Enterer", 
        help="Author.")
    provider_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Provider", 
        help="Responsible practitioner.")
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Responsible organization.")
    insurer_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Insurer", 
        help="Target.")
    facility_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Facility", 
        help="Servicing Facility.")
    coverage_id = fields.Many2one(
        comodel_name="hc.res.coverage", 
        string="Coverage", 
        help="Insurance or medical plan.")
    business_arrangement = fields.Char(
        string="Business Arrangement", 
        help="Business agreement.")
    benefit_category_id = fields.Many2one(
        comodel_name="hc.vs.benefit.category", 
        string="Benefit Category", 
        help="Benefit Category.")
    benefit_sub_category_id = fields.Many2one(
        comodel_name="hc.vs.benefit.sub.category", 
        string="Benefit Sub Category", 
        help="Benefit SubCategory.")

class EligibilityRequestIdentifier(models.Model):    
    _name = "hc.eligibility.request.identifier"    
    _description = "Eligibility Request Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    eligibility_request_id = fields.Many2one(
        comodel_name="hc.res.eligibility.request", 
        string="Eligibility Request", 
        help="Eligibility Request associated with this Eligibility Request Identifier.")                

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

class BenefitNetwork(models.Model):    
    _name = "hc.vs.benefit.network"    
    _description = "Benefit Network"        
    _inherit = ["hc.value.set.contains"]

class BenefitUnit(models.Model):    
    _name = "hc.vs.benefit.unit"    
    _description = "Benefit Unit"        
    _inherit = ["hc.value.set.contains"]

class BenefitTerm(models.Model):    
    _name = "hc.vs.benefit.term"    
    _description = "Benefit Term"        
    _inherit = ["hc.value.set.contains"]