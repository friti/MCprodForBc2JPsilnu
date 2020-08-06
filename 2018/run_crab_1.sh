#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log





echo "================= CMSRUN cmsenv CMSSW_10_6_5 ! ===================="| tee -a job.log


echo "================= CMSRUN starting GEN ====================" | tee -a job.log

cmsRun -j GEN_step.log BBbarToJpsiGEN_cfg.py jobNum=$1 
#cmsRun -j GS_step2.log JME-RunIIFall18GS-00009_crab_cfg.py jobNum=$1
#echo "-> cleaning"
#rm -v BTV-RunIISummer19UL18SIM-00025.root  

echo "================= CMSRUN starting SIM ====================" | tee -a job.log

cmsRun -j DR_SIM.log  BTV-RunIISummer19UL18SIM-00025_1_cfg.py #DR_step1_crab_cfg_ac.py 
#echo "-> cleaning"



echo "================= CMSRUN starting PREMIX ====================" | tee -a job.log

#cmsRun -j  DR_Premix.log  BTV-RunIISummer19UL18DIGIPremix-00025_1_cfg.py #DR_step2_crab_cfg.py 
cmsRun -e -j FrameworkJobReport.xml  BTV-RunIISummer19UL18DIGIPremix-00025_1_cfg.py

echo "-> cleaning"
#rm -v BTV-RunIISummer19UL18SIM-00025.root  


