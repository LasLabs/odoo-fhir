# -*- coding: utf-8 -*-

from openerp import models, fields, api

class OperationOutcome(models.Model):    
    _name = "hc.res.operation.outcome"    
    _description = "Operation Outcome"        

    issue_ids = fields.One2many(
        comodel_name="hc.operation.outcome.issue", 
        inverse_name="operation_outcome_id", 
        string="Issues", 
        required="True", 
        help="A single issue associated with the action.")                

class OperationOutcomeIssue(models.Model):    
    _name = "hc.operation.outcome.issue"    
    _description = "Operation Outcome Issue"        

    operation_outcome_id = fields.Many2one(
        comodel_name="hc.res.operation.outcome", 
        string="Operation Outcome", 
        help="Operation Outcome associated with this Operation Outcome Issue.")                
    severity = fields.Selection(
        tring="Issue Severity", 
        required="True", 
        selection=[
            ("fatal", "Fatal"), 
            ("error", "Error"), 
            ("warning", "Warning"), 
            ("information", "Information")], 
        help="Indicates whether the issue indicates a variation from successful processing.")                
    code_id = fields.Many2one(
        comodel_name="hc.vs.issue.type", 
        string="Code", 
        required="True", help="Error or warning code.")                
    details_id = fields.Many2one(
        comodel_name="hc.vs.operation.outcome", 
        string="Details", 
        help="Additional details about the error.")                
    diagnostics = fields.Text(
        string="Diagnostics", 
        help="Additional diagnostic information about the issue.")                
    location_ids = fields.One2many(
        comodel_name="hc.operation.outcome.issue.location", 
        inverse_name="issue_id", 
        string="Locations", 
        help="XPath of element(s) related to issue.")                
    expression_ids = fields.One2many(
        comodel_name="hc.operation.outcome.issue.expression", 
        inverse_name="issue_id", string="Expressions", 
        help="FluentPath of element(s) related to issue.")                

class OperationOutcomeIssueLocation(models.Model):    
    _name = "hc.operation.outcome.issue.location"    
    _description = "Operation Outcome Issue Location"        
    _inherit = ["hc.basic.association"]

    issue_id = fields.Many2one(
        comodel_name="hc.operation.outcome.issue", 
        string="Issue", 
        help="Issue associated with this Operation Outcome Issue Location.")                
    location = fields.Char(
        string="Location", 
        help="Location associated with this Operation Outcome Issue Location.")                

class OperationOutcomeIssueExpression(models.Model):    
    _name = "hc.operation.outcome.issue.expression"    
    _description = "Operation Outcome Issue Expression"        
    _inherit = ["hc.basic.association"]

    issue_id = fields.Many2one(
        comodel_name="hc.operation.outcome.issue", 
        string="Issue", 
        help="Issue associated with this Operation Outcome Issue Expression.")                
    expression = fields.Char(
        string="Expression", 
        help="Expression associated with this Operation Outcome Issue Expression.")                

class IssueType(models.Model):    
    _name = "hc.vs.issue.type"    
    _description = "Issue Type"        
    _inherit = ["hc.value.set.contains"]

class OperationOutcome(models.Model):    
    _name = "hc.vs.operation.outcome"    
    _description = "Operation Outcome"        
    _inherit = ["hc.value.set.contains"]
