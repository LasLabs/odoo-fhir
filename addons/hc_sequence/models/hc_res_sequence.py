# -*- coding: utf-8 -*-

from openerp import models, fields, api

class Sequence(models.Model):    
    _name = "hc.res.sequence"    
    _description = "Sequence"        

    identifier_ids = fields.One2many(
        comodel_name="hc.sequence.identifier", 
        inverse_name="sequence_id", 
        string="Identifiers", 
        help="Unique ID for this particular sequence.")                
    type = fields.Selection(
        string="Type", 
        required="True", 
        selection=[
            ("aa", "AA"), 
            ("dna", "DNA"), 
            ("rna", "RNA")], 
        help="Type of a sequence.")                
    coordinate_system = fields.Integer(
        string="Coordinate System", 
        required="True", 
        help="Numbering used for sequence (0-based or 1-based).")                
    patient_id = fields.Many2one(
        comodel_name="hc.res.patient", 
        string="Patient", 
        help="Who and/or what this is about.")                
    specimen_id = fields.Many2one(
        comodel_name="hc.res.specimen", 
        string="Specimen", 
        help="Specimen used for sequencing.")                
    device_id = fields.Many2one(
        comodel_name="hc.res.device", 
        string="Device", 
        help="The method for sequencing.")                
    quantity = fields.Float(
        string="Quantity", 
        help="Quantity of the sequence.")                
    quantity_uom_id = fields.Many2one(
        comodel_name="product.uom", 
        string="Quantity UOM", 
        help="Quantity unit of measure.")                
    observed_seq = fields.Char(
        string="Observed Sequence", 
        help="Observed sequence.")                
    read_coverage = fields.Integer(
        string="Read Coverage", 
        help="Average number of reads representing a given nucleotide in the reconstructed sequence.")                
    pointer_ids = fields.One2many(
        comodel_name="hc.sequence.pointer", 
        inverse_name="sequence_id", 
        string="Pointers", 
        help="Pointer to next atomic sequence.")                
    reference_seq_ids = fields.One2many(
        comodel_name="hc.sequence.reference.seq", 
        inverse_name="sequence_id", 
        string="Reference Sequences", 
        help="A sequence that is used to represent an allele or variant.")                
    variant_ids = fields.One2many(
        comodel_name="hc.sequence.variant", 
        inverse_name="sequence_id", 
        string="Variants", 
        help="Variant info in this sequence.")                
    quality_ids = fields.One2many(
        comodel_name="hc.sequence.quality", 
        inverse_name="sequence_id", 
        string="Quality", 
        help="Sequence Quality.")                
    repository_ids = fields.One2many(
        comodel_name="hc.sequence.repository", 
        inverse_name="sequence_id", 
        string="Repositories", 
        help="External repository.")                
    structure_variant_ids = fields.One2many(
        comodel_name="hc.sequence.structure.variant", 
        inverse_name="sequence_id", 
        string="Structure Variants", 
        help="Structural variant.")                

class SequenceReferenceSeq(models.Model):    
    _name = "hc.sequence.reference.seq"    
    _description = "Sequence Reference Sequence"        

    sequence_id = fields.Many2one(
        comodel_name="hc.res.sequence", 
        string="Sequence", 
        help="Sequence associated with this reference seq.")                
    chromosome_id = fields.Many2one(
        comodel_name="hc.vs.chromosome.human", 
        string="Chromosome", 
        help="The chromosome containing the genetic finding.")                
    genome_build = fields.Char(
        string="Genome Build", 
        help='The Genome Build used for reference, following GRCh build versions e.g. "GRCh 37".')                
    reference_seq_id = fields.Many2one(
        comodel_name="hc.vs.sequence.reference.seq", 
        string="Reference Sequence ID", 
        required="True", 
        help="Reference identifier.")                
    reference_seq_pointer_id = fields.Many2one(
        comodel_name="hc.res.sequence", 
        string="Reference Sequence Pointer", 
        help="A Pointer to another Sequence entity as refence sequence.")                
    reference_seq_string = fields.Char(
        string="Reference Seq String", 
        help="A Reference Sequence string.")                
    strand = fields.Integer(
        string="Strand", 
        required="True", 
        help='Strand of DNA. Available values are "1" for the plus strand and "-1" for the minus strand.')                
    window_start = fields.Integer(
        string="Window Start", 
        required="True", 
        help="Start position (inclusive) of the window on the reference sequence.")                
    window_end = fields.Integer(
        string="Window End", 
        required="True", 
        help="End position (exclusive) of the window on the reference sequence.")                

class SequenceVariant(models.Model):    
    _name = "hc.sequence.variant"   
    _description = "Sequence Variant"        

    sequence_id = fields.Many2one(
        comodel_name="hc.res.sequence", 
        string="Sequence", 
        help="Sequence associated with this variant.")                
    start = fields.Integer(
        string="Start", 
        help="Start position (inclusive) of the variant on the reference sequence.")                
    end = fields.Integer(
        string="End", 
        help="End position (exclusive) of the variant on the reference sequence.")                
    observed_allele = fields.Char(
        string="Observed Allele", 
        help="Nucleotide(s)/amino acids from start position to stop position of observed variant.")                
    reference_allele = fields.Char(
        string="Reference Allele", 
        help="Nucleotide(s)/amino acids from start position to stop position of reference variant.")                
    cigar = fields.Char(
        string="Cigar", 
        help="Extended CIGAR string for aligning the sequence with reference bases.")                
    # variant_pointer_id = fields.Many2one(
    #     comodel_name="hc.res.observation", 
    #     string="Variant Pointer", 
    #     help="A pointer to an Observation containing variant information.")                

class SequenceQuality(models.Model):    
    _name = "hc.sequence.quality"    
    _description = "Sequence Quality"        

    sequence_id = fields.Many2one(
        comodel_name="hc.res.sequence", 
        string="Sequence", 
        help="Sequence associated with this quality.")                
    standard_sequence_id = fields.Many2one(
        comodel_name="hc.vs.sequence.standard.sequence", 
        string="Standard Sequence", 
        help="Standard sequence for comparison.")                
    start = fields.Integer(
        string="Start", 
        help="Start position (inclusive) of the sequence.")                
    end = fields.Integer(
        string="End", 
        help="End position (exclusive) of the sequence.")                
    score = fields.Float(
        string="Score", 
        help="Quality score.")                
    method_id = fields.Many2one(
        comodel_name="hc.vs.sequence.quality.method", 
        string="Method", help="Method for quality.")                
    true_positives = fields.Float(
        string="True Positives", 
        help="True positives from the perspective of the truth data.")                
    query_tp = fields.Float(
        string="Query TP", 
        help="True positives from the perspective of the query data.")                
    truth_fn = fields.Float(
        string="Truth FN", 
        help="False negatives.")
    query_fp = fields.Float(
        string="Query FP", 
        help="False positives.")
    gt_fp = fields.Float(
        string="Gt FP", 
        help="False positives where the non-REF alleles in the Truth and Query Call Sets match.")                
    precision = fields.Float(
        string="Precision", 
        help="Precision (PPV); QUERY.TP / (QUERY.TP + QUERY.FP).")
    recall = fields.Float(
        string="Recall", 
        help="Recall (sensitivity); TRUTH.TP / (TRUTH.TP + TRUTH.FN).")             
    f_measure = fields.Float(
        string="f Measure", 
        help="F-score.")                

class SequenceRepository(models.Model):    
    _name = "hc.sequence.repository"    
    _description = "Sequence Repository"        

    sequence_id = fields.Many2one(
        comodel_name="hc.res.sequence", 
        string="Sequence", 
        help="Sequence associated with this repository.")                
    url = fields.Char(
        string="URI", 
        help="URI of the repository.")                
    name = fields.Char(
        string="Name", 
        help="Name of the repository.")                
    variant_id = fields.Char(
        string="Variant ID", 
        help="ID of the variant in this external repository.")
    read_id = fields.Char(
        string="Read ID", 
        help="ID of the read in this external repository.")

class SequenceStructureVariant(models.Model):    
    _name = "hc.sequence.structure.variant"    
    _description = "Sequence Structure Variant"        

    sequence_id = fields.Many2one(
        comodel_name="hc.res.sequence", 
        string="Sequence", 
        help="Sequence associated with this structure variant.")                
    precision_of_boundaries = fields.Char(
        string="Precision Of Boundaries", 
        help="Precision of boundaries.")                
    reported_acgh_ratio = fields.Float(
        string="Reported ACGH Ratio", 
        help="Structural Variant reported aCGH ratio.")                
    length = fields.Integer(
        string="Length", 
        help="Structural Variant Length.")                
    outer_ids = fields.One2many(
        comodel_name="hc.sequence.structure.variant.outer", 
        inverse_name="structure_variant_id", 
        string="Outers", 
        help="Structural variant outer.")                
    inner_ids = fields.One2many(
        comodel_name="hc.sequence.structure.variant.inner", 
        inverse_name="structure_variant_id", 
        string="Inners", 
        help="Structural variant inner.")                

class SequenceStructureOuter(models.Model):    
    _name = "hc.sequence.structure.variant.outer"    
    _description = "Sequence Structure Variant Outer"        

    structure_variant_id = fields.Many2one(
        comodel_name="hc.sequence.structure.variant", 
        string="Structure Variant", 
        help="Structure Variant associated with this outer.")                
    start = fields.Integer(
        string="Start", 
        help="Structural Variant Outer Start-End.")                
    end = fields.Integer(
        string="End", 
        help="Structural Variant Outer Start-End.")                

class SequenceStructureInner(models.Model):    
    _name = "hc.sequence.structure.variant.inner"    
    _description = "Sequence Structure Variant Inner"        

    structure_variant_id = fields.Many2one(
        comodel_name="hc.sequence.structure.variant", 
        string="Structure Variant", 
        help="Structure Variant associated with this inner.")                
    start = fields.Integer(
        string="Start", 
        help="Structural Variant Inner Start-End.")                
    end = fields.Integer(
        string="End", 
        help="Structural Variant Inner Start-End.")                

class SequenceIdentifier(models.Model):    
    _name = "hc.sequence.identifier"    
    _description = "Sequence Identifier"        
    _inherit = ["hc.basic.association", "hc.identifier"]

    sequence_id = fields.Many2one(
        comodel_name="hc.res.sequence", 
        string="Sequence", 
        help="Sequence associated with this sequence identifier.")                

class SequencePointer(models.Model):    
    _name = "hc.sequence.pointer"    
    _description = "Sequence Pointer"        
    _inherit = ["hc.basic.association"]

    sequence_id = fields.Many2one(
        comodel_name="hc.res.sequence", 
        string="Sequence", 
        help="Sequence associated with this sequence pointer.")                
    pointer_id = fields.Many2one(
        comodel_name="hc.res.sequence", 
        string="Pointer", 
        help="Pointer associated with this sequence pointer.")                

class ChormosomeHuman(models.Model):    
    _name = "hc.vs.chromosome.human"    
    _description = "Chromosome Human"        
    _inherit = ["hc.value.set.contains"]

class SequenceReferenceSeq(models.Model):    
    _name = "hc.vs.sequence.reference.seq"    
    _description = "Sequence Reference Seq"        
    _inherit = ["hc.value.set.contains"]

class SequenceStandardSequence(models.Model):    
    _name = "hc.vs.sequence.standard.sequence"    
    _description = "Sequence Standard Sequence"        
    _inherit = ["hc.value.set.contains"]

class SequenceQualityMethod(models.Model):    
    _name = "hc.vs.sequence.quality.method"    
    _description = "Sequence Quality Method"        
    _inherit = ["hc.value.set.contains"]
