# -*- coding: utf-8 -*-

from openerp import models, fields, api

class MessageHeader(models.Model):    
    _name = "hc.res.message.header"    
    _description = "Message Header"            

    timestamp = fields.Datetime(
        string="Timestamp", 
        required="True", 
        help="Time that the message was sent.")                    
    event_id = fields.Many2one(
        comodel_name="hc.vs.message.event", 
        string="Event", 
        required="True", 
        help="Code for the event this message represents.")                    
    identifier = fields.Char(
        string="Identifier", 
        required="True", 
        help="Id of this message.")                    
    enterer_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Enterer", 
        help="The source of the data entry.")                    
    author_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Author", 
        help="The source of the decision.")                    
    receiver_type = fields.Selection(
        string="Receiver Type", 
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Organization", "Organization")],
        help='Type of intended "real-world" recipient for the data.')                    
    receiver_name = fields.Char(
        string="Receiver", 
        compute="_compute_receiver_name", 
        store="True", 
        help='Intended "real-world" recipient for the data.')                    
    receiver_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Receiver Practitioner", 
        help='Practitioner intended "real-world" recipient for the data.')                    
    receiver_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Receiver Organization", 
        help='Organization intended "real-world" recipient for the data.')                    
    responsible_type = fields.Selection(
        string="Responsible Type", 
        selection=[
            ("Practitioner", "Practitioner"), 
            ("Organization", "Organization")], 
        help="Type of final responsibility for event.")                    
    responsible_name = fields.Char(
        string="Responsible", 
        compute="_compute_responsible_name", 
        store="True", 
        help="Final responsibility for event.")                    
    responsible_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Responsible Practitioner", 
        help="Practitioner final responsibility for event.")                    
    responsible_organization_id = fields.Many2one(
        comodel_name="hc.res.organization", 
        string="Responsible Organization", 
        help="Organization final responsibility for event.")                    
    reason_id = fields.Many2one(
        comodel_name="hc.vs.message.header.reason", 
        string="Reason", 
        help="Cause of event.")                    
    data_ids = fields.One2many(
        comodel_name="hc.message.header.data", 
        inverse_name="message_header_id", 
        string="Data", 
        help="The actual content of the message.")                    
    response_ids = fields.One2many(
        comodel_name="hc.message.header.response", 
        inverse_name="message_header_id", 
        string="Responses", 
        help="If this is a reply to prior message.")                    
    source_ids = fields.One2many(
        comodel_name="hc.message.header.source", 
        inverse_name="message_header_id", 
        string="Sources", 
        required="True", 
        help="Message Source Application.")                    
    destination_ids = fields.One2many(
        comodel_name="hc.message.header.destination", 
        inverse_name="message_header_id", 
        string="Destinations", 
        help="Message Destination Application(s).")                    

class MessageHeaderResponse(models.Model):    
    _name = "hc.message.header.response"    
    _description = "Message Header Response"            

    message_header_id = fields.Many2one(
        comodel_name="hc.res.message.header", 
        string="Message Header", 
        help="Message Header associated with this Message Header Response.")                    
    identifier = fields.Char(
        string="Identifier", 
        required="True", 
        help="Id of original message.")                    
    code = fields.Selection(
        string="Response Code", 
        required="True", 
        selection=[
            ("ok", "Ok"), 
            ("transient-error", "Transient Error"), 
            ("fatal-error", "Fatal Error")], 
        help="Code that identifies the type of response to the message - whether it was successful or not, and whether it should be resent or not.")                    
    details_id = fields.Many2one(
        comodel_name="hc.res.operation.outcome", 
        string="Details", 
        help="Specific list of hints/warnings/errors.")                    

class MessageHeaderSource(models.Model):    
    _name = "hc.message.header.source"    
    _description = "Message Header Source"            

    message_header_id = fields.Many2one(
        comodel_name="hc.res.message.header", 
        string="Message Header", 
        help="Message Header associated with this Message Header Source.")                    
    name = fields.Char(
        string="Name", 
        help="Name of system.")                    
    software = fields.Char(
        string="Software", 
        help="Name of software running the system.")                    
    version = fields.Char(
        string="Version", 
        help="Version of software running.")                    
    contact_id = fields.Many2one(
        comodel_name="hc.message.header.source.contact", 
        string="Contact", 
        help="Human contact for problems.")                    
    endpoint = fields.Char(
        string="Endpoint URI", 
        required="True", 
        help="Actual message source address or id.")                    

class MessageHeaderDestination(models.Model):    
    _name = "hc.message.header.destination"    
    _description = "Message Header Destination"            

    message_header_id = fields.Many2one(
        comodel_name="hc.res.message.header", 
        string="Message Header", 
        help="Message Header associated with this Message Header Destination.")                    
    name = fields.Char(
        string="Name", 
        help="Name of system.")                    
    target_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Target", 
        help="Particular delivery destination within the destination.")                    
    endpoint = fields.Char(
        string="Endpoint URI", 
        required="True", 
        help="Actual destination address or id.")                    

class MessageHeaderData(models.Model):    
    _name = "hc.message.header.data"    
    _description = "Message Header Data"        
    _inherit = ["hc.basic.association"]    

    message_header_id = fields.Many2one(
        comodel_name="hc.res.message.header", 
        string="Message Header", 
        help="Message Header associated with this Message Header Data.")                    
    data_type = fields.Selection(
        string="Data Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help='Type of the actual content of the message.')                    
    data_name = fields.Char(
        string="Data", 
        compute="_compute_data_name", 
        store="True", 
        help='The actual content of the message.')                    
    data_string = fields.Text(
        string="Data String", 
        help="String of the actual content of the message.")                    
    data_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Data Code", 
        help="Type of resource of actual content of the message.")                    

class MessageHeaderSourceContact(models.Model):    
    _name = "hc.message.header.source.contact"    
    _description = "Message Header Source Contact"        
    _inherit = ["hc.contact.point.use"]    
    _inherits = {"hc.contact.point": "contact_id"}

    contact_id = fields.Many2one(
        comodel_name="hc.contact.point", 
        string="Contact", 
        ondelete="restrict", 
        required="True", 
        help="Telecom associated with this Message Header Source Contact.")                     

class MessageHeaderReason(models.Model):    
    _name = "hc.vs.message.header.reason"    
    _description = "Message Header Reason"        
    _inherit = ["hc.value.set.contains"]    
