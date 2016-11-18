# -*- coding: utf-8 -*-

from openerp import models, fields, api

class PaymentNotice(models.Model):    
    _name = "hc.res.payment.notice"    
    _description = "Payment Notice"        

    identifier_ids = fields.One2many(
        comodel_name="hc.payment.notice.identifier", 
        inverse_name="payment_notice_id", 
        string="Identifiers", 
        help="Business Identifier.")                
    status = fields.Selection(
        string="Payment Notice Status", 
        required="True", 
        selection=[
            ("active", "Active"), 
            ("cancelled", "Cancelled"), 
            ("draft", "Draft"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="The status of the resource instance.")                
    ruleset_id = fields.Many2one(
        comodel_name="hc.vs.ruleset", 
        string="Ruleset", 
        help="Resource version.")                
    original_ruleset_id = fields.Many2one(
        comodel_name="hc.vs.ruleset", 
        string="Original Ruleset", 
        help="Original version.")                
    created = fields.Datetime(
        string="Payment Notice Creation Date", 
        help="Creation date.")                
    target_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Target", 
        help="Insurer or Regulatory body.")                
    provider_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Provider", 
        help="Responsible practitioner.")                
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Responsible organization.")                
    supporting_information_type = fields.Selection(
        string="Supporting Information Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of request reference.")                
    request_name = fields.Char(
        string="Request", 
        compute="_compute_request_name", 
        store="True", 
        help="Request reference.")                
    request_string = fields.Char(
        string="Request String", 
        help="String of request reference.")                
    request_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Request Code", 
        help="Type of resource of request reference.")                
    supporting_information_type = fields.Selection(
        string="Supporting Information Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of response reference.")                
    response_name = fields.Char(
        string="Response", 
        compute="_compute_response_name", 
        store="True", help="Response reference.")                
    response_string = fields.Char(
        string="Response String",
        help="String of response reference.")                
    response_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Response Code", 
        help="Type of resource of response reference.")                
    payment_status_id = fields.Many2one(
        comodel_name="hc.vs.payment.status", 
        string="Payment Status", 
        required="True", 
        help="Status of the payment.")                
    status_date = fields.Date(
        string="Status Date", 
        help="Payment or clearing date.")                

class PaymentNoticeIdentifier(models.Model):    
    _name = "hc.payment.notice.identifier"    
    _description = "Payment Notice Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    payment_notice_id = fields.Many2one(
        comodel_name="hc.res.payment.notice", 
        string="Payment Notice", 
        help="Payment Notice associated with this Payment Notice Identifier.")                

class PaymentStatus(models.Model):    
    _name = "hc.vs.payment.status"    
    _description = "Payment Status"        
    _inherit = ["hc.value.set.contains"]
