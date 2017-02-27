# -*- coding: utf-8 -*-

from openerp import models, fields, api

class FamilyMemberHistory(models.Model):    
    _name = "hc.res.family.member.history"  
    _description = "Family Member History"          
    _inherits = {"hc.res.person": "person_id"}

    person_id = fields.Many2one(
        comodel_name="hc.res.person",
        string="Person",
        required="True",
        ondelete="restrict",
        help="Person who is this Family Member.")
    identifier_ids = fields.One2many(
        comodel_name="hc.family.member.history.identifier", 
        inverse_name="family_member_history_id", 
        string="Identifiers", 
        help="External Id(s) for this record.")                 
    definition_type = fields.Selection(
        string="Definition Type", 
        selection=[
            ("plan_definition", "Plan Definition"), 
            ("questionnaire", "Questionnaire")], 
        help="Type of instantiates protocol or definition.")
    definition_name = fields.Char(
        string="Definition", 
        compute="_compute_definition_name", 
        store="True", 
        help="Instantiates protocol or definitio.")
    definition_plan_definition_id = fields.Many2one(
        comodel_name="hc.res.plan.definition", 
        string="Definition Plan Definition", 
        help="Istantiates Plan Definition.")
    definition_questionnaire_id = fields.Many2one(
        comodel_name="hc.res.questionnaire", 
        string="Definition Questionnaire", 
        help="Instantiates Questionnaire.")
    status = fields.Selection(
        string="status", 
        required="True", 
        selection=[
            ("partial", "Partial"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("health-unknown", "Health-Unknown")], 
        help="A code specifying the status of the record of the family history of a specific family member.")
    is_not_done = fields.Boolean(
        string="Not Done", 
        help="Family member history did not occur.")
    not_done_reason = fields.Char(
        string="Not Done Reason", 
        selection=[
            ("subject-unknown", "Subject-Unknown"), 
            ("withheld", "Withheld"), 
            ("unable-to-obtain", "Unable-To-Obtain"), 
            ("deferred", "Deferred")], 
        help="Describes why the family member history did not occur in coded and/or textual form.")
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        required="True", 
        help="Patient history is about.")                    
    capture_date = fields.Date(
        string="Capture Date", 
        help="When history was captured.")                    
    update_date = fields.Date(
        string="Update Date", 
        help="When history was updated.")                                        
    name = fields.Char(
        string="Name", 
        help="The family member described.")                  
    relationship_id = fields.Many2one(
        comodel_name="hc.vs.v3.family.member", 
        string="Relationship", 
        required="True", 
        help="Relationship to the subject.")                    
    gender = fields.Selection(
        string="Gender", 
        selection=[
            ("male", "Male"), 
            ("female", "Female"), 
            ("other", "Other"), 
            ("unknown", "Unknown")], 
        help="The gender of a family member used for administrative purposes.")                 
    born_type = fields.Selection(
        string="Born Type",
        selection=[
            ("period", "Period"), 
            ("date", "Date"), 
            ("string", "String")], 
        help="Type of date of birth.")                  
    born_name = fields.Char(
        string="Born", 
        compute="compute_born_name", 
        help="Date of birth.")                 
    earliest_birth_date = fields.Date(
        string="Earliest Birth Date", 
        help="Earliest approximate date of birth.")                   
    latest_birth_date = fields.Date(
        string="Latest Birth Date", 
        help="Latest approximate date of birth.")                 
    born_date = fields.Date(
        string="Born Date", 
        help="Date of birth.")                  
    born_string = fields.Char(
        string="Born", 
        help="String of approximate date of birth.")                 
    is_age_known = fields.Boolean(
        string="Is Age Known", 
        help="Age known?")                 
    age_type = fields.Selection(
        string="Age Type", 
        selection=[
            ("age", "Age"), 
            ("range", "Range"), 
            ("string", "String")], 
        help="Type of age.")                  
    age_name = fields.Char(
        string="Age", 
        compute="compute_age_name", 
        help="Age.")                  
    age = fields.Integer(
        string="Age Integer", 
        size=3, 
        help="Approximate age.")                   
    age_uom_id = fields.Many2one(
        comodel_name="hc.vs.time.uom", 
        string="Time UOM", 
        default="a", 
        help="Time unit of measure.")                  
    age_range_low = fields.Float(
        string="Age Range Low", 
        help="Low limit of approximate age.")                    
    age_range_high = fields.Float(
        string="Age Range High", 
        help="High limit of approximate age.")                 
    age_string = fields.Char(
        string="Age", 
        help="String of approximate age.")                    
    is_deceased = fields.Boolean(
        string="Deceased", 
        help="Dead? How old/when?.")                    
    is_deceased_age_known = fields.Boolean(
        string="Is Deceased Age Known", 
        help="Deceased age known?")  
    deceased_type = fields.Selection(
        string="Deceased Type", 
        selection=[
            ("boolean", "Boolean"), 
            ("Age", "Age"), 
            ("Range", "Range"), 
            ("date", "Date"), 
            ("string", "String")], 
        help="Type of dead? how old/when.")                   
    deceased_name = fields.Char(
        string="Deceased", 
        compute="compute_deceased_name", 
        help="Dead? How old/when.")                                  
    deceased_age = fields.Integer(
        string="Deceased Age", 
        size=3, 
        help="Dead? How old/when?.")
    deceased_age_uom_id = fields.Many2one(
        comodel_name="hc.vs.time.uom", 
        string="Deceased Time UOM", 
        default="a", 
        help="Deceased Time unit of measure.")                  
    deceased_age_range_low = fields.Float(
        string="Deceased Age Range Low", 
        help="Low limit of dead? how old/when?.")                    
    deceased_age_range_high = fields.Float(
        string="Deceased Age Range High", 
        help="High limit of dead? how old/when?.")                 
    deceased_date = fields.Date(
        string="Deceased Date", 
        help="Deceased date.")                 
    deceased_string = fields.Text(
        string="Deceased", 
        help="String of dead? how old/when?")
    note_ids = fields.One2many(
        comodel_name="hc.family.member.history.note", 
        inverse_name="family_member_history_id", 
        string="Notes", 
        help="General note about related person.")
    condition_ids = fields.One2many(
        comodel_name="hc.family.member.history.condition", 
        inverse_name="family_member_history_id", 
        string="Conditions", 
        help="Condition that the related person had.")

class FamilyMemberHistoryCondition(models.Model):   
    _name = "hc.family.member.history.condition"    
    _description = "Family Member History Condition"            

    family_member_history_id = fields.Many2one(
        comodel_name="hc.res.family.member.history", 
        string="Family Member History", 
        help="Family Member History associated with this Condition.")                   
    code_id = fields.Many2one(
        comodel_name="hc.vs.condition.code", 
        string="Code", 
        required="True", 
        help="Condition suffered by relation.")                  
    outcome = fields.Selection(
        string="Condition Outcome", 
        selection=[
            ("deceased", "Deceased"), 
            ("permanent disability", "Permanent Disability"), 
            ("etc.", "Etc.")], 
        help="Indicates what happened as a result of this condition. If the condition resulted in death, deceased date is captured on the relation.")                  
    onset_type = fields.Selection(
        string="Onset Type", 
        selection=[
            ("age", "Age"), 
            ("range", "Range"), 
            ("string", "String")], 
        help="Type of when condition first manifested.")                  
    onset_name = fields.Char(
        string="Onset", 
        compute="compute_onset_name", 
        help="When condition first manifested.")                    
    onset_age = fields.Integer(
        string="Onset Age", 
        size=3, 
        help="When condition first manifested.")                 
    onset_age_uom_id = fields.Many2one(
        comodel_name="hc.vs.time.uom", 
        string="Onset Time UOM", 
        default="a", 
        help="Onset Time unit of measure.")              
    onset_range_low = fields.Float(
        string="Onset Range Low", 
        help="Low limit of when condition first manifested.")                  
    onset_range_high = fields.Float(
        string="Onset Range High", 
        help="High limit of when condition first manifested.")                   
    onset_string = fields.Char(
        string="Onset", 
        help="String of when condition first manifested.")                    
    note_ids = fields.One2many(
        comodel_name="hc.family.member.history.condition.note", 
        inverse_name="condition_id", 
        string="Notes", 
        help="Extra information about condition.")              

class FamilyMemberHistoryIdentifier(models.Model): 
    _name = "hc.family.member.history.identifier"   
    _description = "Family Member History Identifier"           
    _inherits = {"hc.person.identifier": "identifier_id"}
    
    identifier_id = fields.Many2one(
        comodel_name="hc.person.identifier", 
        string="Identifier", 
        ondelete="restrict", 
        required="True", 
        help="Person Identifier associated with this Family Member Identifier.")
    family_member_history_id = fields.Many2one(
        comodel_name="hc.res.family.member.history", 
        string="Family Member History", 
        help="Family Member History associated with this Family Member Identifier.")              
                 
class FamilyMemberHistoryNote(models.Model):  
    _name = "hc.family.member.history.note"  
    _description = "Family Member History Note"     
    _inherit = ["hc.basic.association", "hc.annotation"]

    family_member_history_id = fields.Many2one(
        comodel_name="hc.res.family.member.history", 
        string="Family Member History", 
        help="Family Member History associated with this Family Member History Note.")

class FamilyMemberHistoryConditionNote(models.Model):   
    _name = "hc.family.member.history.condition.note"   
    _description = "Family Member History Condition Note"           
    _inherit = ["hc.basic.association", "hc.annotation"]

    condition_id = fields.Many2one(
        comodel_name="hc.family.member.history.condition", 
        string="Condition", 
        help="Condition associated with this Family Member History Condition Note.")

class V3FamilyMember(models.Model): 
    _name = "hc.vs.v3.family.member"    
    _description = "V3 Family Member"       
    _inherit = ["hc.value.set.contains"]

# External Reference

# class Patient(models.Model):
#     _inherit = ["hc.res.patient"]

#     family_member_history_ids = fields.One2many(
#         comodel_name="hc.res.family.member.history",
#         inverse_name="patient_id", 
#         string="Family Members", 
#         help="Relation with this patient.")
