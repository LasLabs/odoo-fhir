# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ProcessResponse(models.Model):    
    _name = "hc.res.process.response"    
    _description = "Process Response"            

    identifier_ids = fields.One2many(comodel_name="hc.process.response.identifier", inverse_name="process_response_id", string="Identifiers", help="Business Identifier.")                    
    status = fields.Selection(string="Process Response Status", selection=[("active", "Active"), ("cancelled", "Cancelled"), ("draft", "Draft"), ("entered-in-error", "Entered-In-Error")], help="The status of the resource instance.")                    
    created = fields.Datetime(string="Process Response Creation Date", help="Creation date.")                    
    organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Organization", help="Authoring Organization.")                    
    request_type = fields.Selection(string="Request Type", selection=[("string", "String"), ("code", "Code")], help="Type of request reference.")                    
    request_name = fields.Char(string="Request", compute="_compute_request_name", store="True", help="Request reference.")                    
    request_string = fields.Char(string="Request String", help="String of request reference.")                    
    request_code_id = fields.Many2one(comodel_name="hc.vs.resource.type", string="Request Code", help="Code request reference.")                    
    outcome_id = fields.Many2one(comodel_name="hc.vs.process.outcome", string="Outcome", help="Processing outcome.")                    
    disposition = fields.Char(string="Disposition", help="Disposition Message.")                    
    request_provider_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Request Provider", help="Responsible Practitioner.")                    
    request_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Request Organization", help="Responsible organization.")                    
    form_id = fields.Many2one(comodel_name="hc.vs.forms", string="Form", help="Printed Form Identifier.")                    
    error_ids = fields.Many2many(comodel_name="hc.vs.adjudication.error", relation="process_response_error_rel", string="Errors", help="Error code.")                    
    communication_request_ids = fields.One2many(comodel_name="hc.process.response.communication.request", inverse_name="process_response_id", string="Communication Requests", help="Request for additional information.")                    
    process_note_ids = fields.One2many(comodel_name="hc.process.response.process.note", inverse_name="process_response_id", string="Process Notes", help="Processing comments or additional requirements.")                    

class ProcessResponseProcessNote(models.Model):    
    _name = "hc.process.response.process.note"    
    _description = "Process Response Process Note"            

    process_response_id = fields.Many2one(comodel_name="hc.res.process.response", string="Process Response", help="Process Response associated with this Process Response Process Note.")                    
    type = fields.Selection(string="Type", selection=[("display", "Display"), ("print", "Print"), ("printoper", "Printoper")], help="The note purpose: Print/Display.")                    
    text = fields.Char(string="Text", help="Notes text.")                    

class ProcessResponseIdentifier(models.Model):    
    _name = "hc.process.response.identifier"    
    _description = "Process Response Identifier"            
    _inherit = ["hc.basic.association", "hc.identifier"]

    process_response_id = fields.Many2one(comodel_name="hc.res.process.response", string="Process Response", help="Process Response associated with this Process Response Identifier.")                    

class ProcessResponseCommunicationRequest(models.Model):    
    _name = "hc.process.response.communication.request"    
    _description = "Process Response Communication Request"            
    _inherit = ["hc.basic.association"]

    process_response_id = fields.Many2one(comodel_name="hc.res.process.response", string="Process Response", help="Process Response associated with this Process Response Communication Request.")                    
    communication_request_id = fields.Many2one(comodel_name="hc.res.communication.request", string="Communication Request", help="CommunicationRequest associated with this Process Response Communication Request.")                    

class ProcessOutcome(models.Model):    
    _name = "hc.vs.process.outcome"    
    _description = "Process Outcome"            
    _inherit = ["hc.value.set.contains"]
