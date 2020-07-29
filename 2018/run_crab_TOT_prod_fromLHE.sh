#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log





echo "================= CMSRUN cmsenv CMSSW_10_2_9 ===================="| tee -a job.log

cmsRun -j LHE_step1.log  LHE_crab_cfg.py jobNum=$1

echo "================= CMSRUN starting GS 2 ====================" | tee -a job.log
cmsRun -j GS_step2.log GS_Fall18_BcChic1TauNu_crab_cfg.py
#cmsRun -j GS_step2.log GS_Fall18_BcChic1MuNu_crab_cfg.py
#cmsRun -j GS_step2.log GS_Fall18_BcPsi2STauNu_crab_cfg.py  #
#cmsRun -j GS_step2.log GS_Fall18_BcPsi2SMuNu_crab_cfg.py

echo "-> cleaning"
#rm -v lhe1.root  

echo "================= CMSRUN starting RECO 1 ====================" | tee -a job.log

cmsRun -j DR_step1.log  DR_step1_crab_cfg_ac.py 
echo "-> cleaning"
rm -v GS1.root 


echo "================= CMSRUN starting RECO 2 ====================" | tee -a job.log

cmsRun -j  DR_step2.log  DR_step2_crab_cfg.py 
echo "-> cleaning"
rm -v DR_step1.root

echo "================= CMSRUN  miniAOD starts ===================="  | tee -a job.log

cmsRun -e -j FrameworkJobReport.xml  miniAOD_crab_cfg.py 
rm -v fileAOD.root

echo "================= CMSRUN  finished ===================="  | tee -a job.log
