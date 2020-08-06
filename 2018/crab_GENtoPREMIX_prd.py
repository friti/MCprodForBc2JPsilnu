from CRABClient.UserUtilities import config#, getUsernameFromSiteDB
import datetime
production_tag = datetime.date.today().strftime('%Y%b%d')

config = config()

config.General.requestName = 'HardQCD_BBbarToJpsiX_MuMu'
config.General.workArea = 'crab_privateMC_%s' % production_tag
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName = 'BTV-RunIISummer19UL18DIGIPremix_fake_-00025_1_cfg.py'
config.JobType.allowUndistributedCMSSW = True



config.JobType.inputFiles = ['run_crab_1.sh', 'BBbarToJpsiGEN_cfg.py','BTV-RunIISummer19UL18SIM-00025_1_cfg.py','BTV-RunIISummer19UL18DIGIPremix-00025_1_cfg.py','BTV-RunIISummer19UL18DIGIPremix_fake_-00025_1_cfg.py','puUL.py']

config.JobType.scriptExe='run_crab_1.sh'
config.JobType.numCores=1

#config.JobType.disableAutomaticOutputCollection = True 
#config.JobType.outputFiles = ['fileAOD.root','miniAOD.root']

config.JobType.maxJobRuntimeMin = 10000

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob =    1000000
config.JobType.eventsPerLumi = 1000
NJOBS = 10000
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase ='/store/user/%s/%s/' %('friti','crab_job_'+production_tag)
config.Data.publication = True
config.Data.outputPrimaryDataset = 'BBbarToJpsiMu3Mu3PlusX_TuneCP5_13TeV-pythia8-v3'
config.Data.outputDatasetTag = 'RunIISummer19UL18GEN'
config.Data.lumiMask =""
config.Data.ignoreLocality = True
config.Site.whitelist=['T2_CH_CSCS']


config.Site.storageSite = 'T2_CH_CSCS'
