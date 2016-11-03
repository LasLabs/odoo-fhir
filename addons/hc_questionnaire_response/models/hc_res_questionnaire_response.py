# -*- coding: utf-8 -*-

from openerp import models, fields, api

class QuestionnaireResponse(models.Model):    
    _name = "hc.res.questionnaire.response"    
    _description = "Questionnaire Response"            

    identifier_id = fields.Many2one(
        comodel_name="hc.questionnaire.response.identifier", 
        string="Identifier", 
        help="Unique id for this set of answers.")                    
    based_on_ids = fields.One2many(
        comodel_name="hc.questionnaire.response.based.on", 
        inverse_name="questionnaire_response_id", 
        string="Based Ons", 
        help="Request fulfilled by this Questionnaire.")                    
    parent_ids = fields.One2many(
        comodel_name="hc.questionnaire.response.parent", 
        inverse_name="questionnaire_response_id", 
        string="Parents", 
        help="Part of this action.")                    
    questionnaire_id = fields.Many2one(
        comodel_name="hc.res.questionnaire", 
        string="Questionnaire", 
        help="Form being answered.")                    
    status = fields.Selection(
        string="Questionnaire Response Status", 
        required="True", 
        selection=[
            ("in-progress", "In-Progress"), 
            ("completed", "Completed"), 
            ("amended", "Amended")], 
        help="The lifecycle status of the questionnaire response as a whole.")                    
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="The subject of the questions.")                    
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="The subject of the questions.")                    
    subject_string = fields.Char(
        string="Subject String", 
        help="String of the subject of the questions.")                    
    subject_code_id = fields.Many2one(
        comodel_name="hc.vs.resource.type", 
        string="Subject Code", 
        help="Resource type of the subject of the questions.")                    
    context_type = fields.Selection(
        string="Context Type", 
        required="True", 
        selection=[
            ("Encounter", "Encounter"), 
            ("Episode Of Care", "Episode Of Care")], 
        help="Encounter or Episode during which questionnaire was completed.")                    
    context_name = fields.Char(
        string="Context", 
        compute="_compute_context_name", 
        store="True", 
        help="Encounter or Episode during which questionnaire was completed.")                    
    context_encounter_id = fields.Many2one(
        comodel_name="hc.res.encounter", 
        string="Context Encounter", 
        help="Encounter during which questionnaire was completed.")                    
    context_episode_of_care_id = fields.Many2one(
        comodel_name="hc.res.episode.of.care", 
        string="Context Episode Of Care", 
        help="Episode during which questionnaire was completed.")                    
    author_type = fields.Selection(
        string="Author Type", 
        required="True", 
        selection=[
            ("Device", "Device"), 
            ("Practitioner", "Practitioner"), 
            ("Patient", "Patient"), 
            ("Related Person", "Related Person")], 
        help="Type of person or device who received and recorded the answers.")                    
    author_name = fields.Char(
        string="Author", 
        compute="_compute_author_name", 
        store="True", 
        help="Person who received and recorded the answers.")                    
    author_device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Author Device", 
        help="Device who received and recorded the answers.")                    
    author_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Author Practitioner", 
        help="Practitioner who received and recorded the answers.")                    
    author_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Author Patient", 
        help="Patient who received and recorded the answers.")                    
    author_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Author Related Person", 
        help="Related Person who received and recorded the answers.")                    
    authored = fields.Datetime(
        string="Authored Date", 
        help="Date this version was authored.")                    
    source_type = fields.Selection(
        string="Source Type", 
        selection=[
            ("Patient", "Patient"), 
            ("Practitioner", "Practitioner"), 
            ("Related Person", "Related Person")], 
        help="Type of person who answered the questions.")                    
    source_name = fields.Char(
        string="Source", 
        compute="_compute_source_name", 
        store="True", 
        help="The person who answered the questions.")                    
    source_patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Source Patient", 
        help="Patient who answered the questions.")                    
    source_practitioner_id = fields.Many2one(
        comodel_name="hc.res.practitioner", 
        string="Source Practitioner", 
        help="Practitioner who answered the questions.")                    
    source_related_person_id = fields.Many2one(
        comodel_name="hc.res.related.person", 
        string="Source Related Person", 
        help="Related Person who answered the questions.")                    
    item_ids = fields.One2many(
        comodel_name="hc.questionnaire.response.item", 
        inverse_name="questionnaire_response_id", 
        string="Items", help="Groups and questions.")                    

class QuestionnaireResponseItem(models.Model):    
    _name = "hc.questionnaire.response.item"    
    _description = "Questionnaire Response Item"            

    questionnaire_response_id = fields.Many2one(
        comodel_name="hc.res.questionnaire.response", 
        string="Questionnaire Response", 
        help="Questionnaire Response associated with this Questionnaire Response Item.")                    
    link_id = fields.Char(
        string="Link Id", 
        help="Corresponding group within Questionnaire.")                    
    title = fields.Char(
        string="Title", 
        help="Name for group or question text.")                    
    subject_type = fields.Selection(
        string="Subject Type", 
        selection=[
            ("string", "String"), 
            ("code", "Code")], 
        help="The subject this group's answers are about.")
    subject_name = fields.Char(
        string="Subject", 
        compute="_compute_subject_name", 
        store="True", 
        help="The subject this group's answers are about.")
    subject_string = fields.Char(
        string="Subject String", 
        help="String of the subject this group's answers are about.")
    subject_code_id = fields.Many2one(comodel_name="hc.vs.resource.type", string="Subject Code", help="Resource type of the subject this group's answers are about.")                  
    item_id = fields.Many2one(
        comodel_name="hc.questionnaire.response.item", 
        string="Item", 
        help="Allows text, questions and other groups to be nested beneath a question or group.")                    
    answer_ids = fields.One2many(
        comodel_name="hc.questionnaire.response.item.answer", 
        inverse_name="item_id", 
        string="Answers", 
        help="The response(s) to the question.")                    
    answer_id = fields.Many2one(
        comodel_name="hc.questionnaire.response.item.answer", 
        string="Answer", 
        help="Answer associated with this Questionnaire Response Item.")                    

class QuestionnaireResponseItemAnswer(models.Model):    
    _name = "hc.questionnaire.response.item.answer"    
    _description = "Questionnaire Response Item Answer"            

    item_id = fields.Many2one(
        comodel_name="hc.questionnaire.response.item", 
        string="Item", 
        help="Item associated with this Questionnaire Response Item Answer.")                    
    value_type = fields.Selection(
        string="Value Type", 
        selection=[
            ("boolean", "Boolean"), 
            ("decimal", "Decimal"),
            ("integer", "Integer"),
            ("date", "Date"),
            ("dateTime", "Datetime"),
            ("instant", "Instant"),
            ("time", "Time"), 
            ("string", "String"),
            ("uri", "URL"),
            ("Attachment", "Attachment"),
            ("Coding", "Coding"),
            ("Quantity", "Quantity")], 
        help="Type of single-valued answer to the question.")                    
    value_name = fields.Char(
        string="Value", 
        compute="_compute_value_name", 
        store="True", 
        help="Single-valued answer to the question.")                    
    is_value = fields.Boolean(
        string="Value", 
        help="Boolean single-valued answer to the question.")                    
    value_decimal = fields.Float(
        string="Single Value Answer", 
        help="Decimal single-valued answer to the question.")                    
    value_integer = fields.Integer(
        string="Value Integer", 
        help="Integer single-valued answer to the question.")                    
    value_date = fields.Date(
        string="Value Date", 
        help="Date single-valued answer to the question.")                    
    value_datetime = fields.Datetime(
        string="Value Datetime", 
        help="Datetime single-valued answer to the question.")                    
    value_instant = fields.Datetime(
        string="Value Instant", 
        help="Instant single-valued answer to the question.")                    
    value_time = fields.Float(
        string="Value Time", 
        help="Time single-valued answer to the question.")                    
    value_string = fields.Char(
        string="Value", 
        help="String of single-valued answer to the question.")                    
    value_uri = fields.Char(
        string="Value URL", 
        help="URL of answer to the question")                    
    value_attachment_id = fields.Many2one(
        comodel_name="hc.questionnaire.response.item.answer.value.attachment", 
        string="Value Attachment", 
        help="Attachment single-valued answer to the question.")                    
    value_coding_id = fields.Many2one(
        comodel_name="hc.vs.answer.value", 
        string="Value Coding", 
        help="Coding of single-valued answer to the question.")                    
    value_quantity = fields.Float(
        string="Value Quantity", 
        help="Single-valued answer to the question.")                    
    value_quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Value Quantity UOM", 
        help="Value Quantity unit of measure.")                    
    item_ids = fields.One2many(
        comodel_name="hc.questionnaire.response.item", 
        inverse_name="answer_id", 
        string="Items", 
        help="Groups and questions.")                    

class QuestionnaireResponseIdentifier(models.Model):    
    _name = "hc.questionnaire.response.identifier"    
    _description = "Questionnaire Response Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]    

class QuestionnaireResponseBasedOn(models.Model):    
    _name = "hc.questionnaire.response.based.on"    
    _description = "Questionnaire Response Based On"        
    _inherit = ["hc.basic.association"]    

    questionnaire_response_id = fields.Many2one(
        comodel_name="hc.res.questionnaire.response", 
        string="Questionnaire Response", 
        help="Questionnaire Response associated with this Questionnaire Response Based On.")                    
    based_on_type = fields.Selection(
        string="Based On Type", 
        selection=[
            ("Diagnostic Request", "Diagnostic Request"), 
            ("Referral Request", "Referral Request"), 
            ("Care Plan", "Care Plan")], 
        help="Type of request fulfilled by this Questionnaire.")                    
    based_on_name = fields.Char(
        string="Based On", 
        compute="_compute_based_on_name", 
        store="True", 
        help="Request fulfilled by this Questionnaire.")                    
    based_on_diagnostic_request_id = fields.Many2one(
        comodel_name="hc.res.diagnostic.request", 
        string="Based On Diagnostic Request", 
        help="Diagnostic Request which was fulfilled by this questionnaire.")                    
    based_on_referral_request_id = fields.Many2one(
        comodel_name="hc.res.referral.request", 
        string="Based On Referral Request", 
        help="Referral Request which was fulfilled by this questionnaire.")                    
    based_on_care_plan_id = fields.Many2one(
        comodel_name="hc.res.care.plan", 
        string="Based On Care Plan", 
        help="Care Plan which was fulfilled by this questionnaire.")                    

class QuestionnaireResponseParent(models.Model):    
    _name = "hc.questionnaire.response.parent"    
    _description = "Questionnaire Response Parent"        
    _inherit = ["hc.basic.association"]    

    questionnaire_response_id = fields.Many2one(
        comodel_name="hc.res.questionnaire.response", 
        string="Questionnaire Response", 
        help="Questionnaire Response associated with this Questionnaire Response Parent.")                    
    parent_type = fields.Selection(
        string="Parent Type", 
        selection=[
            ("Observation", "Observation"), 
            ("Procedure", "Procedure")], 
        help="Type of part of this action.")                    
    parent_name = fields.Char(
        string="Parent", 
        compute="_compute_parent_name", 
        store="True", 
        help="Part of this action.")                    
    parent_observation_id = fields.Many2one(
        comodel_name="hc.res.observation", 
        string="Parent Observation", 
        help="Observation part of this action.")                    
    parent_procedure_id = fields.Many2one(
        comodel_name="hc.res.procedure", 
        string="Parent Procedure", 
        help="Procedure part of this action.")                    

class QuestionnaireResponseItemAnswerValueAttachment(models.Model):    
    _name = "hc.questionnaire.response.item.answer.value.attachment"    
    _description = "Questionnaire Response Item Answer Value Attachment"        
    _inherit = ["hc.basic.association", "hc.attachment"]    

class AnswerValue(models.Model):    
    _name = "hc.vs.answer.value"    
    _description = "Answer Value"        
    _inherit = ["hc.value.set.contains"]    
