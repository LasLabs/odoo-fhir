# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Appointment(models.Model):    
    _name = "hc.res.appointment"    
    _description = "Appointment"        

    identifier_ids = fields.One2many(
        comodel_name="hc.appointment.identifier", 
        inverse_name="appointment_id", 
        string="Identifiers", 
        help="External Ids for this item.")                
    status = fields.Selection(
        string="Appointment Status", 
        required="True", 
        selection=[
            ("proposed", "Proposed"), 
            ("pending", "Pending"), 
            ("booked", "Booked"), 
            ("arrived", "Arrived"), 
            ("fulfilled", "Fulfilled"), 
            ("cancelled", "Cancelled"), 
            ("noshow", "No Show")], 
        help="The overall status of the Appointment.")                
    service_category_id = fields.Many2one(
        comodel_name="hc.vs.service.category", 
        string="Appointment Service Category", 
        help="A broad categorisation of the service that is to be performed during this appointment.")              
    service_type_ids = fields.Many2many(
        comodel_name="hc.vs.service.type", 
        string="Service Types", 
        help="The specific service that is to be performed during this appointment.")                
    specialty_ids = fields.Many2many(
        comodel_name="hc.vs.c80.practice.code", 
        string="Specialties", 
        help="The specialty of a practitioner that would be required to perform the service requested in this appointment.")                
    appointment_type_id = fields.Many2one(
        comodel_name="hc.vs.v2.appointment.reason.code", 
        string="Appointment Type", 
        help="The style of appointment or patient that has been booked in the slot (not service type).")                
    reason_id = fields.Many2one(
        comodel_name="hc.vs.encounter.reason", 
        string="Reason", 
        help="The reason that this appointment is being scheduled, this is more clinical than administrative.")                
    indication_ids = fields.One2many(
        comodel_name="hc.appointment.indication", 
        inverse_name="appointment_id", 
        string="Indications", 
        help="Reason the appointment is to takes place (resource).")
    priority = fields.Integer(
        string="Priority", 
        help="The priority of the appointment. Can be used to make informed decisions if needing to re-prioritize appointments. (The iCal Standard specifies 0 as undefined, 1 as highest, 9 as lowest priority).")                
    description = fields.Text(
        string="Description", 
        help="The brief description of the appointment as would be shown on a subject line in a meeting request, or appointment list. Detailed or expanded information should be put in the comment field.")                
    supporting_information_ids = fields.One2many(
        comodel_name="hc.appointment.supporting.information", 
        inverse_name="appointment_id", 
        string="Supporting Information", 
        help="Additional information to support the appointment.")
    start = fields.Datetime(
        string="Start Date", 
        required="True", 
        help="Date/Time that the appointment is to take place.")                
    end = fields.Datetime(
        string="End Date", 
        required="True", 
        help="Date/Time that the appointment is to conclude.")
    minutes_duration = fields.Integer(
        string="Minutes Duration", 
        help="Can be less than start/end (e.g. estimate).")                             
    slot_ids = fields.One2many(
        comodel_name="hc.appointment.slot", 
        inverse_name="appointment_id", 
        string="Slots", 
        help="The slot that this appointment is filling. If provided then the schedule will not be provided as slots are not recursive, and the start/end values MUST be the same as from the slot.")                
    created = fields.Datetime(
        string="Appointment Creation Date", 
        help="The date that this appointment was initially created.")                
    comment = fields.Text(
        string="Comment", 
        help="Additional comments about the appointment.")                
    incoming_referral_ids = fields.One2many(
        comodel_name="hc.appointment.incoming.referral", 
        inverse_name="appointment_id", 
        string="Incoming Referrals", 
        help="The slot that this appointment is filling. If provided then the schedule will not be provided as slots are not recursive, and the start/end values MUST be the same as from the slot.")
    requested_period_ids = fields.One2many(
        comodel_name="hc.appointment.requested.period", 
        inverse_name="appointment_id", 
        string="Requested Periods", 
        help="The slot that this appointment is filling. If provided then the schedule will not be provided as slots are not recursive, and the start/end values MUST be the same as from the slot.")                               
    participant_ids = fields.One2many(
        comodel_name="hc.appointment.participant", 
        inverse_name="appointment_id", 
        string="Participants", 
        required="True", 
        help="List of participants involved in the appointment.")                

class AppointmentParticipant(models.Model):    
    _name = "hc.appointment.participant"    
    _description = "Appointment Participant"        
    
    appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Appointment", 
        help="Appointment associated with this Appointment Participant.")                
    type_ids = fields.Many2many(
        comodel_name="hc.vs.encounter.participant.type", 
        string="Types", 
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
    required = fields.Selection(
        string="Participant Required", 
        selection=[
            ("required", "Required"), 
            ("optional", "Optional"), 
            ("information-only", "Information Only")], 
        help="Is this participant required to be present at the meeting.")                
    status = fields.Selection(
        string="Participant Status", 
        required="True", 
        selection=[
            ("accepted", "Accepted"), 
            ("declined", "Declined"), 
            ("tentative", "Tentative"), 
            ("needs-action", "Needs Action")], 
        help="Participation status of the Patient.")                

class AppointmentIdentifier(models.Model):    
    _name = "hc.appointment.identifier"    
    _description = "Appointment Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Appointment", 
        help="Appointment associated with this Appointment Identifier.")                

class AppointmentIndication(models.Model):  
    _name = "hc.appointment.indication" 
    _description = "Appointment Indication"         
    _inherit = ["hc.basic.association"]

    appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Appointment", 
        help="Appointment associated with this Appointment Indication.")                  
    # indication_type = fields.Selection(
    #     string="Indication Type", 
    #     selection=[
    #         ("condition", "Condition"), 
    #         ("procedure", "Procedure")], 
    #     help="Type of reason the appointment is to takes place (resource).")                   
    # indication_name = fields.Char(
    #     string="Indication", 
    #     compute="_compute_indication_name", 
    #     store="True", 
    #     help="Reason the appointment is to takes place (resource).")                   
    # indication_condition_id = fields.Many2one(
    #     comodel_name="hc.res.condition", 
    #     string="Indication Condition", 
    #     help="Condition that is participating in the appointment.")                   
    # indication_procedure_id = fields.Many2one(
    #     comodel_name="hc.res.procedure", 
    #     string="Indication Procedure", 
    #     help="Procedure that is participating in the appointment.")                   

class AppointmentSupportingInformation(models.Model):   
    _name = "hc.appointment.supporting.information" 
    _description = "Appointment Supporting Information"         
    _inherit = ["hc.basic.association"]

    appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Appointment", 
        help="Appointment associated with this Appointment Supporting Information.")                  
    supporting_information_type = fields.Selection(
        string="Supporting Information Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="Type of additional information to support the appointment.")                   
    supporting_information_name = fields.Char(
        string="Supporting Information", 
        compute="_compute_supporting_information_name", 
        store="True", 
        help="Additional information to support the appointment.")                 
    supporting_information_string = fields.Char(
        string="Supporting Information String", 
        help="String of additional information to support the appointment.")                  
    supporting_information_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Supporting Information Code", 
        help="Resource type of additional information to support the appointment.")                    

class AppointmentSlot(models.Model):    
    _name = "hc.appointment.slot"    
    _description = "Appointment Slot"        
    _inherit = ["hc.basic.association"]

    appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Appointment", 
        help="Appointment associated with this Appointment Slot.")                
    slot_id = fields.Many2one(
        comodel_name="hc.res.slot", 
        string="Slot", 
        help="The slot that this appointment is filling. If provided then the schedule will not be provided as slots are not recursive, and the start/end values MUST be the same as from the slot")                

class AppointmentIncomingReferral(models.Model):    
    _name = "hc.appointment.incoming.referral"  
    _description = "Appointment Incoming Referral"          
    _inherit = ["hc.basic.association"]

    appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Appointment", 
        help="Appointment associated with this Appointment Incoming Referral.")                   
    # incoming_referral_id = fields.Many2one(
    #     comodel_name="hc.res.referral.request", 
    #     string="Incoming Referral", 
    #     help="The ReferralRequest provided as information to allocate to the Encounter")                 

class AppointmentRequestedPeriod(models.Model):    
    _name = "hc.appointment.requested.period"    
    _description = "Appointment Requested Period"        
    _inherit = ["hc.basic.association"]

    appointment_id = fields.Many2one(
        comodel_name="hc.res.appointment", 
        string="Appointment", 
        help="Appointment associated with this Appointment Requested Period.")                
    start_date = fields.Datetime(
        string="Start Date", 
        help="Start of the potential date/time interval(s) requested to allocate the appointment during.")                
    end_date = fields.Datetime(
        string="End Date", 
        help="End of the potential date/time interval(s) requested to allocate the appointment during.")                
