# -*- coding: utf-8 -*-

from openerp import models, fields, api

class FamilyMemberHistory(models.Model):
    _name = "hc.res.family.member.history"
    _description = "Family Member History"
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person",
        string="Person",
        required=True,
        ondelete="restrict",
        help="Person who is this related person.")
    # identifier_ids = fields.One2many(
    #     comodel_name="hc.family.member.identifier", 
    #     inverse_name="family_member_id", 
    #     string="Identifiers", 
    #     help="External Id(s) for this record.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        required=True, 
        help="Patient history is about.")
    family_history_date = fields.Datetime(
        string="Date", 
        help="When history was captured/updated.")
    family_history_status = fields.Selection(
        string="Family History Status", 
        selection=[
            ("partial", "Partial"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("health-unknown", "Health-Unknown")], 
        help="A code specifying a state of a Family Member History record.")
    # name = fields.Char(
    #     string="Name", 
    #     help="The family member described.")
    # relationship_id = fields.Many2one(
    #     comodel_name="hc.vs.related.person.relationship", 
    #     string="Relationship", 
    #     help="Relationship to the subject.")
    # gender = fields.Selection(
    #     string="Family Member History Gender", 
    #     selection=[
    #         ("male", "Male"), 
    #         ("female", "Female"), 
    #         ("other", "Other"), 
    #         ("unknown", "Unknown")], 
    #     help="The gender that the relative is considered to have for administration and record keeping purposes.")
    earliest_birth_date = fields.Datetime(
        string="Earliest Birth Date", 
        help="From (approximate) date of birth.")
    latest_birth_date = fields.Datetime(
        string="Latest Birth Date", 
        help="To (approximate) date of birth.")
    born_date = fields.Date(
        string="Born Date", 
        help="(approximate) date of birth.")
    born_note = fields.Text(
        string="Born Note", 
        help="General note about (approximate) date of birth.")
    is_age_known = fields.Boolean(
        string="Age Known", 
        help="Age known?")
    age = fields.Integer(
        string="Age", 
        size=3, 
        help="(approximate) age.")
    age_uom_id = fields.Many2one(
        comodel_name="hc.vs.uom", 
        string="Age UOM", 
        default="year", 
        help="Age unit of measure. Default = year.")
    age_range_low = fields.Float(
        string="Age Range Low", 
        help="Low limit of (approximate) age.")
    age_range_high = fields.Float(
        string="Age Range High", 
        help="High limit of (approximate) age.")
    age_note = fields.Text(
        string="Age Note", 
        help="General note about (approximate) age.")
    is_deceased = fields.Boolean(
        string="Deceased", 
        help="Dead?")
    is_deceased_age_known = fields.Boolean(
        string="Deceased Age Known", 
        help="Deceased age known?")
    deceased_age = fields.Integer(
        string="Deceased Age", 
        size=3, 
        help="How old/when?")
    deceased_age_uom_id = fields.Many2one(
        comodel_name="hc.vs.uom", 
        string="Deceased Age UOM", 
        default="year", help="Age unit of measure. Default = year.")
    deceased_age_range_low = fields.Float(
        string="Deceased Age Range Low", 
        help="Low limit age of dead?")
    deceased_age_range_high = fields.Float(
        string="Deceased Age Range High", 
        help="High limit of of dead?")
    deceased_date = fields.Date(
        string="Deceased Date", 
        help="Deceased date.")
    deceased_note = fields.Text(
        string="Deceased Note", 
        help="General note about deceased event.")
    note = fields.Text(
        string="Note", 
        help="General note about related person.")

class FamilyMemberHistoryCondition(models.Model):
    _name = "hc.family.member.history.condition"
    _description = "Family Member History Condition"

    family_member_id = fields.Many2one(
        comodel_name="hc.res.family.member.history", 
        string="Family Member", 
        help="Relation with this condition.")
    code_id = fields.Many2one(
        comodel_name="hc.vs.condition.code", 
        string="Condition Code", 
        help="Condition suffered by relation.")
    outcome_id = fields.Many2one(
        comodel_name="hc.vs.condition.outcome", 
        string="Condition Outcome", 
        help="Indicates what happened as a result of this condition. If the condition resulted in death, deceased date is captured on the relation.")
    onset_age = fields.Integer(
        string="Onset Age", 
        size=3, 
        help="When condition first manifested.")
    onset_age_uom_id = fields.Many2one(
        comodel_name="hc.vs.uom", 
        string="Onset Age UOM", 
        default="year", 
        help="Age unit of measure. Default = year.")
    onset_range_low = fields.Float(
        string="Onset Range Low", 
        help="Low limit of when condition first manifested.")
    onset_range_high = fields.Float(
        string="Onset Range High", 
        help="High limit of when condition first manifested.")
    onset = fields.Char(
        string="Onset", 
        help="When condition first manifested.")
    note = fields.Text(
        string="Note", 
        help="Extra information about condition.")

class FamilyMemberIdentifier(models.Model):
    _name = "hc.family.member.identifier"
    _description = "Family Member Identifier"
    _inherits = {"hc.person.identifier": "person_identifier_id"}

    person_identifier_id = fields.Many2one(
        comodel_name="hc.person.identifier", 
        string="Person Identifier",
        required=True,
        ondelete="restrict", 
        help="Person identifier associated with this relation.")
    family_member_id = fields.Many2one(
        comodel_name="hc.res.family.member.history", 
        string="Family Member", 
        help="Relation with this condition.")

class ConditionOutcome(models.Model):
    _name = "hc.vs.condition.code"
    _description = "Condition"
    _inherit = ["hc.value.set.contains"]

class ConditionOutcome(models.Model):
    _name = "hc.vs.condition.outcome"
    _description = "Condition Outcome"
    _inherit = ["hc.value.set.contains"]

class UOM(models.Model):
    _name = "hc.vs.uom"
    _description = "UOM"
    _inherit = ["hc.value.set.contains"]

# External Reference

class Patient(models.Model):
    _inherit = ["hc.res.patient"]

    family_member_ids = fields.One2many(
        comodel_name="hc.res.family.member.history",
        inverse_name="patient_id", 
        string="Family Members", 
        help="Relation with this patient.")
