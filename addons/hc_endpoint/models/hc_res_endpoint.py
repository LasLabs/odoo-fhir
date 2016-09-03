# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Endpoint(models.Model):   
    _name = "hc.res.endpoint"   
    _description = "Endpoint"           
    
    identifier_ids = fields.One2many(
        comodel_name="hc.endpoint.identifier", 
        inverse_name="endpoint_id", 
        string="Identifiers", 
        help="Identifies this endpoint across multiple systems.")                    
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("active", "Active"), 
            ("suspended", "Suspended"), 
            ("error", "Error"), 
            ("off", "Off"), 
            ("entered-in-error", "Entered-In-Error")], 
        help="The status of the encounter.")                    
    name = fields.Char(
        string="Name", 
        help="A name that this endpoint can be identified by.")                   
    managing_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Managing Organization", 
        help="Organization that manages this endpoint (may not be the organization that exposes the endpoint).")                    
    contact_ids = fields.One2many(
        comodel_name="hc.endpoint.telecom", 
        inverse_name="endpoint_id", 
        string="Telecom", 
        help="Contact details for source (e.g. troubleshooting).")                    
    connection_type_id = fields.Many2one(
        comodel_name="hc.vs.subscription.channel.type", 
        string="Connection Type", 
        required="True", 
        help="rest-hook | websocket | email | sms | message.")                 
    method_ids = fields.Many2many(
        comodel_name="hc.vs.http.verb", 
        string="Methods", 
        help="The http verb to be used when calling this endpoint.")                   
    period_start_date = fields.Datetime(
        string="Period Start Date", 
        help="Start of the interval during responsibility is assumed.")                 
    period_end_date = fields.Datetime(
        string="Period End Date", 
        help="End of the interval during responsibility is assumed.")                   
    address_uri = fields.Char(
        string="Address URL", 
        required="True", 
        help="Where the channel points to.")                   
    payload_format = fields.Char(
        string="Payload Format", 
        required="True", 
        help="MIME type to send, or blank for no payload.")                   
    payload_type_ids = fields.One2many(
        comodel_name="hc.endpoint.payload.type", 
        inverse_name="endpoint_id", 
        string="Payload Types", 
        help="The type of content that may be used at this endpoint (e.g. XDS Discharge summaries).")                  
    header_ids = fields.One2many(
        comodel_name="hc.endpoint.header", 
        inverse_name="endpoint_id", 
        string="Headers", 
        help="Usage depends on the channel type.")                   
    public_key = fields.Char(
        string="Public Key", 
        help="PKI Public keys to support secure communications.")                 

class EndpointIdentifier(models.Model): 
    _name = "hc.endpoint.identifier"    
    _description = "Endpoint Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    endpoint_id = fields.Many2one(
        comodel_name="hc.res.endpoint", 
        string="Endpoint", 
        help="Endpoint associated with this endpoint identifier.")                    

class EndpointTelecom(models.Model):    
    _name = "hc.endpoint.telecom"   
    _description = "Endpoint Telecom"       
    _inherit = ["hc.telecom.contact.point"] 
    _inherits = {"hc.telecom": "telecom_id"}

    telecom_id = fields.Many2one(
        comodel_name="hc.telecom",
        string="Telecom",
        required="True",
        ondelete="restrict",
        help="Telecom contact point associated with this endpoint telecom.")
    endpoint_id = fields.Many2one(
        comodel_name="hc.res.endpoint", 
        string="Endpoint", 
        help="Endpoint associated with with this endpoint telecom.")                   

class EndpointHeader(models.Model): 
    _name = "hc.endpoint.header"    
    _description = "Endpoint Header"        
    _inherit = ["hc.basic.association"] 
    
    endpoint_id = fields.Many2one(
        comodel_name="hc.res.endpoint", 
        string="Endpoint", 
        help="Endpoint associated with this endpoint header.")                    
    header = fields.Char(
        string="Header", 
        help="Usage depends on the channel type.")                    

class EndpointPayloadType(models.Model):    
    _name = "hc.endpoint.payload.type"  
    _description = "Endpoint Payload Type"      
    _inherit = ["hc.basic.association"] 
    
    endpoint_id = fields.Many2one(
        comodel_name="hc.res.endpoint", 
        string="Endpoint", 
        help="Endpoint associated with this endpoint payload type.")                  
    payload_type_id = fields.Many2one(
        comodel_name="hc.vs.endpoint.payload.type", 
        string="Payload Type", 
        help="Payload type associated with this endpoint payload type.")                   

class HttpVerb(models.Model):   
    _name = "hc.vs.http.verb"   
    _description = "HTTP Verb"      
    _inherit = ["hc.value.set.contains"]    

class SubscriptionChannelType(models.Model):    
    _name = "hc.vs.subscription.channel.type"   
    _description = "Subscription Channel Type"      
    _inherit = ["hc.value.set.contains"]    

class EndpointPayloadType(models.Model):    
    _name = "hc.vs.endpoint.payload.type"   
    _description = "Endpoint Payload Type"      
    _inherit = ["hc.value.set.contains"]    
