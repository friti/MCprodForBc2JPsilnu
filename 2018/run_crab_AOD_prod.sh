#!/bin/bash
echo "================= CMSRUN starting jobNum=$1 ====================" | tee -a job.log





echo "================= CMSRUN cmsenv CMSSW_10_2_9 ===================="| tee -a job.log

#mkdir -p Configuration/GenProduction/python
#cp -v $BASE/LHE_crab_cfg.py Configuration/GenProduction/python/
#cp -v $BASE/GS_Fall18_BcJpsiMuNu_crab_cfg.py Configuration/GenProduction/python/


#scram b
#cd $BASE

#echo "================= CMSRUN starting LHE 1 ====================" | tee -a job.log

#cmsRun -j LHE_step1.log  LHE_crab_cfg.py jobNum=$1

#cd $BASE
echo "================= CMSRUN starting GS 2 ====================" | tee -a job.log

cmsRun -j GS_step2.log MUO-RunIIFall17GS-0001_2018_crab_cfg.py jobNum=$1 #
#cmsRun -j GS_step2.log JME-RunIIFall18GS-00009_crab_cfg.py jobNum=$1
echo "-> cleaning"
#rm -v lhe1.root  

echo "================= CMSRUN starting RECO 1 ====================" | tee -a job.log

cmsRun -j DR_step1.log  DR_step1_crab_cfg_ac.py 
echo "-> cleaning"
rm -v GS1.root 


echo "================= CMSRUN starting RECO 2 ====================" | tee -a job.log

cmsRun -e -j FrameworkJobReport.xml  DR_step2_crab_cfg.py 
echo "-> cleaning"
rm -v DR_step1.root

#echo "================= CMSRUN  miniAOD starts ===================="  | tee -a job.log

#cmsRun miniAOD_crab_cfg.py 

echo "================= CMSRUN  finished ===================="  | tee -a job.log
