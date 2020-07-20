
echo "================= CMSRUN starting RECO ====================" | tee -a job.log

cmsRun -j  DR_RECO.log  BTV-RunIISummer19UL18RECO-00025_1_cfg.py
#echo "-> cleaning"
#rm -v BTV-RunIISummer19UL18HLT-00025.root


echo "================= CMSRUN  min ===================="  | tee -a job.log

cmsRun -e -j FrameworkJobReport.xml BTV-RunIISummer19UL18MiniAOD-00025_1_cfg.py

#echo "-> cleaning"
#rm -v BTV-RunIISummer19UL18RECO-00025.root

echo "================= CMSRUN  finished ===================="  | tee -a job.log
