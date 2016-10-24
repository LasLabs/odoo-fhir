# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AuditEvent(models.Model):    
    _name = "hc.res.audit.event"    
    _description = "Audit Event"        

    type_id = fields.Many2one(comodel_name="hc.vs.audit.event.type", string="Type", required="True", help="Type/identifier of event.")                
    subtype_ids = fields.Many2many(comodel_name="hc.vs.audit.event.sub.type", string="Subtypes", help="More specific type/id for the event.")                
    action_id = fields.Many2one(comodel_name="hc.vs.audit.event.action", string="Action", help="Type of action performed during the event.")                
    date_time = fields.Datetime(string="Date Time", required="True", help="Time when the event occurred on source.")                
    outcome_id = fields.Many2one(comodel_name="hc.vs.audit.event.outcome", string="Outcome", help="Whether the event succeeded or failed.")                
    outcome_desc = fields.Text(string="Outcome Desc", help="Description of the event outcome.")                
    purpose_of_event_ids = fields.One2many(comodel_name="hc.audit.event.purpose.of.event", inverse_name="audit_event_id", string="Purpose Of Events", help="Coding The purposeOfUse of the event.")                
    source_ids = fields.One2many(comodel_name="hc.audit.event.source", inverse_name="audit_event_id", string="Sources", required="True", help="Application systems and processes.")                
    agent_ids = fields.One2many(comodel_name="hc.audit.event.agent", inverse_name="audit_event_id", string="Agents", required="True", help="Actor involved in the event.")                
    entity_ids = fields.One2many(comodel_name="hc.audit.event.entity", inverse_name="audit_event_id", string="Entities", help="Data or objects used.")                

class AuditEventAgent(models.Model):    
    _name = "hc.audit.event.agent"    
    _description = "Audit Event Agent"        

    audit_event_id = fields.Many2one(comodel_name="hc.res.audit.event", string="Audit Event", help="Audit Event associated with this Audit Event Agent.")                
    role_ids = fields.Many2many(comodel_name="hc.vs.dicm.402.roleid", string="Roles", help="User roles (e.g. local RBAC codes).")              
    reference_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Reference Practitioner", help="Practitioner direct reference to resource.")                
    reference_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Reference Organization", help="Organization direct reference to resource.")                
    reference_device_id = fields.Many2one(comodel_name="hc.res.device", string="Reference Device", help="Device direct reference to resource.")                
    reference_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Reference Patient", help="Patient direct reference to resource.")                
    reference_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Reference Related Person", help="Related Person direct reference to resource.")                
    user_id = fields.Many2one(comodel_name="hc.audit.event.agent.user", string="User", help="Identifier Unique identifier for the user.")                
    alt_id = fields.Char(string="Alt Id", help="Alternative User id e.g. authentication.")                
    name = fields.Char(string="Name", help="Human-meaningful name for the user.")                
    is_requestor = fields.Boolean(string="Requestor", required="True", help="Whether user is initiator.")                
    location_id = fields.Many2one(comodel_name="hc.res.location", string="Location", help="Where.")                
    policy_ids = fields.One2many(comodel_name="hc.audit.event.agent.policy", inverse_name="agent_id", string="Policy URLs", help="URL of policy that authorized event.")                
    media_id = fields.Many2one(comodel_name="hc.vs.dicm.405.mediatype", string="Media", help="Type of media.")                
    network_ids = fields.One2many(comodel_name="hc.audit.event.agent.network", inverse_name="agent_id", string="Networks", help="Logical network location for application activity.")                

class AuditEventAgentNetwork(models.Model):    
    _name = "hc.audit.event.agent.network"    
    _description = "Audit Event Agent Network"        

    agent_id = fields.Many2one(comodel_name="hc.audit.event.agent", string="Agent", help="Agent associated with this Audit Event Agent Network.")                
    address = fields.Char(string="Address", help="Identifier for the network access point of the user device.")                
    type_id = fields.Many2one(comodel_name="hc.vs.network.type", string="Type", help="The type of network access point.")                
    purpose_of_use_ids = fields.One2many(comodel_name="hc.audit.event.agent.network.purpose.of.use", inverse_name="network_id", string="Purposes Of Use", help="Coding Participant purposeOfUse.")                

class AuditEventSource(models.Model):    
    _name = "hc.audit.event.source"    
    _description = "Audit Event Source"        

    audit_event_id = fields.Many2one(comodel_name="hc.res.audit.event", string="Audit Event", help="Audit Event associated with this Audit Event Source.")                
    site = fields.Char(string="Site", help="Logical source location within the enterprise.")                
    identifier = fields.Char(string="Identifier", required="True", help="The id of source where event originated.")                
    type_ids = fields.One2many(comodel_name="hc.audit.event.source.type", inverse_name="source_id", string="Types", help="Coding The type of source where event originated.")                

class AuditEventEntity(models.Model):    
    _name = "hc.audit.event.entity"    
    _description = "Audit Event Entity"        

    audit_event_id = fields.Many2one(comodel_name="hc.res.audit.event", string="Audit Event", help="Audit Event associated with this Audit Event Entity.")                
    identifier_id = fields.Many2one(comodel_name="hc.audit.event.entity.identifier", string="Identifier", help="Specific instance of object (e.g. versioned).")                
    reference_id = fields.Many2one(comodel_name="hc.audit.event.entity.reference", string="Reference", help="Specific instance of resource (e.g. versioned).")                
    type_id = fields.Many2one(comodel_name="hc.vs.audit.source.type", string="Type", help="Type of entity involved.")                
    role_id = fields.Many2one(comodel_name="hc.vs.object.type", string="Role", help="What role the entity played.")                
    lifecycle_id = fields.Many2one(comodel_name="hc.vs.object.lifecycle", string="Lifecycle", help="Life-cycle stage for the entity.")                
    security_label_ids = fields.One2many(comodel_name="hc.audit.event.entity.security.label", inverse_name="entity_id", string="Security Labels", help="Security labels on the entity.")                
    name = fields.Text(string="Name", help="Instance-specific descriptor for Object.")                
    description = fields.Text(string="Description", help="Descriptive text.")                
    query = fields.Binary(string="Query", help="Actual query for object.")                
    detail_ids = fields.One2many(comodel_name="hc.audit.event.entity.detail", inverse_name="entity_id", string="Details", help="Additional Information about the Object.")                

class AuditEventEntityDetail(models.Model):    
    _name = "hc.audit.event.entity.detail"    
    _description = "Audit Event Entity Detail"        

    entity_id = fields.Many2one(comodel_name="hc.audit.event.entity", string="Entity", help="Entity associated with this Audit Event Entity Detail.")                
    type = fields.Char(string="Type", required="True", help="Name of the property.")                
    value = fields.Binary(string="Value", required="True", help="Property value.")                

class AuditEventPurposeOfEvent(models.Model):    
    _name = "hc.audit.event.purpose.of.event"    
    _description = "Audit Event Purpose Of Event"        
    _inherit = ["hc.basic.association"]

    audit_event_id = fields.Many2one(comodel_name="hc.res.audit.event", string="Audit Event", help="Audit Event associated with this Audit Event Purpose Of Event.")                
    purpose_of_event_id = fields.Many2one(comodel_name="hc.vs.purpose.of.use", string="Purpose Of Event", help="The purposeOfUse of the event.")                

class AuditEventAgentUser(models.Model):    
    _name = "hc.audit.event.agent.user" 
    _description = "Audit Event Agent User"     
    _inherit = ["hc.basic.association", "hc.identifier"]

class AuditEventAgentRole(models.Model):    
    _name = "hc.audit.event.agent.role" 
    _description = "Audit Event Agent Role"     
    _inherit = ["hc.basic.association"]

    agent_id = fields.Many2one(comodel_name="hc.audit.event.agent", string="Agent", help="Agent associated with this Agent Event Agent Role.")                
    role_id = fields.Many2one(comodel_name="hc.vs.dicm.402.roleid", string="Role", help="User roles (e.g. local RBAC codes).")                

class AuditEventAgentPolicy(models.Model):    
    _name = "hc.audit.event.agent.policy"    
    _description = "Audit Event Agent Policy"        
    _inherit = ["hc.basic.association"]

    agent_id = fields.Many2one(comodel_name="hc.audit.event.agent", string="Agent", help="Agent associated with this Audit Event Agent Policy.")                
    policy_url = fields.Char(string="Policy URL", help="URL of Policy associated with this Audit Event Agent Policy.")                

class AuditEventAgentNetworkPurposeOfUse(models.Model):    
    _name = "hc.audit.event.agent.network.purpose.of.use"    
    _description = "Audit Event Agent Network Purpose Of Use"        
    _inherit = ["hc.basic.association"]

    network_id = fields.Many2one(comodel_name="hc.audit.event.agent.network", string="Network", help="Network associated with this Audit Event Agent Network Purpose Of Use.")                
    purpose_of_use_id = fields.Many2one(comodel_name="hc.vs.purpose.of.use", string="Purpose Of Use", help="Participant purposeOfUse.")                

class AuditEventSourceType(models.Model):    
    _name = "hc.audit.event.source.type"    
    _description = "Audit Event Source Type"        
    _inherit = ["hc.basic.association"]

    source_id = fields.Many2one(comodel_name="hc.audit.event.source", string="Source", help="Source associated with this Audit Event Source Type.")                
    type_id = fields.Many2one(comodel_name="hc.vs.audit.event.type", string="Type", help="The type of source where event originated.")                

class AuditEventEntityIdentifier(models.Model): 
    _name = "hc.audit.event.entity.identifier"  
    _description = "Audit Event Entity Identifier"      
    _inherit = ["hc.basic.association", "hc.identifier"]

class AuditEventEntityReference(models.Model):  
    _name = "hc.audit.event.entity.reference"   
    _description = "Audit Event Entity Reference"       
    _inherit = ["hc.basic.association"]
    
class AuditEventEntitySecurityLabel(models.Model):    
    _name = "hc.audit.event.entity.security.label"    
    _description = "Audit Event Entity Security Label"        
    _inherit = ["hc.basic.association"]

    entity_id = fields.Many2one(comodel_name="hc.audit.event.entity", string="Entity", help="Entity associated with this Audit Event Entity Security Label.")                
    security_label_id = fields.Many2one(comodel_name="hc.vs.security.label", string="Security Label", help="Security labels on the entity.")                

class AuditEventType(models.Model):    
    _name = "hc.vs.audit.event.type"    
    _description = "Audit Event Type"        
    _inherit = ["hc.value.set.contains"]

class AuditEventAction(models.Model):    
    _name = "hc.vs.audit.event.action"    
    _description = "Audit Event Action"        
    _inherit = ["hc.value.set.contains"]

class AuditEventOutcome(models.Model):    
    _name = "hc.vs.audit.event.outcome"    
    _description = "Audit Event Outcome"        
    _inherit = ["hc.value.set.contains"]

class Dicm405Mediatype(models.Model):    
    _name = "hc.vs.dicm.405.mediatype"    
    _description = "Dicm 405 Mediatype"        
    _inherit = ["hc.value.set.contains"]

class NetworkType(models.Model):    
    _name = "hc.vs.network.type"    
    _description = "Network Type"        
    _inherit = ["hc.value.set.contains"]

class AuditSourceType(models.Model):    
    _name = "hc.vs.audit.source.type"    
    _description = "Audit Source Type"        
    _inherit = ["hc.value.set.contains"]

class ObjectType(models.Model):    
    _name = "hc.vs.object.type"    
    _description = "Object Type"        
    _inherit = ["hc.value.set.contains"]

class ObjectLifecycle(models.Model):    
    _name = "hc.vs.object.lifecycle"    
    _description = "Object Lifecycle"        
    _inherit = ["hc.value.set.contains"]

class AuditEventSubType(models.Model):    
    _name = "hc.vs.audit.event.sub.type"    
    _description = "Audit Event Sub Type"        
    _inherit = ["hc.value.set.contains"]

class Dicm402Roleid(models.Model):    
    _name = "hc.vs.dicm.402.roleid"    
    _description = "Dicm 402 Roleid"        
    _inherit = ["hc.value.set.contains"]

class AuditEventType(models.Model):    
    _name = "hc.vs.audit.event.type"    
    _description = "Audit Event Type"        
    _inherit = ["hc.value.set.contains"]
