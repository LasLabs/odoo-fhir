# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Provenance(models.Model):    
    _name = "hc.res.provenance"    
    _description = "Provenance"        

    target_ids = fields.One2many(comodel_name="hc.provenance.target", inverse_name="provenance_id", string="Targets", required="True", help="Target Reference(s) (usually version specific).")                
    start_date = fields.Datetime(string="Start Date", help="Start of the when the activity occurred.")                
    end_date = fields.Datetime(string="End Date", help="End of the when the activity occurred.")                
    recorded = fields.Datetime(string="Recorded Date", required="True", help="When the activity was recorded / updated.")                
    reason_id = fields.Many2one(comodel_name="hc.vs.purpose.of.use", string="Reason", help="Reason the activity is occurring.")                
    activity_id = fields.Many2one(comodel_name="hc.vs.provenance.activity", string="Activity", help="Activity that occurred.")                
    location_id = fields.Many2one(comodel_name="hc.res.location", string="Location", help="Where the activity occurred, if relevant.")                
    policy_ids = fields.One2many(comodel_name="hc.provenance.policy", inverse_name="provenance_id", string="Policies", help="URL of policy or plan the activity was defined by.")                
    signature_ids = fields.One2many(comodel_name="hc.provenance.signature", inverse_name="provenance_id", string="Signatures", help="Signature on target.")                
    entity_ids = fields.One2many(comodel_name="hc.provenance.entity", inverse_name="provenance_id", string="Entities", help="An entity used in this activity.")                
    agent_ids = fields.One2many(comodel_name="hc.provenance.agent", inverse_name="provenance_id", string="Agents", help="Agents involved in creating resource.")                

class ProvenanceEntity(models.Model):    
    _name = "hc.provenance.entity"    
    _description = "Provenance Entity"        

    provenance_id = fields.Many2one(comodel_name="hc.res.provenance", string="Provenance", help="Provenance associated with this entity.")                
    role = fields.Selection(string="Entity Role", required="True", selection=[("derivation", "Derivation"), ("revision", "Revision"), ("quotation", "Quotation"), ("source", "Source")], help="How the entity was used during the activity.")                
    type_id = fields.Many2one(comodel_name="hc.vs.resource.type", string="Type", required="True", help="Entity Type.")                
    reference = fields.Char(string="Reference", required="True", help="Identity of entity.")                
    display = fields.Char(string="Display", help="Human description of entity.")                
    agent_ids = fields.One2many(comodel_name="hc.provenance.agent", inverse_name="entity_id", string="Agents", help="Agents involved in creating resource.")

class ProvenanceAgent(models.Model):    
    _name = "hc.provenance.agent"    
    _description = "Provenance Agent"        

    provenance_id = fields.Many2one(comodel_name="hc.res.provenance", string="Provenance", help="Provenance associated with this agent.")                
    entity_id = fields.Many2one(comodel_name="hc.provenance.entity", string="Entity", help="Entity associated with this Provenance Agent.")
    role_id = fields.Many2one(comodel_name="hc.vs.provenance.agent.role", string="Role", required="True", help="Agents Role.")                
    actor_type = fields.Selection(string="Actor Type", selection=[("Practitioner", "Practitioner"), ("Related Person", "Related Person"), ("Patient", "Patient"), ("Device", "Device"), ("Organization", "Organization")], help="Type of individual, device or organization playing role.")                
    actor_name = fields.Char(string="Actor", compute="_compute_actor_name", store="True", help="Individual, device or organization playing role.")                
    actor_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Actor Practitioner", help="Practitioner playing role.")                
    actor_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Actor Related Person", help="Related Person playing role.")                
    actor_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Actor Patient", help="Patient playing role.")                
    actor_device_id = fields.Many2one(comodel_name="hc.res.device", string="Actor Device", help="Device playing role.")                
    actor_organization_id = fields.Many2one(comodel_name="hc.res.organization", string="Actor Organization", help="Organization playing role.")                
    user_id = fields.Many2one(comodel_name="hc.provenance.agent.user", string="User", help="Authorization-system identifier for the agent.")                
    related_agent_ids = fields.One2many(comodel_name="hc.provenance.related.agent", inverse_name="agent_id", string="Related Agents", help="Track delegation between agents.")

class ProvenanceRelatedAgent(models.Model):    
    _name = "hc.provenance.related.agent"    
    _description = "Provenance Related Agent"        

    agent_id = fields.Many2one(comodel_name="hc.provenance.agent", string="Agent", help="Agent associated with this Provenance Related Agent.")   
    type_id = fields.Many2one(comodel_name="hc.vs.role.link.type", string="Type", required="True", help="Type of relationship between agents.")                
    display = fields.Char(string="Display", required="True", help="Reference to other agent in this resource by identifier.")                

class ProvenanceAgentUser(models.Model):    
    _name = "hc.provenance.agent.user"    
    _description = "Provenance Agent User"        
    _inherit = ["hc.identifier"]

class ProvenancePolicy(models.Model):    
    _name = "hc.provenance.policy"    
    _description = "Provenance Policy"        
    _inherit = ["hc.basic.association"]

    provenance_id = fields.Many2one(comodel_name="hc.res.provenance", string="Provenance", help="Provenance associated with this Provenance Policy.")                
    policy_url = fields.Char(string="Policy URL", help="Policy URL associated with this Provenance Policy.")                

class ProvenanceSignature(models.Model):    
    _name = "hc.provenance.signature"    
    _description = "Provenance Signature"        
    _inherit = ["hc.basic.association", "hc.signature"]

    provenance_id = fields.Many2one(comodel_name="hc.res.provenance", string="Provenance", help="Provenance associated with this Provenance Signature.")                

class ProvenanceTarget(models.Model):    
    _name = "hc.provenance.target"    
    _description = "Provenance Target"        
    _inherit = ["hc.basic.association"]

    provenance_id = fields.Many2one(comodel_name="hc.res.provenance", string="Provenance", help="Provenance associated with this Provenance Target.")                
    target_type = fields.Selection(string="Target Type", selection=[("string", "String"), ("Providence", "Providence")], help="Type of individual, device or organization playing role.")                
    target_name = fields.Char(string="Target", compute="_compute_target_name", store="True", help="Target Reference(s) (usually version specific).")                
    target_string = fields.Char(string="Target String", help="String target reference(s) (usually version specific).")                
    target_provenance_id = fields.Many2one(comodel_name="hc.res.provenance", string="Target Provenance", help="Provenance target reference(s) (usually version specific).")                

class ProvenanceActivity(models.Model):    
    _name = "hc.vs.provenance.activity"    
    _description = "Provenance Activity"        
    _inherit = ["hc.value.set.contains"]

class ProvenanceAgentRole(models.Model):    
    _name = "hc.vs.provenance.agent.role"    
    _description = "Provenance Agent Role"        
    _inherit = ["hc.value.set.contains"]

class ProvenanceRelatedAgentType(models.Model):    
    _name = "hc.vs.role.link.type"    
    _description = "Role Link Type"        
    _inherit = ["hc.value.set.contains"]
