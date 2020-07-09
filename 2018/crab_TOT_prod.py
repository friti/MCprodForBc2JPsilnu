from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'miniAOD_JpsiX_MuMu_J_211119'
config.General.workArea = 'crab_privateMC'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName='miniAOD_crab_fake_cfg.py'

config.JobType.inputFiles = ['run_crab_TOT_prod.sh', 'BPH-JpsiX_MuMu_2018_cfg_Jordan.py','DR_step1_crab_cfg_ac.py','DR_step2_crab_cfg.py','pu.py','miniAOD_crab_fake_cfg.py','miniAOD_crab_cfg.py']
config.JobType.scriptExe='run_crab_TOT_prod.sh'
config.JobType.numCores=1

#config.JobType.disableAutomaticOutputCollection = True 
#config.JobType.outputFiles = ['fileAOD.root','miniAOD.root']

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob =    100000 #500
config.JobType.eventsPerLumi = 50000
config.Data.totalUnits = 1000000000 #200000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputPrimaryDataset = 'JpsiX_MuMu_J_211119'
config.Data.outputDatasetTag ='Autumn18_10_2_9_miniAOD'
config.Data.lumiMask =""
config.Data.ignoreLocality = True
config.Site.whitelist=['T2_US_Nebraska', 'T2_FR_IPHC', 'T2_DE_RWTH','T2_CH_CSCS', 'T2_CH_CERN','T2_FR_GRIF_LLR']


config.Site.storageSite = 'T2_CH_CSCS'
