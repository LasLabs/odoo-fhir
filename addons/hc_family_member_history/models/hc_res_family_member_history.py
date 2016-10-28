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
        help="Person who is this family member.")
    identifier_ids = fields.One2many(
        comodel_name="hc.family.member.identifier", 
        inverse_name="family_member_id", 
        string="Identifiers", 
        help="External Id(s) for this record.")                 
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
    family_history_status = fields.Selection(
        string="Family History Status", 
        required="True", 
        selection=[
            ("partial", "Partial"), 
            ("completed", "Completed"), 
            ("entered-in-error", "Entered-In-Error"), 
            ("health-unknown", "Health-Unknown")], 
        help="A code specifying a state of a Family Member History record.")                  
    name = fields.Char(
        string="Name", 
        help="The family member described.")                  
    relationship_id = fields.Many2one(
        comodel_name="hc.vs.v3.family.member", 
        string="Relationship", 
        required="True", 
        help="Relationship to the subject.")                    
    gender = fields.Selection(
        string="Family Member History Gender", 
        selection=[
            ("male", "Male"), 
            ("female", "Female"), 
            ("other", "Other"), 
            ("unknown", "Unknown")], 
        help="The gender that the relative is considered to have for administration and record keeping purposes.")                 
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
        help="approximate age.")                   
    age_uom_id = fields.Many2one(
        comodel_name="hc.vs.uom", 
        string="Age UOM", 
        default="year", 
        help="Age unit of measure. Default = year.")                  
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
        comodel_name="hc.vs.uom", 
        string="Deceased Age UOM", 
        default="year", 
        help="Age unit of measure. Default = year.")                    
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
    note_id = fields.Many2one(
        comodel_name="hc.family.member.history.note", 
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
    onset_string = fields.Char(
        string="Onset", 
        help="String of when condition first manifested.")                    
    note_id = fields.Many2one(
        comodel_name="hc.family.member.history.condition.note", 
        string="Note", 
        help="Extra information about condition.")                    

class FamilyMemberIdentifier(models.Model): 
    _name = "hc.family.member.identifier"   
    _description = "Family Member Identifier"           
    _inherits = {"hc.person.identifier": "person_identifier_id"}
    
    person_identifier_id = fields.Many2one(
        comodel_name="hc.person.identifier",
        string="Person Identifier",
        required="True",
        ondelete="restrict", 
        help="Person identifier associated with this family member.")   

    family_member_id = fields.Many2one(
        comodel_name="hc.res.family.member.history", 
        string="Family Member", 
        help="Relation with this condition.")                   
                 
class FamilyMemberHistoryNote(models.Model):  
    _name = "hc.family.member.history.note"  
    _description = "Family Member History Note"     
    _inherit = ["hc.basic.association", "hc.annotation"]
                 
    # family_member_id = fields.Many2one(
    #     comodel_name="hc.res.family.member.history", 
    #     string="Family Member", 
    #     help="Family member associated with this note.")                   

class FamilyMemberHistoryConditionNote(models.Model):   
    _name = "hc.family.member.history.condition.note"   
    _description = "Family Member History Condition Note"       
    _inherit = ["hc.basic.association", "hc.annotation"]

    # family_member_condition_id = fields.Many2one(
    #     comodel_name="hc.family.member.history.condition", 
    #     string="Family Member Condition", 
    #     help="Family member condition associated with this note.")

class V3FamilyMember(models.Model): 
    _name = "hc.vs.v3.family.member"    
    _description = "V3 Family Member"       
    _inherit = ["hc.value.set.contains"]

# External Reference

class Patient(models.Model):
    _inherit = ["hc.res.patient"]

    family_member_ids = fields.One2many(
        comodel_name="hc.res.family.member.history",
        inverse_name="patient_id", 
        string="Family Members", 
        help="Relation with this patient.")
