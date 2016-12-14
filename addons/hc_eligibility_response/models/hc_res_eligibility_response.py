# -*- coding: utf-8 -*-

from openerp import models, fields, api

class EligibilityResponse(models.Model):    
    _name = "hc.res.eligibility.response"    
    _description = "Eligibility Response"        

    identifier_ids = fields.One2many(
        comodel_name="hc.eligibility.response.identifier", 
        inverse_name="eligibility_response_id", 
        string="Identifiers", 
        help="Business Identifier.")                
    status = fields.Selection(
        string="Eligibility Response Status", 
        required="True", 
        selection=[
            ("active", "Active"), 
            ("cancelled", "Cancelled"), 
            ("draft", "Draft"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="Transaction status: error, complete.")                
    request_id = fields.Many2one(
        comodel_name="hc.res.eligibility.request", 
        string="Request", 
        help="Claim reference.")                
    outcome = fields.Selection(
        string="Eligibility Response Outcome", 
        selection=[
            ("complete", "Complete"), 
            ("error", "Error")], 
        help="Transaction status: error, complete.")                
    disposition = fields.Text(
        string="Disposition", 
        help="Disposition Message.")                
    ruleset_id = fields.Many2one(
        comodel_name="hc.vs.ruleset", 
        string="Ruleset", 
        help="Resource version.")                
    original_ruleset_id = fields.Many2one(
        comodel_name="hc.vs.ruleset", 
        string="Original Ruleset", 
        help="Original version.")                
    created = fields.Datetime(
        string="Eligibility Response Creation Date", 
        help="Creation date.")                
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Insurer.")                
    request_provider_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Request Provider", 
        help="Responsible practitioner.")                
    request_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Request Organization", 
        help="Responsible organization.")                
    is_inforce = fields.Boolean(
        string="Inforce", 
        help="Coverage inforce.")                
    # contract_id = fields.Many2one(
    #     comodel_name="hc.res.contract", 
    #     string="Contract", 
    #     help="Contract details.")                
    form_id = fields.Many2one(
        comodel_name="hc.vs.forms", 
        string="Form", 
        help="Printed Form Identifier.")                
    benefit_balance_ids = fields.One2many(
        comodel_name="hc.eligibility.response.benefit.balance", 
        inverse_name="eligibility_response_id", 
        string="Benefit Balances", 
        help="Benefits by Category.")                
    error_ids = fields.One2many(
        comodel_name="hc.eligibility.response.error", 
        inverse_name="eligibility_response_id", 
        string="Errors", 
        help="Processing errors.")                

class EligibilityResponseBenefitBalance(models.Model):    
    _name = "hc.eligibility.response.benefit.balance"    
    _description = "Eligibility Response Benefit Balance"        

    eligibility_response_id = fields.Many2one(
        comodel_name="hc.res.eligibility.response", 
        string="Eligibility Response", 
        help="Eligibility Response associated with this Eligibility Response Benefit Balance.")                
    category_id = fields.Many2one(
        comodel_name="hc.vs.benefit.category", 
        string="Category", 
        required="True", 
        help="Benefit Category.")                
    sub_category_id = fields.Many2one(
        comodel_name="hc.vs.benefit.sub.category", 
        string="Sub Category", 
        help="Benefit SubCategory.")                
    name = fields.Char(
        string="Name", 
        help="Short name for the benefit.")                
    description = fields.Text(
        string="Description", 
        help="Description of the benefit.")                
    network_id = fields.Many2one(
        comodel_name="hc.vs.benefit.network", 
        string="Network", 
        help="In or out of network.")                
    unit_id = fields.Many2one(
        comodel_name="hc.vs.benefit.unit", 
        string="Unit", 
        help="Individual or family.")                
    term_id = fields.Many2one(
        comodel_name="hc.vs.benefit.term", 
        string="Term", 
        help="Annual or lifetime.")                
    financial_ids = fields.One2many(
        comodel_name="hc.eligibility.response.benefit.balance.financial", 
        inverse_name="benefit_balance_id", 
        string="Financials", 
        help="Benefit Summary.")                

class EligibilityResponseBenefitBalanceFinancial(models.Model):    
    _name = "hc.eligibility.response.benefit.balance.financial"    
    _description = "Eligibility Response Benefit Balance Financial"        

    benefit_balance_id = fields.Many2one(
        comodel_name="hc.eligibility.response.benefit.balance", 
        string="Benefit Balance", 
        help="Benefit Balance associated with this Eligibility Response Benefit Balance Financial.")                
    type_id = fields.Many2one(
        comodel_name="hc.vs.benefit.code", 
        string="Type", 
        required="True", 
        help="Deductable, visits, benefit amount.")                
    benefit_type = fields.Selection(
        string="Benefit Type", 
        selection=[
            ("unsigned Int", "Unsigned Int"), 
            ("string", "String"), 
            ("Money", "Money")], 
        help="Type of benefits allowed.")                
    benefit_name = fields.Char(
        string="Benefit Name", 
        help="Benefits allowed.")                
    benefit_unsigned_int = fields.Integer(
        string="Benefit Unsigned Int", 
        help="Code of benefits allowed.")                
    benefit_string = fields.Char(
        string="Benefit String", 
        help="String of content of this set of documents.")                
    benefit_money = fields.Float(
        string="Benefit Money", 
        help="Money content of this set of documents.")                
    benefit_used_type = fields.Selection(
        string="Benefit Used Type", 
        selection=[
            ("unsigned Int", "Unsigned Int"), 
            ("Money", "Money")], 
        help="Type of benefits used.")                
    benefit_used_name = fields.Char(
        string="Benefit Used Name", 
        help="Benefits used.")                
    benefit_used_unsigned_int = fields.Integer(
        string="Benefit Used Unsigned Int", 
        help="Code of benefits used.")                
    benefit_used_money = fields.Float(
        string="Benefit Used Money", 
        help="Money content of this set of documents.")                

class EligibilityResponseError(models.Model):    
    _name = "hc.eligibility.response.error"    
    _description = "Eligibility Response Error"        

    eligibility_response_id = fields.Many2one(
        comodel_name="hc.res.eligibility.response", 
        string="Eligibility Response", 
        help="Eligibility Response associated with this Eligibility Response Error.")                
    code_id = fields.Many2one(
        comodel_name="hc.vs.adjudication.error", 
        string="Code", required="True", 
        help="Error code detailing processing issues.")                

class EligibilityResponseIdentifier(models.Model):    
    _name = "hc.eligibility.response.identifier"    
    _description = "Eligibility Response Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    eligibility_response_id = fields.Many2one(
        comodel_name="hc.res.eligibility.response", 
        string="Eligibility Response", 
        help="Eligibility Response associated with this Eligibility Response Identifier.")                

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

class BenefitCode(models.Model):    
    _name = "hc.vs.benefit.code"    
    _description = "Benefit Code"        
    _inherit = ["hc.value.set.contains"]

class AdjudicationError(models.Model):    
    _name = "hc.vs.adjudication.error"    
    _description = "Adjudication Error"        
    _inherit = ["hc.value.set.contains"]
