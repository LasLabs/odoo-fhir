# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Schedule(models.Model):    
    _name = "hc.res.schedule"    
    _description = "Schedule"        

    identifier_ids = fields.One2many(comodel_name="hc.schedule.identifier", inverse_name="schedule_id", string="Identifiers", help="External Ids for this item.")                
    is_active = fields.Boolean(string="Active", help="Whether this schedule is in active use.")                
    service_category_id = fields.Many2one(comodel_name="hc.vs.service.category", string="Service Category", help="A broad categorisation of the service that is to be performed during this appointment.")                
    service_type_ids = fields.Many2many(comodel_name="hc.vs.service.type", string="Service Types", help="The specific service that is to be performed during this appointment.")                
    specialty_ids = fields.Many2many(comodel_name="hc.vs.c80.practice.code", string="Specialties", help="The specialty of a practitioner that would be required to perform the service requested in this appointment.")                
    actor_type = fields.Selection(string="Actor Type", required="True", selection=[("Healthcare Service", "Healthcare Service"), ("Location", "Location"), ("Practitioner", "Practitioner"), ("Device", "Device"), ("Patient", "Patient"), ("Related Person", "Related Person")], help="Type of resource this Schedule resource is providing availability information for.")                
    actor_name = fields.Char(string="Actor", compute="_compute_actor_name", store="True", help="The resource this Schedule resource is providing availability information for.")                
    actor_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Actor Patient", required="True", help="Patient resource this schedule resource is providing availability information for.")                
    actor_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Actor Practitioner", help="Practitioner resource this schedule resource is providing availability information for.")                
    actor_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Actor Related Person", help="Related Person resource this schedule resource is providing availability information for.")                
    actor_device_id = fields.Many2one(comodel_name="hc.res.device", string="Actor Device", help="Device resource this schedule resource is providing availability information for.")                
    actor_healthcare_service_id = fields.Many2one(comodel_name="hc.res.healthcare.service", string="Actor Healthcare Service", help="Healthcare Service resource this schedule resource is providing availability information for.")                
    actor_location_id = fields.Many2one(comodel_name="hc.res.location", string="Actor Location", help="Location resource this schedule resource is providing availability information for.")                
    planning_horizon_start_date = fields.Datetime(string="Planning Horizon Start Date", 
        help="Start of the the period of time that the slots that are attached to this schedule resource cover (even if none exist).")                
    planning_horizon_end_date = fields.Datetime(string="Planning Horizon End Date", 
        help="End of the the period of time that the slots that are attached to this schedule resource cover (even if none exist).")                
    comment = fields.Text(string="Comment", 
        help="Comments on the availability to describe any extended information.")                

class ScheduleIdentifier(models.Model):    
    _name = "hc.schedule.identifier"    
    _description = "Schedule Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    schedule_id = fields.Many2one(comodel_name="hc.res.schedule", string="Schedule", help="Schedule associated with this Schedule Identifier." )                
