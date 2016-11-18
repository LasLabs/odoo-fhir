# -*- coding: utf-8 -*-

from openerp import models, fields, api

class PaymentReconciliation(models.Model):    
    _name = "hc.res.payment.reconciliation"    
    _description = "Payment Reconciliation"        

    identifier_ids = fields.One2many(
        comodel_name="hc.payment.reconciliation.identifier", 
        inverse_name="payment_reconciliation_id", 
        string="Identifiers", 
        help="Business Identifier.")                
    status = fields.Selection(
        string="Payment Reconciliation Status", 
        required="True", 
        selection=[
            ("active", "Active"), 
            ("cancelled", "Cancelled"), 
            ("draft", "Draft"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="The status of the resource instance.")                
    # request_id = fields.Many2one(
    #     comodel_name="hc.res.process.request", 
    #     string="Request", 
    #     help="Claim reference.")                
    outcome = fields.Selection(
        string="Outcome", 
        selection=[
            ("complete", "Complete"), 
            ("error", "Error"), 
            ("partial", "Partial")], 
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
        string="Created", 
        help="Creation date.")                
    period_start_date = fields.Datetime(
        string="Period Start Date", 
        help="Start of the period covered.")                
    period_end_date = fields.Datetime(
        string="Period End Date", 
        help="End of the period covered.")                
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", help="Insurer.")                
    request_provider_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Request Provider", 
        help="Responsible practitioner.")                
    request_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Request Organization", 
        help="Responsible organization.")                
    form_id = fields.Many2one(
        comodel_name="hc.vs.forms", 
        string="Form", 
        help="Printed Form Identifier.")                
    total = fields.Float(
        string="Total", 
        required="True", 
        help="Total amount of Payment.")                
    detail_ids = fields.One2many(
        comodel_name="hc.payment.reconciliation.detail", 
        inverse_name="payment_reconciliation_id", 
        string="Detail", 
        help="Details.")                
    note_ids = fields.One2many(
        comodel_name="hc.payment.reconciliation.note", 
        inverse_name="payment_reconciliation_id", 
        string="Note", 
        help="Note text.")                

class PaymentReconciliationDetail(models.Model):    
    _name = "hc.payment.reconciliation.detail"    
    _description = "Payment Reconciliation Detail"        

    payment_reconciliation_id = fields.Many2one(
        comodel_name="hc.res.payment.reconciliation", 
        string="Payment Reconciliation", 
        help="Payment Reconciliation associated with this Payment Reconciliation Detail.")                
    type_id = fields.Many2one(
        comodel_name="hc.vs.payment.type", 
        string="Type", 
        required="True", 
        help="Type code.")                
    request_type = fields.Selection(
        string="Request Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of claim.")                
    request_name = fields.Char(
        string="Request", 
        compute="_compute_request_name", 
        store="True", 
        help="Claim.")                
    request_string = fields.Char(
        string="Request String", 
        help="String of claim.")                
    request_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Request Code", 
        help="Type of resource of claim.")                
    response_type = fields.Selection(
        string="Response Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of claim response.")                
    response_name = fields.Char(
        string="Response", 
        compute="_compute_response_name", 
        store="True", 
        help="Claim Response.")                
    response_string = fields.Char(
        string="Response String", 
        help="String of claim response.")                
    response_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Response Code", 
        help="Type of resource of claim response.")                
    submitter_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Submitter", 
        help="Submitter.")                
    payee_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Payee", 
        help="Payee.")                
    date = fields.Date(
        string="Date", 
        help="Invoice date.")                
    amount = fields.Float(
        string="Amount", 
        help="Detail amount.")                

class PaymentReconciliationNote(models.Model):    
    _name = "hc.payment.reconciliation.note"    
    _description = "Payment Reconciliation Note"        

    payment_reconciliation_id = fields.Many2one(
        comodel_name="hc.res.payment.reconciliation", 
        string="Payment Reconciliation", 
        help="Payment Reconciliation associated with this Payment Reconciliation Note.")                
    type = fields.Selection(
        string="Type", 
        selection=[
            ("display", "Display"), 
            ("print", "Print"), 
            ("printoper", "Printoper")], 
        help="The note purpose: Print/Display.")                
    text = fields.Text(
        string="Text", 
        help="Notes text.")                

class PaymentReconciliationIdentifier(models.Model):    
    _name = "hc.payment.reconciliation.identifier"    
    _description = "Payment Reconciliation Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    payment_reconciliation_id = fields.Many2one(
        comodel_name="hc.res.payment.reconciliation", 
        string="Payment Reconciliation", 
        help="Payment Reconciliation associated with this Payment Reconciliation Identifier.")                

class PaymentType(models.Model):    
    _name = "hc.vs.payment.type"    
    _description = "Payment Type"       
    _inherit = ["hc.value.set.contains"]

