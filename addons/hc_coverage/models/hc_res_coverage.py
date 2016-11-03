# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Coverage(models.Model):
    _name = "hc.res.coverage"
    _description = "Coverage"

    status = fields.Selection(
        string="Status", required="True", 
        selection=[
            ("active", "Active"), 
            ("cancelled", "Cancelled"), 
            ("draft", "Draft"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="The status of the resource instance.")
    issuer_type = fields.Selection(
        string="Issuer Type", 
        required="True", 
        selection=[
            ("identifier", "Identifier"), 
            ("organization", "Organization"), 
            ("patient", "Patient"), 
            ("related person", "Related Person")], 
        help="Type of plan or agreement issuer.")
    issuer_name = fields.Char(
        string="Issuer",
        required="True", 
        compute="compute_issuer_name", 
        help="Identifier for the plan or agreement issuer.")
    issuer_identifier_id = fields.Many2one(
        comodel_name="hc.issuer.identifier", 
        string="Issuer Identifier", 
        help="Identifier for the plan or agreement issuer.")
    issuer_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Issuer Organization", 
        help="Organization identifier for the plan or agreement issuer.")
    issuer_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Issuer Patient", 
        help="Patient identifier for the plan or agreement issuer.")
    issuer_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Issuer Related Person", 
        help="RelatedPerson identifier for the plan or agreement issuer.")
    is_agreement = fields.Boolean(
        comodel_name="hc.coverage.is.agreement", 
        string="Agreement", 
        help="Is a Payment Agreement.")
    bin = fields.Char(string="Group", help="BIN Number.")
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the coverage.")
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the coverage.")

    type_id = fields.Many2one(
        comodel_name="hc.vs.act.coverage.type.code", 
        string="Type", 
        help="Type of coverage.")
    planholder_type = fields.Selection(
        string="Planholder Type", 
        required="True", 
        selection=[
            ("identifier", "Identifier"), 
            ("patient", "Patient"), 
            ("organization", "Organization")], 
        help="Type of plan holder.")
    planholder_name = fields.Char(
        string="Planholder", 
        compute="compute_planholder_name", 
        required="True", 
        help="Plan holder.")
    planholder_identifier_id = fields.Many2one(
        comodel_name="hc.planholder.identifier", 
        string="Planholder Identifier", 
        help="Identifier plan holder.")
    planholder_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Planholder Patient", 
        help="Patient plan holder.")
    planholder_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Planholder Organization", 
        help="Organization plan holder.")
    beneficiary_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Beneficiary", 
        help="Patient plan holder.")
    relationship_id = fields.Many2one(
        comodel_name="hc.vs.policyholder.relationship", 
        string="Relationship", 
        required="True", 
        help="Beneficiary relationship to Planholder.")
    identifier_ids = fields.One2many(
        comodel_name="hc.coverage.identifier", 
        inverse_name="coverage_id", 
        string="Primary Coverage Identifiers", 
        help="The primary coverage ID.")
    group = fields.Char(
        string="Group", 
        help="An identifier for the group.")
    plan = fields.Char(
        string="Plan", 
        help="An identifier for the plan.")
    sub_plan = fields.Char(
        string="Sub Plan", 
        help="An identifier for the subsection of the plan.")
    dependent = fields.Integer(
        string="Dependent", 
        help="The dependent number.")
    sequence = fields.Integer(
        string="Sequence", 
        help="The plan instance or sequence counter.")
    network_ids = fields.One2many(
        comodel_name="hc.coverage.network", 
        inverse_name="coverage_id", 
        string="Networks", 
        help="Insurer network.")
    contract_ids = fields.One2many(
        comodel_name="hc.coverage.contract", 
        inverse_name="coverage_id", 
        string="Contracts", 
        help="Contract details.")

class CoverageIdentifier(models.Model):
    _name = "hc.coverage.identifier"
    _description = "Coverage Identifier"
    _inherit = ["hc.basic.association", "hc.identifier"]

    coverage_id = fields.Many2one(
        comodel_name="hc.res.coverage", 
        string="Coverage", 
        help="Coverage associated with this coverage identifier.")

class CoverageContract(models.Model):
    _name = "hc.coverage.contract"
    _description = "Coverage Contract"
    _inherit = ["hc.basic.association"]

    # contract_id = fields.Many2one(
    #     comodel_name="hc.res.contract", 
    #     string="Contract", 
    #     help="Contract associated with this coverage contract.")
    coverage_id = fields.Many2one(
        comodel_name="hc.res.coverage", 
        string="Coverage", 
        help="Coverage associated with this coverage contract.")

class CoverageNetwork(models.Model):    
    _name = "hc.coverage.network"   
    _description = "Coverage Network"       
    _inherit = ["hc.basic.association"]

    organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Organization", 
        help="Organization associated with this coverage network.")             
    coverage_id = fields.Many2one(
        comodel_name="hc.res.coverage", 
        string="Coverage", 
        # required="True", 
        help="Coverage associated with this coverage network.")

class IssuerIdentifier(models.Model):
    _name = "hc.issuer.identifier"
    _description = "Issuer Identifier"
    _inherit = ["hc.basic.association", "hc.identifier"]

class PlanholderIdentifier(models.Model):
    _name = "hc.planholder.identifier"
    _description = "Planholder Identifier"
    _inherit = ["hc.basic.association", "hc.identifier"]

class BeneficiaryIdentifier(models.Model):
    _name = "hc.beneficiary.identifier"
    _description = "Beneficiary Identifier"
    _inherit = ["hc.basic.association", "hc.identifier"]

class ActCoverageTypeCode(models.Model):
    _name = "hc.vs.act.coverage.type.code"
    _description = "Act Coverage Type Code"
    _inherit = ["hc.value.set.contains"]

class PolicyholderRelationship(models.Model):
    _name = "hc.vs.policyholder.relationship"
    _description = "Policyholder Relationship"
    _inherit = ["hc.value.set.contains"]

