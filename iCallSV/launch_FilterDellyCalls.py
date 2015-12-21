'''
Created on November 20, 2015
Description: This module will filter delly results and create filtered delly vcf files
@author: Ronak H Shah
'''
'''
::Inputs::
args: Arguments passed to iCallSV
config: configuration file passed to iCallSV
sampleOutdirForDelly: Output directory for delly vcf files.
del_vcf: Path to deletion based vcf file
dup_vcf: Path to duplication based vcf file
inv_vcf: Path to inversion based vcf file
tra_vcf: Path to translocation based vcf file
ins_vcf: Path to insertion based vcf file
'''
import logging
import FilterDellyCalls as fdc


def launch_filterdellycalls_for_different_analysis_type(args, config, sampleOutdirForDelly, del_vcf, dup_vcf, inv_vcf, tra_vcf):
    verbose = args.verbose
    
    # Run Delly for Deletion
    if(verbose):
        logging.info("launch_Run_Delly: Launched Delly for Deletion Events")

    filter_del_vcf = fdc.run(
        delly=config.get("SVcaller", "DELLY"),
        analysisType="DEL",
        reference=config.get("ReferenceFasta", "REFFASTA"),
        controlBam=args.controlBam,
        caseBam=args.caseBam,
        caseId=args.patientId,
        mapq=config.get("ParametersToRunDelly", "MAPQ"),
        excludeRegions=config.get("ExcludeRegion", "EXREGIONS"),
        outputdir=sampleOutdirForDelly,
        verbose=verbose,
        debug=False)

# Run Delly for duplication
    if(verbose):
        logging.info("launch_Run_Delly: Launched Delly for Duplication Events")

    dup_vcf = fdc.run(
        delly=config.get("SVcaller", "DELLY"),
        analysisType="DUP",
        reference=config.get("ReferenceFasta", "REFFASTA"),
        controlBam=args.controlBam,
        caseBam=args.caseBam,
        caseId=args.patientId,
        mapq=config.get("ParametersToRunDelly", "MAPQ"),
        excludeRegions=config.get("ExcludeRegion", "EXREGIONS"),
        outputdir=sampleOutdirForDelly,
        verbose=verbose,
        debug=False)

# Run Delly for inversion
    if(verbose):
        logging.info("launch_Run_Delly: Launched Delly for Inversion Events")

    inv_vcf = fdc.run(
        delly=config.get("SVcaller", "DELLY"),
        analysisType="INV",
        reference=config.get("ReferenceFasta", "REFFASTA"),
        controlBam=args.controlBam,
        caseBam=args.caseBam,
        caseId=args.patientId,
        mapq=config.get("ParametersToRunDelly", "MAPQ"),
        excludeRegions=config.get("ExcludeRegion", "EXREGIONS"),
        outputdir=sampleOutdirForDelly,
        verbose=verbose,
        debug=False)

# Run Delly for Translocation
    if(verbose):
        logging.info("launch_Run_Delly: Launched Delly for Translocation Envents")

    tra_vcf = fdc.run(
        delly=config.get("SVcaller", "DELLY"),
        analysisType="TRA",
        reference=config.get("ReferenceFasta", "REFFASTA"),
        controlBam=args.controlBam,
        caseBam=args.caseBam,
        caseId=args.patientId,
        mapq=config.get("ParametersToRunDelly", "MAPQ"),
        excludeRegions=config.get("ExcludeRegion", "EXREGIONS"),
        outputdir=sampleOutdirForDelly,
        verbose=verbose,
        debug=False)
'''
# Run Delly for Insertion
    if(verbose):
        logging.info("launch_Run_Delly: Launched Delly for Insertion Events")

    ins_vcf = fdc.run(
        delly=config.get("SVcaller", "DELLY"),
        analysisType="INS",
        reference=config.get("ReferenceFasta", "REFFASTA"),
        controlBam=args.controlBam,
        caseBam=args.caseBam,
        caseId=args.patientId,
        mapq=config.get("ParametersToRunDelly", "MAPQ"),
        excludeRegions=config.get("ExcludeRegion", "EXREGIONS"),
        outputdir=sampleOutdirForDelly,
        verbose=verbose,
        debug=False)
'''
    return(filter_del_vcf, filter_dup_vcf, filter_inv_vcf, filter_tra_vcf)