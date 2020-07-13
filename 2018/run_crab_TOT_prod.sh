#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log





echo "================= CMSRUN cmsenv CMSSW_10_2_9 ===================="| tee -a job.log


#echo "================= CMSRUN starting GS 2 ====================" | tee -a job.log

#cmsRun -j GS_step2.log BPH-JpsiX_MuMu_2018_cfg_Jordan.py jobNum=$1 #
#cmsRun -j GS_step2.log JME-RunIIFall18GS-00009_crab_cfg.py jobNum=$1
#echo "-> cleaning"
#rm -v lhe1.root  

echo "================= CMSRUN starting SIM ====================" | tee -a job.log

cmsRun -j DR_SIM.log  BTV-RunIISummer19UL18SIM-00025_1_cfg.py #DR_step1_crab_cfg_ac.py 
#echo "-> cleaning"
#rm -v GS1.root 


echo "================= CMSRUN starting PREMIX ====================" | tee -a job.log

cmsRun -j  DR_Premix.log  BTV-RunIISummer19UL18DIGIPremix-00025_1_cfg.py #DR_step2_crab_cfg.py 
#echo "-> cleaning"
#rm -v DR_step1.root

echo "================= CMSRUN starting HLT ====================" | tee -a job.log

cmsRun -j  DR_HLT.log  BTV-RunIISummer19UL18HLT-00025_1_cfg.py
#echo "-> cleaning"
#rm -v DR_step1.root

echo "================= CMSRUN starting RECO ====================" | tee -a job.log

cmsRun -j  DR_RECO.log  BTV-RunIISummer19UL18RECO-00025_1_cfg.py
#echo "-> cleaning"
#rm -v DR_step1.root


echo "================= CMSRUN  min ===================="  | tee -a job.log

cmsRun -e -j FrameworkJobReport.xml BTV-RunIISummer19UL18MiniAOD-00025_1_cfg.py
#rm -v fileAOD.root

echo "================= CMSRUN  finished ===================="  | tee -a job.log
