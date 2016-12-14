# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Annotation(models.AbstractModel):
    _name = "hc.annotation"
    _description = "Annotation"
 
    # name = fields.Char(
    # 	string="Name",
    #     required="True",
    # 	help="The name of the annotation.")
    text = fields.Text(
        string="Text", 
        required="True", 
        help="The annotation - text content.")
    recorded_date = fields.Datetime(
        string="Recorded Date", 
        help="When the annotation was made.")
    author_type = fields.Selection(
        string="Author Type", 
        selection=[
            ("string", "String"),
            ("practitioner", "Practitioner"),
            ("patient", "Patient"),
            ("related_person", "Related Person")],
        help="Type of individual responsible for the annotation.")
    author_string = fields.Char(
        string="Author String",
        help="Individual responsible for the annotation.")

    # author_practitioner_id = fields.Many2one(comodel_name="hc.res.practitioner", string="Author Practitioner", help="Practitioner responsible for the annotation.")
    # author_patient_id = fields.Many2one(comodel_name="hc.res.patient", string="Author Patient", help="Patient responsible for the annotation.")
    # author_related_person_id = fields.Many2one(comodel_name="hc.res.related.person", string="Author Related Person", help="Related person responsible for the annotation.")

    # @api.multi
    # def _compute_author_name(self):
    #     for hc_annotation in self:
    #         if hc_annotation.author_type == 'string':
    #             hc_annotation.author_name = hc_annotation.author_string

    # @api.multi
    # def _compute_author_name(self):
    #     for hc_annotation in self:
    #         if hc_annotation.author_type == 'string':
    #             hc_annotation.author_name = hc_annotation.author_string
    #         elif hc_annotation.author_type == 'Practitioner':
    #             hc_annotation.author_name = hc_annotation.author_practitioner_id.name
    #         elif hc_annotation.author_type == 'Patient':
    #             hc_annotation.author_name = hc_annotation.author_patient_id.name
    #         elif hc_annotation.author_type == 'Related Person':
    #             hc_annotation.author_name = hc_annotation.author_related_person_id.name


    # @api.multi
    # def _compute_author_name(self):
    #     for hc_annot in self:
    #         if hc_annot.author_type == 'practitioner':
    #             hc_annot.author_name = hc_annot.author_practitioner_id.name
    #         elif hc_annot.author_type == 'patient':
    #             hc_annot.author_name = hc_annot.author_patient_id.name
    #         elif hc_annot.author_type == 'related person':
    #             hc_annot.author_name = hc_annot.author_related_person_id.name