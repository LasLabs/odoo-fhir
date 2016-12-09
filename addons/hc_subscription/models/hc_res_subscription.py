# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Subscription(models.Model):    
    _name = "hc.res.subscription"    
    _description = "Subscription"

    criteria = fields.Text(
        string="Criteria", 
        required="True", 
        help="Rule for server push criteria.")                    
    contact_ids = fields.One2many(
        comodel_name="hc.subscription.contact", 
        inverse_name="subscription_id", 
        string="Contacts", 
        help="Contact details for source (e.g. troubleshooting).")                    
    reason = fields.Text(
        string="Reason", 
        required="True", 
        help="Description of why this subscription was created.")                    
    status = fields.Selection(
        string="Status", 
        required="True", 
        selection=[
            ("requested", "Requested"), 
            ("active", "Active"), 
            ("error", "Error"), 
            ("off", "Off")], 
        help="The status of the subscription, which marks the server state for managing the subscription.")
    error = fields.Text(string="Error", help="Latest error note.")
    end = fields.Datetime(
        string="End", 
        help="When to automatically delete the subscription.")                  
    tag_ids = fields.Many2many(
        comodel_name="hc.vs.subscription.tag", 
        relation="subscription_tag_rel", 
        string="Tags", 
        help="A tag to add to matching resources.")
    channel_ids = fields.One2many(
        comodel_name="hc.subscription.channel", 
        inverse_name="subscription_id", 
        string="Channels", 
        required="True", 
        help="The channel on which to report matches to the criteria.")                    

class SubscriptionChannel(models.Model):    
    _name = "hc.subscription.channel"    
    _description = "Subscription Channel"            

    subscription_id = fields.Many2one(
        comodel_name="hc.res.subscription", 
        string="Subscription", 
        help="Subscription associated with this Channel.")
    type = fields.Selection(
        string="Type", 
        required="True", 
        selection=[
            ("rest_hook", "REST Hook"), 
            ("websocket", "Websocket"), 
            ("email", "Email"), 
            ("sms", "SMS"), 
            ("message", "Message")], 
        help="The type of channel to send notifications on.")
    endpoint = fields.Char(
        string="URI", 
        help="Where the channel points to.")
    payload = fields.Char(
        string="Payload", 
        help="Mimetype to send, or omit for no payload.")
    header = fields.Char(
        string="Header", 
        help="Usage depends on the channel type.")               

class SubscriptionContact(models.Model):    
    _name = "hc.subscription.contact"   
    _description = "Subscription Contact"           
    _inherit = ["hc.contact.point.use"] 
    _inherits = {"hc.contact.point": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.point", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Telecom associated with this Subscription Contact.")                        
    subscription_id = fields.Many2one(
        comodel_name="hc.res.subscription", 
        string="Subscription", 
        help="Subscription associated with this Subscription Contact.")                        
                   
class SubscriptionTag(models.Model):    
    _name = "hc.vs.subscription.tag"    
    _description = "Subscription Tag"        
    _inherit = ["hc.value.set.contains"]    
