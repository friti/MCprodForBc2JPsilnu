#!/bin/bash

echo "================= CMSRUN starting HLT ====================" | tee -a job.log

cmsRun -j  DR_HLT.log  BTV-RunIISummer19UL18HLT-00025_1_cfg.py
#echo "-> cleaning"
#rm -v BTV-RunIISummer19UL18DIGIPremix-00025.root

