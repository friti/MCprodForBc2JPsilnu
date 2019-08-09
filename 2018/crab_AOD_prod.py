from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'AOD_BJpsiX_MuMu_090819'
config.General.workArea = 'crab_privateMC'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
#config.JobType.maxMemoryMB = 2500
config.JobType.psetName='DR_step2_crab_fake_cfg.py'

config.JobType.inputFiles = ['run_crab_AOD_prod.sh', 'BPH-BJpsiX_MuMu_2018_cfg.py','DR_step1_crab_cfg_ac.py','DR_step2_crab_fake_cfg.py','DR_step2_crab_cfg.py','pu.py']
config.JobType.scriptExe='run_crab_AOD_prod.sh'
config.JobType.numCores=1

#config.JobType.disableAutomaticOutputCollection = True 
#config.JobType.outputFiles = ['fileAOD.root','miniAOD.root']

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob =    500000 #500
config.JobType.eventsPerLumi = 5000
config.Data.totalUnits = 10000000 #200000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputPrimaryDataset = 'BJpsiX_MuMu_090819'
config.Data.outputDatasetTag ='Autumn18_10_2_9_AOD'
config.Data.lumiMask =""

config.Site.storageSite = 'T2_CH_CSCS'
