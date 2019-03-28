#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log

source /cvmfs/cms.cern.ch/cmsset_default.sh
export SCRAM_ARCH=slc6_amd64_gcc630

BASE=$PWD


echo "================= CMSRUN setting up CMSSW_10_2_9 ===================="| tee -a job.log
if [ -r CMSSW_10_2_9/src ] ; then 
     echo release CMSSW_10_2_9 already exists
 else
     scram p CMSSW CMSSW_10_2_9
 fi


cd CMSSW_10_2_9/src
eval `scram runtime -sh`


scram b
cd $BASE

echo "================= CMSRUN starting LHE 1 ====================" | tee -a job.log

cmsRun -j LHE_step1.log  LHE_crab_cfg.py

cd $BASE
echo "================= CMSRUN starting GS 2 ====================" | tee -a job.log

cmsRun -j GS_step2.log GS_Fall18_BcJpsiMuNu_crab_cfg.py
echo "-> cleaning"
rm -v lhe1.root  

echo "================= CMSRUN starting RECO 1 ====================" | tee -a job.log

cmsRun -j DR_step1.log  DR_step1_crab_cfg.py 
echo "-> cleaning"
rm -v GS1.root 


echo "================= CMSRUN starting RECO 2 ====================" | tee -a job.log

cmsRun -e -j  DR_step2.log  DR_step2_crab_cfg.py 
echo "-> cleaning"
rm -v DR_step1.root

echo "================= CMSRUN  miniAOD starts ===================="  | tee -a job.log

cmsRun miniAOD_crab_cfg.py 

echo "================= CMSRUN  finished ===================="  | tee -a job.log
