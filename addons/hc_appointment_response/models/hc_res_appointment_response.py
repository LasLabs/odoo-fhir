# -*- coding: utf-8 -*-

from openerp import models, fields, api

class AppointmentResponse(models.Model):    
    _name = "hc.res.appointment.response"    
    _description = "Appointment Response"
    _rec_name = "appointment_id"

    identifier_ids = fields.One2many(
        comodel_name="hc.appointment.response.identifier", 
        inverse_name="appointment_response_id", 
        string="Identifiers", 
        help="External Ids for this item.")                    
    appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Appointment", 
        required="True", 
        help="Parent appointment that this response is replying to.")                    
    start = fields.Datetime(
        string="Start Date", 
        help="Date/Time that the appointment is to take place, or requested new start time.")                    
    end = fields.Datetime(
        string="End Date", 
        help="Date/Time that the appointment is to conclude, or requested new end time.")                    
    participant_type_ids = fields.Many2many(
        comodel_name="hc.vs.encounter.participant.type", 
        relation="appointment_response_participant_type_rel",
        string="Participant Types",
        help="Role of participant in the appointment.")                    
    actor_type = fields.Selection(
        string="Actor Type", 
        selection=[
            ("patient", "Patient"), 
            ("practitioner", "Practitioner"), 
            ("related_person", "Related Person"), 
            ("device", "Device"), 
            ("healthcare_service", "Healthcare Service"), 
            ("location", "Location")], 
        help="Type of what is account tied to.")                    
    actor_name = fields.Char(
        string="Actor", 
        compute="_compute_actor_name", 
        store="True", 
        help="A Person, Location, Healthcare Service or Device that is participating in the appointment.")                    
    actor_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Actor Patient", 
        help="Patient that is participating in the appointment.")                    
    actor_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Actor Practitioner", 
        help="Practitioner that is participating in the appointment.")                    
    actor_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Actor Related Person", 
        help="Related Person that is participating in the appointment.")                    
    actor_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Actor Device", 
        help="Device that is participating in the appointment.")                    
    actor_healthcare_service_id = fields.Many2one(
        comodel_name="hc.res.healthcare.service", 
        string="Actor Healthcare Service", 
        help="Healthcare Service that is participating in the appointment.")                    
    actor_location_id = fields.Many2one(
        comodel_name="hc.res.location", 
        string="Actor Location", 
        help="Location that is participating in the appointment.")                    
    participant_status = fields.Selection(
        string="Participant Status", 
        required="True", 
        selection=[
            ("accepted", "Accepted"), 
            ("declined", "Declined"), 
            ("tentative", "Tentative"), 
            ("in-process", "In-Process"), 
            ("completed", "Completed"), 
            ("needs-action", "Needs-Action")], 
        help="Participation status of the participant.")                    
    comment = fields.Text(
        string="Comment", 
        help="Additional comments about the appointment.")                    

    @api.depends('actor_type')          
    def _compute_actor_name(self):          
        for hc_res_appointment_response in self:        
            if hc_res_appointment_response.actor_type == 'patient': 
                hc_res_appointment_response.actor_name = hc_res_appointment_response.actor_patient_id.name
            elif hc_res_appointment_response.actor_type == 'practitioner':  
                hc_res_appointment_response.actor_name = hc_res_appointment_response.actor_practitioner_id.name
            elif hc_res_appointment_response.actor_type == 'related_person':    
                hc_res_appointment_response.actor_name = hc_res_appointment_response.actor_related_person_id.name
            elif hc_res_appointment_response.actor_type == 'device':    
                hc_res_appointment_response.actor_name = hc_res_appointment_response.actor_device_id.name
            elif hc_res_appointment_response.actor_type == 'healthcare_service':    
                hc_res_appointment_response.actor_name = hc_res_appointment_response.actor_healthcare_service_id.name
            elif hc_res_appointment_response.actor_type == 'location':  
                hc_res_appointment_response.actor_name = hc_res_appointment_response.actor_location_id.name

class AppointmentResponseIdentifier(models.Model):    
    _name = "hc.appointment.response.identifier"    
    _description = "Appointment Response Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

    appointment_response_id = fields.Many2one(
        comodel_name="hc.res.appointment.response", 
        string="Appointment Response", 
        help="Appointment Response associated with this Appointment Response Identifier.")                    
