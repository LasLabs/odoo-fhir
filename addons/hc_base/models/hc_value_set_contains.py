# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ValueSetContains(models.AbstractModel):

    _name = "hc.value.set.contains"
    _description = "Value Set Contains"
    _inherit = ["hc.codeable.concept.coding"]
    _order = "code"

    # system = fields.Char(
    #     string="Source URL",
    #     help="Web address of the source of the code.")
    is_abstract = fields.Boolean(
        string="Abstract", 
        help="If user cannot select this entry.")
    # version = fields.Char(
    #     string="Version", 
    #     help="Version in which this code / display is defined.")
    # code = fields.Char(
    #     string="Code", 
    #     help="Code - if blank, this is not a choosable code.")
    name = fields.Char(
        string="Name", 
        help="User display for the concept.")
    level = fields.Integer(
        string="Level", 
        help="Level in a hierarchy of codes.")
    source_id = fields.Many2one(
        comodel_name="res.partner", 
        string="Source", 
        help="The source of the definition of the code.")
    definition = fields.Text(
        string="Definition", 
        help="An explanation of the meaning of the concept.")
    comments = fields.Text(
        string="Comments", 
        help="Additional notes about how to use the code.")
    contains_id = fields.Many2one(
        comodel_name="hc.value.set.contains", 
        string="Parent",
        help="Parent concept.")

    _sql_constraints = [
        ('code_unique',
        'UNIQUE(code)',
        "The concept code must be unique.")
        ]

    # @api.one
    # @api.constrains('name', 'description')
    # def _check_description(self):
    #     if self.name == self.description:
    #         raise ValidationError("Concept name and description must be different")

class ActCode(models.Model):   
    _name = "hc.vs.act.code"
    _description = "Act Code"  
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this act.")
    code = fields.Char(
        string="Code", 
        help="Code of this act.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.act.code", 
        string="Parent",
        help="Parent concept.")

class ActionCode(models.Model):    
    _name = "hc.vs.action.code"    
    _description = "Action Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this action.")
    code = fields.Char(
        string="Code", 
        help="Code of this action.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.action.code", 
        string="Parent",
        help="Parent concept.")

class ActReason(models.Model):    
    _name = "hc.vs.act.reason"    
    _description = "Act Reason"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this act reason.")
    code = fields.Char(
        string="Code", 
        help="Code of this act reason.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.act.reason", 
        string="Parent",
        help="Parent concept.")

# class AdditionalInstructionsCode(models.Model):    
#     _name = "hc.vs.additional.instructions.code"    
#     _description = "Additional Instructions Code"        
#     _inherit = ["hc.value.set.contains"]    

class AdministrativeGender(models.Model):   
    _name = "hc.vs.administrative.gender"   
    _description = "Administrative Gender"      
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this administrative gender.")
    code = fields.Char(
        string="Code", 
        help="Code of this administrative gender.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.administrative.gender", 
        string="Parent",
        help="Parent concept.")

class AdministrationMethodCode(models.Model):    
    _name = "hc.vs.administration.method.code"    
    _description = "Administration Method Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this administration method.")
    code = fields.Char(
        string="Code", 
        help="Code of this administration method.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.administration.method.code", 
        string="Parent",
        help="Parent concept.")

class ApproachSiteCode(models.Model):    
    _name = "hc.vs.approach.site.code"    
    _description = "Approach Site Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this approach site.")
    code = fields.Char(
        string="Code", 
        help="Code of this approach site.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.approach.site.code", 
        string="Parent",
        help="Parent concept.")

class BodySite(models.Model):   
    _name = "hc.vs.body.site"   
    _description = "Body Site"      
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this body site.")
    code = fields.Char(
        string="Code", 
        help="Code of this body site.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.body.site", 
        string="Parent",
        help="Parent concept.")

class C80DocClassCode(models.Model):    
    _name = "hc.vs.c80.doc.class.code"    
    _description = "C80 Doc Class Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this C80 Doc Class.")
    code = fields.Char(
        string="Code", 
        help="Code of this C80 Doc Class.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.c80.doc.class.code", 
        string="Parent",
        help="Parent concept.")

class C80DocTypeCode(models.Model):    
    _name = "hc.vs.c80.doc.type.code"    
    _description = "C80 Doc Type Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this C80 Doc Type.")
    code = fields.Char(
        string="Code", 
        help="Code of this C80 Doc Type.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.c80.doc.type.code", 
        string="Parent",
        help="Parent concept.")

class C80FacilityCode(models.Model):    
    _name = "hc.vs.c80.facility.code"    
    _description = "C80 Facility Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this C80 Facility.")
    code = fields.Char(
        string="Code", 
        help="Code of this C80 Facility.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.c80.facility.code", 
        string="Parent",
        help="Parent concept.")

class C80PracticeCode(models.Model):   
    _name = "hc.vs.c80.practice.code"  
    _description = "C80 Practice Code"     
    _inherit = ["hc.value.set.contains"]  

    name = fields.Char(
        string="Name", 
        help="Name of this C80 Practice.")
    code = fields.Char(
        string="Code", 
        help="Code of this C80 Practice.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.c80.practice.code", 
        string="Parent",
        help="Parent concept.")

class ClinicalConcept(models.Model):    
    _name = "hc.vs.clinical.concept"    
    _description = "Clinical Concept"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this clinical concept.")
    code = fields.Char(
        string="Code", 
        help="Code of this clinical concept.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.clinical.concept", 
        string="Parent",
        help="Parent concept.")

class ConditionCode(models.Model):
    _name = "hc.vs.condition.code"
    _description = "Condition"
    _inherit = ["hc.value.set.contains"]
    _rec_name = "code"

    name = fields.Char(
        string="Name", 
        help="Name of this condition.")
    code = fields.Char(
        string="Code", 
        help="Code of this condition.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.condition.code", 
        string="Parent",
        help="Parent concept.")

class ConditionOutcome(models.Model):
    _name = "hc.vs.condition.outcome"
    _description = "Condition Outcome"
    _inherit = ["hc.value.set.contains"]        

    name = fields.Char(
        string="Name", 
        help="Name of this condition outcome.")
    code = fields.Char(
        string="Code", 
        help="Code of this condition outcome.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.condition.outcome", 
        string="Parent",
        help="Parent concept.")

class DaysOfWeek(models.Model):  
    _name = "hc.vs.days.of.week"  
    _description = "Days Of Week"     
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this day of week.")
    code = fields.Char(
        string="Code", 
        help="Code of this day of week.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.days.of.week", 
        string="Parent",
        help="Parent concept.")

class DefinedType(models.Model):    
    _name = "hc.vs.defined.type"    
    _description = "Defined Type"            
    _inherit = ["hc.value.set.contains"]    

    name = fields.Char(
        string="Name", 
        help="Name of this defined type.")
    code = fields.Char(
        string="Code", 
        help="Code of this defined type.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.defined.type", 
        string="Parent",
        help="Parent concept.")

class DemographicAgeGroup(models.Model):    
    _name = "hc.vs.demographic.age.group"   
    _description = "Demographic Age Group"      
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this demographic age group.")
    code = fields.Char(
        string="Code", 
        help="Code of this demographic age group.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.demographic.age.group", 
        string="Parent",
        help="Parent concept.")

class DesignationUse(models.Model):    
    _name = "hc.vs.designation.use"    
    _description = "Designation Use"            
    _inherit = ["hc.value.set.contains"] 

    name = fields.Char(
        string="Name", 
        help="Name of this designation use.")
    code = fields.Char(
        string="Code", 
        help="Code of this designation use.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.designation.use",
        string="Parent",
        help="Parent concept.")

class EncounterParticipantType(models.Model):   
    _name = "hc.vs.encounter.participant.type"  
    _description = "Encounter Participant Type"     
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this encounter participant type.")
    code = fields.Char(
        string="Code", 
        help="Code of this encounter participant type.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.encounter.participant.type",
        string="Parent",
        help="Parent concept.")

class EncounterReason(models.Model):    
    _name = "hc.vs.encounter.reason"    
    _description = "Encounter Reason"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this encounter reason.")
    code = fields.Char(
        string="Code", 
        help="Code of this encounter reason.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.encounter.reason",
        string="Parent",
        help="Parent concept.")

class Ethnicity(models.Model):  
    _name = "hc.vs.ethnicity"  
    _description = "Ethnicity" 
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this ethnicity.")
    code = fields.Char(
        string="Code", 
        help="Code of this ethnicity.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.ethnicity",
        string="Parent",
        help="Parent concept.")

class FormatCode(models.Model): 
    _name = "hc.vs.format.code" 
    _description = "Format Code"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this format.")
    code = fields.Char(
        string="Code", 
        help="Code of this format.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.format.code",
        string="Parent",
        help="Parent concept.")

class FormCode(models.Model):   
    _name = "hc.vs.form.code"   
    _description = "Form Code"      
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this form code.")
    code = fields.Char(
        string="Code", 
        help="Code of this form code.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.form.code",
        string="Parent",
        help="Parent concept.")

class Forms(models.Model):    
    _name = "hc.vs.forms"    
    _description = "Forms"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this form.")
    code = fields.Char(
        string="Code", 
        help="Code of this form.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.forms",
        string="Parent",
        help="Parent concept.")

class Jurisdiction(models.Model):   
    _name = "hc.vs.jurisdiction"    
    _description = "Jurisdiction"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this jurisdiction.")
    code = fields.Char(
        string="Code", 
        help="Code of this jurisdiction.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.jurisdiction",
        string="Parent",
        help="Parent concept.")  

class MaritalStatus(models.Model):  
    _name = "hc.vs.marital.status"  
    _description = "Marital Status" 
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this marital status.")
    code = fields.Char(
        string="Code", 
        help="Code of this marital status.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.marital.status",
        string="Parent",
        help="Parent concept.")

class MedicationAsNeededReason(models.Model):    
    _name = "hc.vs.medication.as.needed.reason"    
    _description = "Medication As Needed Reason"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this medication as needed reason.")
    code = fields.Char(
        string="Code", 
        help="Code of this medication as needed reason.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.medication.as.needed.reason",
        string="Parent",
        help="Parent concept.")

class MessageEvent(models.Model):    
    _name = "hc.vs.message.event"    
    _description = "Message Event"        
    _inherit = ["hc.value.set.contains"] 

    name = fields.Char(
        string="Name", 
        help="Name of this message event.")
    code = fields.Char(
        string="Code", 
        help="Code of this message event.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.message.event",
        string="Parent",
        help="Parent concept.")
    
class OccupationCode(models.Model):  
    _name = "hc.vs.occupation.code"  
    _description = "Occupation Code" 
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this occupation.")
    code = fields.Char(
        string="Code", 
        help="Code of this occupation.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.occupation.code",
        string="Parent",
        help="Parent concept.")

class ParticipantRole(models.Model):    
    _name = "hc.vs.participant.role"    
    _description = "Participant Role"      
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this participant role.")
    code = fields.Char(
        string="Code", 
        help="Code of this participant role.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.participant.role",
        string="Parent",
        help="Parent concept.")

class ParticipationType(models.Model): 
    _name = "hc.vs.participation.type" 
    _description = "Participation Type"
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this participation type (e.g., admitter).")
    code = fields.Char(
        string="Code", 
        help="Code of this participation type (e.g., ADM).")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.participation.type", 
        string="Parent",
        help="Parent concept.")

class PurposeOfUse(models.Model):    
    _name = "hc.vs.purpose.of.use"    
    _description = "Purpose Of Use"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this purpose of use.")
    code = fields.Char(
        string="Code", 
        help="Code of this purpose of use.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.purpose.of.use",
        string="Parent",
        help="Parent concept.")

class Race(models.Model):  
    _name = "hc.vs.race"  
    _description = "Race" 
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this race.")
    code = fields.Char(
        string="Code", 
        help="Code of this race.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.race",
        string="Parent",
        help="Parent concept.")  

class RequestPriority(models.Model):    
    _name = "hc.vs.request.priority"    
    _description = "Request Priority"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this request priority.")
    code = fields.Char(
        string="Code", 
        help="Code of this request priority.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.request.priority",
        string="Parent",
        help="Parent concept.")

class ResourceType(models.Model):   
    _name = "hc.vs.resource.type"   
    _description = "Resource Type"      
    _inherit = ["hc.value.set.contains"]   

    name = fields.Char(
        string="Name", 
        help="Name of this resource type.")
    code = fields.Char(
        string="Code", 
        help="Code of this resource type.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.resource.type",
        string="Parent",
        help="Parent concept.")

class RouteCode(models.Model): 
    _name = "hc.vs.route.code" 
    _description = "Route Code"        
    _inherit = ["hc.value.set.contains"]  

    name = fields.Char(
        string="Name", 
        help="Name of this route.")
    code = fields.Char(
        string="Code", 
        help="Code of this route.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.route.code",
        string="Parent",
        help="Parent concept.")

class Ruleset(models.Model):    
    _name = "hc.vs.ruleset"    
    _description = "Ruleset"        
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this ruleset.")
    code = fields.Char(
        string="Code", 
        help="Code of this ruleset.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.ruleset",
        string="Parent",
        help="Parent concept.")

class SecurityLabel(models.Model):  
    _name = "hc.vs.security.label"  
    _description = "Security Label"     
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this security label.")
    code = fields.Char(
        string="Code", 
        help="Code of this security label.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.security.label",
        string="Parent",
        help="Parent concept.")

class SubstanceCode(models.Model):  
    _name = "hc.vs.substance.code"  
    _description = "Substance Code"     
    _inherit = ["hc.value.set.contains"]    

    name = fields.Char(
        string="Name", 
        help="Name of this substance.")
    code = fields.Char(
        string="Code", 
        help="Code of this substance.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.substance.code",
        string="Parent",
        help="Parent concept.")

class TimeUOM(models.Model): 
    _name = "hc.vs.time.uom" 
    _description = "Time Unit of Measure"            
    _inherit = ["hc.value.set.contains", "product.uom"]

    name = fields.Char(
        string="Name", 
        help="Name of time unit of measure.")
    code = fields.Char(
        string="Code", 
        help="Code of this time unit of measure.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.time.uom",
        string="Parent",
        help="Parent concept.")

class UserType(models.Model):   
    _name = "hc.vs.user.type"   
    _description = "User Type"      
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this user type.")
    code = fields.Char(
        string="Code", 
        help="Code of this user type.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.user.type",
        string="Parent",
        help="Parent concept.")

class WorkflowSetting(models.Model):    
    _name = "hc.vs.workflow.setting"    
    _description = "Workflow Setting"       
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this workflow setting.")
    code = fields.Char(
        string="Code", 
        help="Code of this workflow setting.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.workflow.setting",
        string="Parent",
        help="Parent concept.")

class WorkflowTask(models.Model):   
    _name = "hc.vs.workflow.task"   
    _description = "Workflow Task"      
    _inherit = ["hc.value.set.contains"]

    name = fields.Char(
        string="Name", 
        help="Name of this workflow task.")
    code = fields.Char(
        string="Code", 
        help="Code of this workflow task.")
    contains_id = fields.Many2one(
        comodel_name="hc.vs.workflow.task",
        string="Parent",
        help="Parent concept.")
