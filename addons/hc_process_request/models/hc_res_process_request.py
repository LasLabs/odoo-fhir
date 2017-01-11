# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ProcessRequest(models.Model):    
    _name = "hc.res.process.request"    
    _description = "Process Request"            

    identifier_ids = fields.One2many(
        comodel_name="hc.process.request.identifier", 
        inverse_name="process_request_id", 
        string="Identifiers", 
        help="Business Identifier.")                    
    status = fields.Selection(
        string="Process Request Status", 
        selection=[
            ("active", "Active"), 
            ("cancelled", "Cancelled"), 
            ("draft", "Draft"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="The status of the resource instance.")                    
    action = fields.Selection(
        string="Process Request Action", 
        required="True", 
        selection=[
            ("cancel", "Cancel"), 
            ("poll", "Poll"), 
            ("reprocess", "Reprocess"), 
            ("status", "Status")], 
        help="The type of processing action being requested, for example Reversal, Readjudication, StatusRequest,PendedRequest.")                    
    target_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Target", 
        help="Target of the request.")                    
    created = fields.Datetime(
        string="Process Request Creation Date", 
        help="Creation date.")                    
    provider_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Provider", 
        help="Responsible practitioner.")                    
    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Responsible organization.")                    
    request_type = fields.Selection(
        string="Request Type", 
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
        help="Code request reference.")                    
    response_type = fields.Selection(
        string="Response Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of response reference.")                    
    response_name = fields.Char(
        string="Response", 
        compute="_compute_response_name", 
        store="True", 
        help="Response reference.")                    
    response_string = fields.Char(
        string="Response String", 
        help="String of response reference.")                    
    response_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Response Code", 
        help="Code response reference.")                    
    is_nullify = fields.Boolean(
        string="Nullify", 
        help="Nullify.")                    
    reference = fields.Char(
        string="Reference", 
        help="Reference number/string.")                    
    include_ids = fields.One2many(
        comodel_name="hc.process.request.include", 
        inverse_name="process_request_id", 
        string="Includes", 
        help="Resource type(s) to include.")                    
    exclude_ids = fields.One2many(
        comodel_name="hc.process.request.exclude", 
        inverse_name="process_request_id", 
        string="Excludes", 
        help="Resource type(s) to exclude.")                    
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the period.")                    
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the period.")
    item_ids = fields.One2many(
        comodel_name="hc.process.request.item", 
        inverse_name="process_request_id", 
        string="Items", 
        help="Items to re-adjudicate.")                    

class ProcessRequestItem(models.Model):    
    _name = "hc.process.request.item"    
    _description = "Process Request Item"            

    process_request_id = fields.Many2one(
        comodel_name="hc.res.process.request", 
        string="Process Request", 
        help="Process Request associated with this Item.")
    sequence_link_id = fields.Integer(
        string="Sequence Link Id", 
        required="True", 
        help="Service instance.")                    

class ProcessRequestIdentifier(models.Model):    
    _name = "hc.process.request.identifier"    
    _description = "Process Request Identifier"            
    _inherit = ["hc.basic.association", "hc.identifier"]

    process_request_id = fields.Many2one(
        comodel_name="hc.res.process.request", 
        string="Process Request", 
        help="Process Request associated with this Process Request Identifier.")                    

class ProcessRequestInclude(models.Model):    
    _name = "hc.process.request.include"    
    _description = "Process Request Include"            
    _inherit = ["hc.basic.association"]

    process_request_id = fields.Many2one(
        comodel_name="hc.res.process.request", 
        string="Process Request", 
        help="Process Request associated with this Process Request Include.")                    
    include = fields.Char(
        string="Include", 
        help="String associated with this Process Request Include.")                    

class ProcessRequestExclude(models.Model):    
    _name = "hc.process.request.exclude"    
    _description = "Process Request Exclude"            
    _inherit = ["hc.basic.association"]

    process_request_id = fields.Many2one(
        comodel_name="hc.res.process.request", 
        string="Process Request", 
        help="Process Request associated with this Process Request Exclude.")                    
    exclude = fields.Char(
        string="Exclude", 
        help="String associated with this Process Request Exclude.")                    
