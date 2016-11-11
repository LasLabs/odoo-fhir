# -*- coding: utf-8 -*-

from openerp import models, fields, api

class ValueSetContains(models.AbstractModel):

    _name = "hc.value.set.contains"
    _description = "Value Set Contains"
    _inherit = ["hc.codeable.concept.coding"]
    _order = "code"

    system = fields.Char(
        string="Source URL",
        help="Web address of the source of the code.")
    is_abstract = fields.Boolean(
        string="Abstract", 
        help="If user cannot select this entry.")
    version = fields.Char(
        string="Version", 
        help="Version in which this code / display is defined.")
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

class ActReason(models.Model):    
    _name = "hc.vs.act.reason"    
    _description = "Act Reason"        
    _inherit = ["hc.value.set.contains"]

# class AdditionalInstructionsCode(models.Model):    
#     _name = "hc.vs.additional.instructions.code"    
#     _description = "Additional Instructions Code"        
#     _inherit = ["hc.value.set.contains"]    

class AdministrativeGender(models.Model):   
    _name = "hc.vs.administrative.gender"   
    _description = "Administrative Gender"      
    _inherit = ["hc.value.set.contains"]

class AdministrativeMethodCode(models.Model):    
    _name = "hc.vs.administration.method.code"    
    _description = "Administration Method Code"        
    _inherit = ["hc.value.set.contains"]
    
class AnimalBreed(models.Model):    
    _name = "hc.vs.animal.breed"    
    _description = "Animal Breed"   
    _inherit = ["hc.value.set.contains"]

class AnimalGenderStatus(models.Model): 
    _name = "hc.vs.animal.gender.status"    
    _description = "Animal Gender Status"   
    _inherit = ["hc.value.set.contains"]

class AnimalSpecies(models.Model):  
    _name = "hc.vs.animal.species"  
    _description = "Animal Species" 
    _inherit = ["hc.value.set.contains"]

class ApproachSiteCode(models.Model):    
    _name = "hc.vs.approach.site.code"    
    _description = "Approach Site Code"        
    _inherit = ["hc.value.set.contains"]

class BodySite(models.Model):   
    _name = "hc.vs.body.site"   
    _description = "Body Site"      
    _inherit = ["hc.value.set.contains"]

class C80DocClassCode(models.Model):    
    _name = "hc.vs.c80.doc.class.code"    
    _description = "C80 Doc Class Code"        
    _inherit = ["hc.value.set.contains"]

class C80DocTypeCode(models.Model):    
    _name = "hc.vs.c80.doc.type.code"    
    _description = "C80 Doc Type Code"        
    _inherit = ["hc.value.set.contains"]

class C80FacilityCode(models.Model):    
    _name = "hc.vs.c80.facility.code"    
    _description = "C80 Facility Code"        
    _inherit = ["hc.value.set.contains"]

class C80PracticeCode(models.Model):   
    _name = "hc.vs.c80.practice.code"  
    _description = "C80 Practice Code"     
    _inherit = ["hc.value.set.contains"]  

class ClinicalConcept(models.Model):    
    _name = "hc.vs.clinical.concept"    
    _description = "Clinical Concept"       
    _inherit = ["hc.value.set.contains"]

class ConditionCode(models.Model):
    _name = "hc.vs.condition.code"
    _description = "Condition"
    _inherit = ["hc.value.set.contains"]

class ConditionOutcome(models.Model):
    _name = "hc.vs.condition.outcome"
    _description = "Condition Outcome"
    _inherit = ["hc.value.set.contains"]        

class DaysOfWeek(models.Model):  
    _name = "hc.vs.days.of.week"  
    _description = "Days Of Week"     
    _inherit = ["hc.value.set.contains"]

class DemographicAgeGroup(models.Model):    
    _name = "hc.vs.demographic.age.group"   
    _description = "Demographic Age Group"      
    _inherit = ["hc.value.set.contains"]

class EncounterParticipantType(models.Model):   
    _name = "hc.vs.encounter.participant.type"  
    _description = "Encounter Participant Type"     
    _inherit = ["hc.value.set.contains"]

class EncounterReason(models.Model):    
    _name = "hc.vs.encounter.reason"    
    _description = "Encounter Reason"       
    _inherit = ["hc.value.set.contains"]

class Ethnicity(models.Model):  
    _name = "hc.vs.ethnicity"  
    _description = "Ethnicity" 
    _inherit = ["hc.value.set.contains"]

class FormatCode(models.Model): 
    _name = "hc.vs.format.code" 
    _description = "Format Code"        
    _inherit = ["hc.value.set.contains"]

class Jurisdiction(models.Model):   
    _name = "hc.vs.jurisdiction"    
    _description = "Jurisdiction"       
    _inherit = ["hc.value.set.contains"]

class ManifestationCode(models.Model): 
    _name = "hc.vs.manifestation.code" 
    _description = "Manifestation Code"        
    _inherit = ["hc.value.set.contains"]  

class MaritalStatus(models.Model):  
    _name = "hc.vs.marital.status"  
    _description = "Marital Status" 
    _inherit = ["hc.value.set.contains"]

class MedicationAsNeededReason(models.Model):    
    _name = "hc.vs.medication.as.needed.reason"    
    _description = "Medication As Needed Reason"        
    _inherit = ["hc.value.set.contains"]

class OccupationCode(models.Model):  
    _name = "hc.vs.occupation.code"  
    _description = "Occupation Code" 
    _inherit = ["hc.value.set.contains"]

class ParticipantRole(models.Model):    
    _name = "hc.vs.participant.role"    
    _description = "Participant Role"      
    _inherit = ["hc.value.set.contains"]

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

class Race(models.Model):  
    _name = "hc.vs.race"  
    _description = "Race" 
    _inherit = ["hc.value.set.contains"]  

class RequestPriority(models.Model):    
    _name = "hc.vs.request.priority"    
    _description = "Request Priority"        
    _inherit = ["hc.value.set.contains"]

class ResourceType(models.Model):   
    _name = "hc.vs.resource.type"   
    _description = "Resource Type"      
    _inherit = ["hc.value.set.contains"]   

class RouteCode(models.Model): 
    _name = "hc.vs.route.code" 
    _description = "Route Code"        
    _inherit = ["hc.value.set.contains"]  

class SecurityLabel(models.Model):  
    _name = "hc.vs.security.label"  
    _description = "Security Label"     
    _inherit = ["hc.value.set.contains"]

class SubstanceCode(models.Model):  
    _name = "hc.vs.substance.code"  
    _description = "Substance Code"     
    _inherit = ["hc.value.set.contains"]    

class UOM(models.Model):
    _name = "hc.vs.uom"
    _description = "Unit of Measure"
    _inherit = ["hc.value.set.contains"]

class UserType(models.Model):   
    _name = "hc.vs.user.type"   
    _description = "User Type"      
    _inherit = ["hc.value.set.contains"]

class WorkflowSetting(models.Model):    
    _name = "hc.vs.workflow.setting"    
    _description = "Workflow Setting"       
    _inherit = ["hc.value.set.contains"]

class WorkflowTask(models.Model):   
    _name = "hc.vs.workflow.task"   
    _description = "Workflow Task"      
    _inherit = ["hc.value.set.contains"]

