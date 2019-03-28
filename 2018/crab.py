from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'cgalloni_BcJpsiMuNu218'
config.General.workArea = 'crab_privateMCProduction'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
#config.JobType.disableAutomaticOutputCollection = True
config.JobType.maxMemoryMB = 2500
config.JobType.psetName = ['/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run01.lhe.xz', '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run02.lhe.xz', '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run03.lhe.xz', '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run04.lhe.xz','/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run05.lhe.xz', '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run06.lhe.xz',  '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run07.lhe.xz','/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run08.lhe.xz',  '/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run09.lhe.xz','/store/lhe/16237/bcvegpy_BcPt8Y2p5_MuNoCut_Evt200k_Run10.lhe.xz']
config.JobType.inputFiles = ['run_crab.sh', 'LHE_crab_cfg.py','GS_Fall18_BcJpsiMuNu_crab_cfg.py','DR_step1_crab_cfg.py','DR_step2_crab_cfg.py','miniAOD_crab_cfg.py']
config.JobType.scriptExe='ru_crab.sh'
#config.JobType.numCores=1

config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits = 200000
config.Data.outLFNDirBase = '/store/user/%s/' % (getUsernameFromSiteDB())
config.Data.publication = True
config.Data.outputPrimaryDataset = 'GluGlu_HToMuMu_M125_13TeV_amcatnloFXFX_pythia8'
config.Data.outputDatasetTag ='Fall17_94X-MINIAODSIM'

config.Site.storageSite = 'T2_CH_CSCS'
