# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Consent(models.Model):    
    _name = "hc.res.consent"    
    _description = "Consent"        

    identifier_id = fields.Many2one(comodel_name="hc.consent.identifier", string="Identifier", help="Identifier for this record (external references).")                
    status = fields.Selection(string="Status", required="True", selection=[("draft", "Draft"), ("proposed", "Proposed"), ("active", "Active"), ("rejected", "Rejected"), ("inactive", "Inactive"), ("entered-in-error", "Entered-In-Error")], help="Indicates the current state of this consent.")               
    category_ids = fields.One2many(comodel_name="hc.consent.category", inverse_name="consent_id", string="Categories", help="Classification of the consent statement - for indexing/retrieval.")                
    datetime = fields.Datetime(string="Datetime", help="When this Consent was created or indexed.")             
    period_start_date = fields.Datetime(string="Period Start Date", help="Start of the period that this consent applies.")              
    period_end_date = fields.Datetime(string="Period End Date", help="End of the period that this consent applies.")                
    patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Patient", required="True", help="Who the consent applies to .")             
    consentor_ids = fields.One2many(comodel_name="hc.consent.consentor", inverse_name="consent_id", string="Consentors", help="Who is agreeing to the policy and exceptions.")              
    organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Organization", help="Organization that manages the consent.")               
    source_type = fields.Selection(string="Source Type", required="True", selection=[("Consent", "Consent"), ("Document Reference", "Document Reference"), ("Contract", "Contract"), ("Questionnaire Response", "Questionnaire Response")], help="Type of source from which this consent is taken.")                
    value_name = fields.Char(string="Value", compute="_compute_value_name", store="True", help="Source from which this consent is taken.")              
    source_attachment_id = fields.Many2one(comodel_name="hc.consent.source.attachment", string="Source Attachment", help="Attachment source from which this consent is taken.")             
    source_identifier_id = fields.Many2one(comodel_name="hc.consent.source.identifier", string="Source Identifier", help="Identifier source from which this consent is taken.")             
    source_consent_id = fields.Many2one(comodel_name="hc.res.consent", string="Source Consent", help="Consent source from which this consent is taken.")                
    # source_document_reference_id = fields.Many2one(
    #     comodel_name="hc.res.document.reference", 
    #     string="Source Document Reference", 
    #     help="DocumentReference source from which this consent is taken.")             
    # source_contract_id = fields.Many2one(
    #     comodel_name="hc.res.contract", 
    #     string="Source Contract", 
    #     help="Contract source from which this consent is taken.")                
    # source_questionnaire_response_id = fields.Many2one(
    #     comodel_name="hc.res.questionnaire.response", 
    #     string="Source Questionnaire Response", 
    #     help="QuestionnaireResponse source from which this consent is taken.")             
    policy = fields.Char(string="Policy URL", required="True", help="URL of policy that this consents to.")             
    recipient_ids = fields.One2many(comodel_name="hc.consent.recipient", inverse_name="consent_id", string="Recipients", help="Whose access is controlled by the policy.")              
    purpose_ids = fields.One2many(comodel_name="hc.consent.purpose", inverse_name="consent_id", string="Purposes", help="Context of activities for which the agreement is made.")               
    except_ids = fields.One2many(comodel_name="hc.consent.except", inverse_name="consent_id", string="Excepts", help="Additional rule - addition or removal of permissions.")               

class ConsentExcept(models.Model):  
    _name = "hc.consent.except" 
    _description = "Consent Except"     

    consent_id = fields.Many2one(comodel_name="hc.res.consent", string="Consent", help="Consent associated with this Consent Except.")              
    type = fields.Selection(string="Type", required="True", selection=[("deny", "Deny"), ("permit", "Permit")], help="Action to take - permit or deny - when the exception conditions are met.")               
    period_start_date = fields.Datetime(string="Period Start Date", help="Start of the timeframe for data controlled by this exception.")               
    period_end_date = fields.Datetime(string="Period End Date", help="End of the timeframe for data controlled by this exception.")             
    action_ids = fields.One2many(comodel_name="hc.consent.except.action", inverse_name="except_id", string="Actions", help="Actions controlled by this exception.")             
    security_label_ids = fields.One2many(comodel_name="hc.consent.except.security.label", inverse_name="except_id", string="Security Labels", help="Security Labels that define affected resources.")               
    purpose_ids = fields.One2many(comodel_name="hc.consent.except.purpose", inverse_name="except_id", string="Purposes", help="Context of activities covered by this exception.")               
    class_ids = fields.One2many(comodel_name="hc.consent.except.class", inverse_name="except_id", string="Classs", help="e.g. Resource Type, Profile, or CDA etc.")             
    code_ids = fields.One2many(comodel_name="hc.consent.except.code", inverse_name="except_id", string="Codes", help="e.g. LOINC or SNOMED CT code, etc in the content.")               
    actor_ids = fields.One2many(comodel_name="hc.consent.except.actor", inverse_name="except_id", string="Actors", help="Who|what controlled by this exception (or group, by role).")               
    data_ids = fields.One2many(comodel_name="hc.consent.except.data", inverse_name="except_id", string="Datas", help="Data controlled by this exception.")              

class ConsentExceptActor(models.Model):   
    _name = "hc.consent.except.actor"  
    _description = "Consent Except Actor"      

    except_id = fields.Many2one(comodel_name="hc.consent.except", string="Except", help="Except associated with this Consent Actor.")               
    role_id = fields.Many2one(comodel_name="hc.vs.consent.actor.role", string="Role", required="True", help="How the actor is/was involved.")               
    reference_type = fields.Selection(string="Reference Type", required="True", selection=[("Device", "Device"), ("Group", "Group"), ("Care Team", "Care Team"), ("Organization", "Organization"), ("Patient", "Patient"), ("Practitioner", "Practitioner"), ("Related Person", "Related Person")], help="Type of resource for the actor (or group, by role).")             
    value_name = fields.Char(string="Value", compute="_compute_value_name", store="True", help="Resource for the actor (or group, by role).")               
    reference_device = fields.Many2one(comodel_name="hc.res.device", string="Reference Device", help="Device resource for the actor (or group, by role).")              
    reference_group_id = fields.Many2one(comodel_name="hc.res.group", string="Reference Group", help="Group resource for the actor (or group, by role).")               
    reference_care_team_id = fields.Many2one(comodel_name="hc.res.care.team", string="Reference Care Team", help="CareTeam resource for the actor (or group, by role).")                
    reference_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Reference Organization", help="Organization resource for the actor (or group, by role).")               
    reference_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Reference Patient", help="Patient resource for the actor (or group, by role).")               
    reference_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Reference Practitioner", help="Practitioner resource for the actor (or group, by role).")               
    reference_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Reference Related Person", help="RelatedPerson resource for the actor (or group, by role).")                

class ConsentExceptData(models.Model):    
    _name = "hc.consent.except.data"   
    _description = "Consent Except Data"       

    except_id = fields.Many2one(comodel_name="hc.consent.except", string="Except", help="Except associated with this Consent Data.")                
    meaning = fields.Selection(string="Meaning", required="True", selection=[("instance", "Instance"), ("related", "Related"), ("dependents", "Dependents")], help="How the resource reference is interpreted when testing consent restrictions.")            
    reference_type = fields.Selection(string="Reference Type", required="True", selection=[("string", "String"), ("Consent", "Consent")], help="Type of the actual data reference.")                
    value_name = fields.Char(string="Value", compute="_compute_value_name", store="True", help="The actual data reference.")                
    reference_string = fields.Char(string="Reference String", help="string the actual data reference.")             
    reference_consent_id = fields.Many2one(comodel_name="hc.res.consent", string="Reference Consent", help="Consent the actual data reference.")                

class ConsentConsentor(models.Model):   
    _name = "hc.consent.consentor"  
    _description = "Consent Consentor"      
    _inherit = ["hc.basic.association"]

    consent_id = fields.Many2one(comodel_name="hc.res.consent", string="Consent", help="Consent associated with this Consent Consentor.")               
    consentor_type = fields.Selection(string="Consentor Type", required="True", selection=[("Organization", "Organization"), ("Patient", "Patient"), ("Practitioner", "Practitioner"), ("Related Person", "Related Person")], help="Type of who is agreeing to the policy and exceptions.")             
    value_name = fields.Char(string="Value", compute="_compute_value_name", store="True", help="Who is agreeing to the policy and exceptions.")             
    consentor_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Consentor Organization", help="Organization who is agreeing to the policy and exceptions.")             
    consentor_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Consentor Patient", help="Patient who is agreeing to the policy and exceptions.")             
    consentor_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Consentor Practitioner", help="Practitioner who is agreeing to the policy and exceptions.")             
    consentor_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Consentor Related Person", help="RelatedPerson who is agreeing to the policy and exceptions.")              

class ConsentRecipient(models.Model):   
    _name = "hc.consent.recipient"  
    _description = "Consent Recipient"      
    _inherit = ["hc.basic.association"]

    consent_id = fields.Many2one(comodel_name="hc.res.consent", string="Consent", help="Consent associated with this Consent Recipient.")               
    recipient_type = fields.Selection(string="Recipient Type", selection=[("Device", "Device"), ("Group", "Group"), ("Organization", "Organization"), ("Patient", "Patient"), ("Practitioner", "Practitioner"), ("Related Person", "Related Person"), ("Care Team", "Care Team")], help="Type of whose access is controlled by the policy.")                
    value_name = fields.Char(string="Value", compute="_compute_value_name", store="True", help="Whose access is controlled by the policy.")             
    recipient_device_id = fields.Many2one(comodel_name="hc.res.device", string="Recipient Device", help="Device whose access is controlled by the policy.")             
    recipient_group_id = fields.Many2one(comodel_name="hc.res.group", string="Recipient Group", help="Group whose access is controlled by the policy.")             
    recipient_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Recipient Organization", help="Organization whose access is controlled by the policy.")             
    recipient_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Recipient Patient", help="Patient whose access is controlled by the policy.")             
    recipient_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Recipient Practitioner", help="Practitioner whose access is controlled by the policy.")             
    recipient_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Recipient Related Person", help="RelatedPerson whose access is controlled by the policy.")              
    recipient_care_team_id = fields.Many2one(comodel_name="hc.res.care.team", string="Recipient Care Team", help="CareTeam whose access is controlled by the policy.")              

class ConsentIdentifier(models.Model):  
    _name = "hc.consent.identifier" 
    _description = "Consent Identifier"     
    _inherit = ["hc.basic.association", "hc.identifier"]

class ConsentCategory(models.Model):    
    _name = "hc.consent.category"   
    _description = "Consent Category"       
    _inherit = ["hc.basic.association"]

    consent_id = fields.Many2one(comodel_name="hc.res.consent", string="Consent", help="Consent associated with this Consent Category.")                
    category_id = fields.Many2one(comodel_name="hc.vs.consent.category", string="Category", help="Classification of the consent statement - for indexing/retrieval.")               

class ConsentPurpose(models.Model): 
    _name = "hc.consent.purpose"    
    _description = "Consent Purpose"        
    _inherit = ["hc.basic.association"]

    consent_id = fields.Many2one(comodel_name="hc.res.consent", string="Consent", help="Consent associated with this Consent Purpose.")             
    purpose_id = fields.Many2one(comodel_name="hc.vs.purpose.of.use", string="Purpose", help="Context of activities for which the agreement is made.")              

class ConsentExceptAction(models.Model):    
    _name = "hc.consent.except.action"  
    _description = "Consent Except Action"      
    _inherit = ["hc.basic.association"]

    except_id = fields.Many2one(comodel_name="hc.consent.except", string="Except", help="Except associated with this Consent Except Action.")               
    action_id = fields.Many2one(comodel_name="hc.vs.consent.action", string="Action", help="Actions controlled by this exception.")             

class ConsentExceptSecurityLabel(models.Model): 
    _name = "hc.consent.except.security.label"  
    _description = "Consent Except Security Label"      
    _inherit = ["hc.basic.association"]

    except_id = fields.Many2one(comodel_name="hc.consent.except", string="Except", help="Except associated with this Consent Except Security Label.")               
    security_label_id = fields.Many2one(comodel_name="hc.vs.security.label", string="Security Label", help="Security Labels that define affected resources.")               

class ConsentExceptPurpose(models.Model):   
    _name = "hc.consent.except.purpose" 
    _description = "Consent Except Purpose"     
    _inherit = ["hc.basic.association"]

    except_id = fields.Many2one(comodel_name="hc.consent.except", string="Except", help="Except associated with this Consent Except Purpose.")              
    purpose_id = fields.Many2one(comodel_name="hc.vs.purpose.of.use", string="Purpose", help="Context of activities covered by this exception.")                

class ConsentExceptClass(models.Model): 
    _name = "hc.consent.except.class"   
    _description = "Consent Except Class"       
    _inherit = ["hc.basic.association"]

    except_id = fields.Many2one(comodel_name="hc.consent.except", string="Except", help="Except associated with this Consent Except Class.")                
    class_id = fields.Many2one(comodel_name="hc.vs.consent.content.class", string="Class", help="e.g. Resource Type, Profile, or CDA etc.")             

class ConsentExceptCode(models.Model):  
    _name = "hc.consent.except.code"    
    _description = "Consent Except Code"        
    _inherit = ["hc.basic.association"]

    except_id = fields.Many2one(comodel_name="hc.consent.except", string="Except", help="Except associated with this Consent Except Code.")             
    code_id = fields.Many2one(comodel_name="hc.vs.consent.content.code", string="Code", help="e.g. LOINC or SNOMED CT code, etc in the content.")               

class ConsentSourceAttachment(models.Model):    
    _name = "hc.consent.source.attachment"  
    _description = "Consent Source Attachment"      
    _inherit = ["hc.basic.association", "hc.attachment"]

class ConsentSourceIdentifier(models.Model):    
    _name = "hc.consent.source.identifier"  
    _description = "Consent Source Identifier"      
    _inherit = ["hc.basic.association", "hc.identifier"]

class ConsentAction(models.Model):  
    _name = "hc.vs.consent.action"  
    _description = "Consent Action"     
    _inherit = ["hc.value.set.contains"]

class ConsentActorRole(models.Model):   
    _name = "hc.vs.consent.actor.role"  
    _description = "Consent Actor Role"     
    _inherit = ["hc.value.set.contains"]

class ConsentCategory(models.Model):    
    _name = "hc.vs.consent.category"    
    _description = "Consent Category"       
    _inherit = ["hc.value.set.contains"]

class ConsentContentClass(models.Model):    
    _name = "hc.vs.consent.content.class"   
    _description = "Consent Content Class"      
    _inherit = ["hc.value.set.contains"]

class ConsentContentCode(models.Model): 
    _name = "hc.vs.consent.content.code"    
    _description = "Consent Content Code"       
    _inherit = ["hc.value.set.contains"]
