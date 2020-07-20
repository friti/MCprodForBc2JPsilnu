from CRABClient.UserUtilities import config, ClientException

import datetime

production_tag = datetime.date.today().strftime('%Y%b%d')

config = config()

config.General.requestName = 'hardQCD_BBarToJpsiAll'
config.General.workArea = 'hardQCD_%s' % production_tag
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'BTV-RunIISummer19UL18HLT-00025_1_cfg.py'

config.Data.inputDataset = name_dataset

config.JobType.inputFiles = ['run_crab_2.sh', 'BTV-RunIISummer19UL18HLT-00025_1_cfg.py']
config.JobType.scriptExe='run_crab_2.sh'
config.JobType.numCores=1


config.JobType.allowUndistributedCMSSW = True
config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer19UL18'

config.Data.outLFNDirBase ='/store/user/%s/%s/' %('friti','crab_job_'+production_tag)
config.Site.whitelist = ['T2_CH_CSCS']
config.Site.storageSite = 'T2_CH_CSCS'

