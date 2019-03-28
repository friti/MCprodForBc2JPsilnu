# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --filein lhe:16237 --fileout file:BPH-RunIIFall18pLHE-00001.root --mc --eventcontent LHE --datatier LHE --conditions 102X_upgrade2018_realistic_v11 --step NONE --python_filename BPH-RunIIFall18pLHE_Bc_cfg.py --no_exec --customise Configuration/DataProcessing/Utils.addMonitoring -n 10000
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('LHE')

# import of standard configurations
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("LHESource",
#    skipEvents=cms.untracked.uint32(40),
    fileNames = cms.untracked.vstring(
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run01.lhe.xz', 
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run02.lhe.xz', 
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run03.lhe.xz', 
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run04.lhe.xz', 
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run05.lhe.xz', 
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run06.lhe.xz', 
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run07.lhe.xz', 
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run08.lhe.xz', 
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run09.lhe.xz', 
        '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run10.lhe.xz'
    ), 
   
)

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:10'), #CG 10000
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.LHEoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('LHE'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:lhe1.root'),
    outputCommands = process.LHEEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '102X_upgrade2018_realistic_v11', '')

# Path and EndPath definitions
process.LHEoutput_step = cms.EndPath(process.LHEoutput)

# Schedule definition
process.schedule = cms.Schedule(process.LHEoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
