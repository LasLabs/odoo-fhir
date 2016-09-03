# -*- coding: utf-8 -*-

from openerp import models, fields, api

class HealthcareService(models.Model):  
    _name = "hc.res.healthcare.service" 
    _description = "Healthcare Service"

    identifier_ids = fields.One2many(
        comodel_name="hc.healthcare.service.identifier", 
        inverse_name="healthcare_service_id", 
        string="Identifiers", 
        help="External Identifiers for this item.")       
    provided_by_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Provided By", 
        help="The organization that provides this Healthcare Service.")      
    category_id = fields.Many2one(
        comodel_name="hc.vs.service.category", 
        string="Category", 
        help="Identifies the broad category of service being performed or delivered. Selecting a Service Category then determines the list of relevant service types that can be selected in the Primary Service Type.")        
    type_ids = fields.One2many(
        comodel_name="hc.healthcare.service.type", 
        inverse_name="healthcare_service_id", 
        string="Type", 
        help="Type of service that may be delivered or performed.")      
    specialty_ids = fields.One2many(
        comodel_name="hc.healthcare.service.specialty", 
        inverse_name="healthcare_service_id", 
        string="Specialties", 
        help="Collection of Specialties handled by the Service Site. This is more of a Medical Term.")      
    location_ids = fields.One2many(
        comodel_name="hc.healthcare.service.location", 
        inverse_name="healthcare_service_id", 
        string="Location", 
        help="Location(s) where service may be provided.")        
    service_name = fields.Char(
        string="Service Name", 
        help="Further description of the service as it would be presented to a consumer while searching.")        
    comment = fields.Text(
        string="Comment", 
        help="Any additional description of the service and/or any specific issues not covered by the other attributes, which can be displayed as further detail under the serviceName.")       
    extra_details = fields.Text(
        string="Extra Details", 
        help="Extra details about the service that can't be placed in the other fields.")       
    photo_ids = fields.One2many(
        comodel_name="hc.healthcare.service.photo", 
        inverse_name="healthcare_service_id", 
        string="Photo", 
        help="If there is a photo/symbol associated with this HealthcareService, it may be included here to facilitate quick identification of the service in a list.")       
    telecom_ids = fields.One2many(
        comodel_name="hc.healthcare.service.telecom", 
        inverse_name="healthcare_service_id", 
        string="Telecoms", 
        help="List of contacts related to this specific healthcare service. If this is empty, then refer to the location's contacts.")     
    coverage_area_ids = fields.One2many(
        comodel_name="hc.healthcare.service.coverage.area", 
        inverse_name="healthcare_service_id", 
        string="Coverage Areas", 
        help="The location(s) that this service is available to (not where the service is provided).")       
    service_provision_code_ids = fields.One2many(
        comodel_name="hc.healthcare.service.provision.code", 
        inverse_name="healthcare_service_id", 
        string="Service Provision Codes", 
        help="The code(s) that detail the conditions under which the healthcare service is available/offered.")       
    eligibility_id = fields.Many2one(
        comodel_name="hc.vs.service.eligibility", 
        string="Eligibility", 
        help="Does this service have specific eligibility requirements that need to be met in order to use the service.")      
    eligibility_note = fields.Text(
        string="Eligibility Note", 
        help="Describes the eligibility conditions for the service.")     
    program_name_ids = fields.One2many(
        comodel_name="hc.healthcare.service.program.name", 
        inverse_name="healthcare_service_id", 
        string="Program Names", 
        help="Program Names that can be used to categorize the service.")       
    characteristic_ids = fields.One2many(
        comodel_name="hc.healthcare.service.characteristic", 
        inverse_name="healthcare_service_id", 
        string="Characteristics", 
        help="Collection of Characteristics (attributes).")       
    referral_method_ids = fields.One2many(
        comodel_name="hc.healthcare.service.referral.method", 
        inverse_name="healthcare_service_id", 
        string="Referral Methods", 
        help="Ways that the service accepts referrals.")       
    public_key = fields.Char(
        string="Public Key", 
        help="The public part of the 'keys' allocated to an Organization by an accredited body to support secure exchange of data over the internet. To be provided by the Organization, where available.")       
    is_appointment_required = fields.Boolean(
        string="Appointment Required", 
        help="Indicates if an appointment is required for access to this service.")     
    availability_exceptions = fields.Text(
        string="Availability Exceptions", 
        help="A description of Site availability exceptions, e.g., public holiday availability. Succinctly describing all possible exceptions to normal Site availability as details in the Available Times and Not Available Times.")      

class ServiceType(models.Model):    
    _name = "hc.vs.service.type"    
    _description = "Service Type"       
    _inherit = ["hc.value.set.contains"]    

class C80PracticeCodes(models.Model):   
    _name = "hc.vs.c80.practice.codes"  
    _description = "C80 Practice Codes"     
    _inherit = ["hc.value.set.contains"]    

class ServiceProvisionConditions(models.Model): 
    _name = "hc.vs.service.provision.conditions"    
    _description = "Service Provision Conditions"       
    _inherit = ["hc.value.set.contains"]    

class ServiceCategory(models.Model):    
    _name = "hc.vs.service.category"    
    _description = "Service Category"       
    _inherit = ["hc.value.set.contains"]    

class ServiceEligibility(models.Model): 
    _name = "hc.vs.service.eligibility" 
    _description = "Service Eligibility"        
    _inherit = ["hc.value.set.contains"]    

class ServiceReferralMethod(models.Model):  
    _name = "hc.vs.service.referral.method" 
    _description = "Service Referral Method"        
    _inherit = ["hc.value.set.contains"]    

class ServiceCharacteristic(models.Model):  
    _name = "hc.vs.service.characteristic"  
    _description = "Service Characteristic"     
    _inherit = ["hc.value.set.contains"]    

class HealthcareServiceAvailableTime(models.Model): 
    _name = "hc.healthcare.service.available.time"  
    _description = "Healthcare Service Available Time"      
    _inherit = ["hc.available.time"]    

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service available during this period of time.")                 

class HealthcareServiceNotAvailableTime(models.Model):  
    _name = "hc.healthcare.service.not.available.time"  
    _description = "Healthcare Service Not Available Time"      
    _inherit = ["hc.not.available.time"]

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service not available during this period of time.")                 

class HealthcareServiceIdentifier(models.Model):    
    _name = "hc.healthcare.service.identifier"  
    _description = "Healthcare Service Identifier"      
    _inherit = ["hc.basic.association", "hc.identifier"]

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this identifier.")                 

class HealthcareServiceType(models.Model):  
    _name = "hc.healthcare.service.type"    
    _description = "Healthcare Service Type"        
    _inherit = ["hc.basic.association"]

    service_type_id = fields.Many2one(
        comodel_name="hc.vs.service.type", 
        string="Service Type", 
        help="Service type which is associated with this healthcare service.")                  
    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this service type.")                   

class HealthcareServiceSpecialty(models.Model): 
    _name = "hc.healthcare.service.specialty"   
    _description = "Healthcare Service Specialty"       
    _inherit = ["hc.basic.association"] 
    
    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this specialty.")                  
    specialty_id = fields.Many2one(
        comodel_name="hc.vs.c80.practice.codes", 
        string="Specialty", 
        help="Specialty which is associated with this healthcare service.")                 

class HealthcareServicePhoto(models.Model): 
    _name = "hc.healthcare.service.photo"   
    _description = "Healthcare Service Photo"       
    _inherit = ["hc.basic.association", "hc.attachment"]    

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this photo.")                  

class HealthcareServiceTelecom(models.Model):   
    _name = "hc.healthcare.service.telecom" 
    _description = "Healthcare Service Telecom"     
    _inherit = ["hc.telecom.contact.point"] 
    _inherits = {"hc.telecom": "telecom_id"}

    telecom_id = fields.Many2one(
        comodel_name="hc.telecom", 
        string="Telecom",
        required="True", 
        ondelete="restrict", 
        help="Telecom contact point associated with this healthcare service.")                    
    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this telecom contact point.")                  

class HealthcareServiceProgramName(models.Model):  
    _name = "hc.healthcare.service.program.name"    
    _description = "Healthcare Service Program Name"            

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this name.")                   
    name = fields.Char(
        string="Program Name", 
        help="Name of this healthcare service program.")                 

class HealthcareServiceCharacteristic(models.Model):    
    _name = "hc.healthcare.service.characteristic"  
    _description = "Healthcare Service Characteristic"      
    _inherit = ["hc.basic.association"]

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this service characteristic.")                 
    service_characteristic_id = fields.Many2one(
        comodel_name="hc.vs.service.characteristic", 
        string="Service Characteristic", 
        help="Service characteristic which is associated with this healthcare service.")

class HealthcareServiceLocation(models.Model):  
    _name = "hc.healthcare.service.location"    
    _description = "Healthcare Service Location"        
    _inherit = ["hc.basic.association"] 
    _inherits = {"hc.res.location": "location_id"}

    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location",
        required="True", 
        ondelete="restrict", 
        help="Location which is associated with this location.")                    
    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this location.")                   

class HealthcareServiceProvisionCode(models.Model):
    _name = "hc.healthcare.service.provision.code"  
    _description = "Healthcare Service Provision Code"      
    _inherit = ["hc.basic.association"] 
    
    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this service provision condition.")                 
    service_provision_condition_id = fields.Many2one(
        comodel_name="hc.vs.service.provision.conditions", 
        string="Service Provision Condition", 
        help="Service provision condition which is associated with this healthcare service.")             

class HealthcareServiceCoverageArea(models.Model):   
    _name = "hc.healthcare.service.coverage.area"    
    _description = "Healthcare Service Coverage Area"        
    _inherit = ["hc.basic.association"] 
    _inherits = {"hc.res.location": "location_id"}

    location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Location",
        required="True", 
        ondelete="restrict", 
        help="Coverage area which is associated with this healthcare service.") 
    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this coverage area.")                   

class HealthcareServiceReferralMethod(models.Model):    
    _name = "hc.healthcare.service.referral.method" 
    _description = "Healthcare Service Referral Method"     
    _inherit = ["hc.basic.association"]

    healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Healthcare Service", 
        help="Healthcare service which is associated with this service referral method.")                     
    service_referral_method_id = fields.Many2one(
        comodel_name="hc.vs.service.referral.method", 
        string="Service Referral Method", 
        help="Service referral method which is associated with this healthcare service.")                  
