# -*- coding: utf-8 -*-

from openerp import models, fields, api

class DetectedIssue(models.Model):
    _name = "hc.res.detected.issue"
    _description = "Detected Issue"

    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Associated patient.")
    category_id = fields.Many2one(
        comodel_name="hc.vs.detected.issue.category", 
        string="Category", 
        help="Issue Category, e.g. drug-drug, duplicate therapy, etc.")
    severity = fields.Selection(
        string="Severity", 
        selection=[
            ("high", "High"), 
            ("moderate", "Moderate"), 
            ("low", "Low")], 
        help="Identifies the general type of issue identified.")
    implicated_ids = fields.One2many(
        comodel_name="hc.detected.issue.implicated", 
        inverse_name="detected_issue_id", 
        string="Implicated", 
        help="Problem resource.")
    detail = fields.Char(
        string="Detail", 
        help="Description and context.")
    date = fields.Datetime(
        string="Date", 
        help="When identified.")
    author_type = fields.Selection(
        string="Author Type", 
        selection=[
            ("practitioner", "Practitioner"), 
            ("device", "Device")], 
        help="Type of provider or device that identified the issue.")
    author_name = fields.Char(
        string="Author", 
        compute="compute_author_name", 
        help="The provider or device that identified the issue.")
    author_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Author Practitioner", 
        help="Practitioner that identified the issue.")
    author_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Author Device", 
        help="Device that identified the issue.")
    identifier_ids = fields.One2many(
        comodel_name="hc.detected.issue.identifier", 
        inverse_name="detected_issue_id", 
        string="Identifier", 
        help="Identifier Unique id for the detected issue.")
    reference = fields.Char(
        string="Reference", 
        help="Authority for issue.")
    mitigation_ids = fields.One2many(
        comodel_name="hc.detected.issue.mitigation", 
        inverse_name="detected_issue_id", 
        string="Mitigation", 
        help="taken to address.")

class DetectedIssueMitigation(models.Model):
    _name = "hc.detected.issue.mitigation"
    _description = "Detected Issue Mitigation"

    detected_issue_id = fields.Many2one(
        comodel_name="hc.res.detected.issue", 
        string="Detected Issue", 
        help="Detected Issue associated with this mitigation.")
    action_id = fields.Many2one(
        comodel_name="hc.vs.detected.issue.mitigation.action", 
        string="Action", 
        required="True", 
        help="What mitigation?")
    date = fields.Datetime(
        string="Date", 
        help="Date committed.")
    author_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Author", 
        help="Who is committing?")

class DetectedIssueImplicated(models.Model):
    _name = "hc.detected.issue.implicated"
    _description = "Detected Issue Implicated"

    detected_issue_id = fields.Many2one(
        comodel_name="hc.res.detected.issue", 
        string="Detected Issue", 
        help="Detected Issue associated with this detected issue implicated.")
    impicated_type = fields.Selection(
        string="Impicated Type", 
        required="True", 
        selection=[
            ("string", "String"), 
            ("codeable concept", "Codeable concept")], 
        help="Type of resource representing the current activity or proposed activity that is potentially problematic.")
    implicated_name = fields.Char(
        string="Implicated", 
        compute="compute_implicated_name", 
        help="Indicates the resource representing the current activity or proposed activity that is potentially problematic.")
    implicated_string = fields.Char(
        string="Implicated String", 
        help="String problem resource.")
    implicated_codeable_concept_id = fields.Many2one(
        comodel_name="hc.vs.detected.issue.implicated", 
        string="Implicated Codeable Concept", 
        help="Codeable Concept problem resource.")

class DetectedIssueIdentifier(models.Model):
    _name = "hc.detected.issue.identifier"
    _description = "Detected Issue Identifier"
    _inherit = ["hc.basic.association", "hc.identifier"]

    detected_issue_id = fields.Many2one(
        comodel_name="hc.res.detected.issue", 
        string="Detected Issue", 
        help="Detected Issue associated with this detected issue identifier.")

class DetectedIssueCategory(models.Model):
    _name = "hc.vs.detected.issue.category"
    _description = "Detected Issue Category"
    _inherit = ["hc.value.set.contains"]

class DetectedIssueMitigationAction(models.Model):
    _name = "hc.vs.detected.issue.mitigation.action"
    _description = "Detected Issue Mitigation Action"
    _inherit = ["hc.value.set.contains"]

class DetectedIssueImplicated(models.Model):
    _name = "hc.vs.detected.issue.implicated"
    _description = "Detected Issue Implicated"
    _inherit = ["hc.value.set.contains"]
