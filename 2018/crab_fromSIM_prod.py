from CRABClient.UserUtilities import config, ClientException

import datetime

production_tag = datetime.date.today().strftime('%Y%b%d')

config = config()

config.General.requestName = 'hardQCD_BBarToJpsiAll'
config.General.workArea = 'hardQCD_%s' % production_tag
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
#config.JobType.psetName = '../BBbarToJpsiSIM_cfg.py'

config.Data.inputDataset = '/BBbarToJpsiMu3Mu3PlusX_TuneCP5_13TeV-pythia8/friti-RunIISummer19UL18GEN-a8f71ab9fd4d4356d5029de29bb32fbd/USER'

config.JobType.inputFiles = ['run_crab_TOT_prod.sh', 'BTV-RunIISummer19UL18SIM-00025_1_cfg.py','BTV-RunIISummer19UL18DIGIPremix-00025_1_cfg.py','BTV-RunIISummer19UL18HLT-00025_1_cfg.py','BTV-RunIISummer19UL18RECO-00025_1_cfg.py','BTV-RunIISummer19UL18MiniAOD-00025_1_cfg.py']

config.Data.inputDBS = 'phys03'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.publication = True
config.Data.outputDatasetTag = 'RunIISummer19UL18SIM'

config.Data.outLFNDirBase ='/store/user/%s/%s/' %('friti','crab_job_'+production_tag)
config.Site.whitelist = ['T2_CH_CSCS']
config.Site.storageSite = 'T2_CH_CSCS'

from CRABAPI.RawCommand import crabCommand
from CRABClient.ClientExceptions import ClientException
from httplib import HTTPException
from multiprocessing import Process


def submit(config):
    try:
        crabCommand('submit', config = config)
    except HTTPException as hte:
        print "Failed submitting task: %s" % (hte.headers)
    except ClientException as cle:
        print "Failed submitting task: %s" % (cle)

print(config)
#submit(config)
