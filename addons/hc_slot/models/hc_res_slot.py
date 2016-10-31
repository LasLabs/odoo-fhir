# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Slot(models.Model):    
    _name = "hc.res.slot"    
    _description = "Slot"        

    identifier_ids = fields.One2many(
        comodel_name="hc.slot.identifier", 
        inverse_name="slot_id", 
        string="Identifiers", 
        help="External Ids for this item.")                
    service_category_id = fields.Many2one(
        comodel_name="hc.vs.service.category", 
        string="Service Category", 
        help="A broad categorisation of the service that is to be performed during this appointment.")                
    service_type_ids = fields.Many2many(
        comodel_name="hc.vs.service.type", 
        string="Service Types", 
        help="The type of appointments that can be booked into this slot (ideally this would be an identifiable service - which is at a location, rather than the location itself). If provided then this overrides the value provided on the availability resource.")                
    specialty_ids = fields.Many2many(
        comodel_name="hc.vs.c80.practice.code", 
        string="Specialties", 
        help="The specialty of a practitioner that would be required to perform the service requested in this appointment.")                
    type_id = fields.Many2one(
        comodel_name="hc.vs.v2.appointment.reason.code", 
        string="Type", 
        help="The style of appointment or patient that has been booked in the slot (not service type).")                
    schedule_id = fields.Many2one(
        comodel_name="hc.res.schedule", 
        string="Schedule", 
        required="True", 
        help="The schedule resource that this slot defines an interval of status information.")                
    status = fields.Selection(
        string="Slot Status", 
        required="True", 
        selection=[("busy", "Busy"), ("free", "Free"), ("busy-unavailable", "Busy-Unavailable"), ("busy-tentative", "Busy-Tentative"), ("entered-in-error", "Entered-In-Error")], 
        help="The free/busy status of the slot.")                
    start = fields.Datetime(
        string="Start Date", 
        required="True", 
        help="Date/Time that the slot is to begin.")                
    end = fields.Datetime(
        string="End Date", 
        required="True", 
        help="Date/Time that the slot is to conclude.")                
    is_overbooked = fields.Boolean(
        string="Overbooked", 
        help="This slot has already been overbooked, appointments are unlikely to be accepted for this time.")                
    comment = fields.Text(
        string="Comment", 
        help="Comments on the slot to describe any extended information. Such as custom constraints on the slot.")                

class SlotIdentifier(models.Model):    
    _name = "hc.slot.identifier"    
    _description = "Slot Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    slot_id = fields.Many2one(
        comodel_name="hc.res.slot", 
        string="Slot", 
        help="Slot associated with this Slot Identifier.")                

class V2AppointmentReasonCode(models.Model):    
    _name = "hc.vs.v2.appointment.reason.code"  
    _description = "V2 Appointment Reason Code"     
    _inherit = ["hc.value.set.contains"]
