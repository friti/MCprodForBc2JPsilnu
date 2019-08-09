from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'Samples2018_BJpsiX_MuMu'
config.General.workArea = 'crab_privateMC_miniAOD'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'Analysis'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName='miniAOD_crab_cfg.py'

config.JobType.numCores=1

#config.JobType.disableAutomaticOutputCollection = True 
#config.JobType.outputFiles = ['fileAOD.root','miniAOD.root']

config.Data.inputDataset=''
config.Data.inputDBS='phys03'

#config.Data.splitting = 'Automatic'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 30 #5
#config.Data.unitsPerJob = 1000 #500
#config.Data.totalUnits = 800000 #200000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
#config.Data.outputPrimaryDataset = 'BcJpsiMuNu_MiniAOD'
config.Data.outputDatasetTag ='Fall18_10_2_9-MINIAODSIM'
config.Data.lumiMask =""
config.Data.ignoreLocality = True
config.Site.whitelist=['T2_US_Nebraska', 'T2_FR_IPHC', 'T2_DE_RWTH','T2_CH_CSCS', 'T2_CH_CERN','T2_FR_GRIF_LLR']

config.Site.storageSite = 'T2_CH_CSCS'
