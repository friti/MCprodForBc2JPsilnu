GEN to PREMIX production

```
cmsrel CMSSW_10_6_5
cd CMSSW_10_6_5/src
cmsenv
source /cvmfs/cms.cern.ch/crab3/crab.sh
git cms-addpkg GeneratorInterface/GenFilters
git clone git@github.com:friti/MCprodForBc2JPsilnu  

#add the fragment in the right position
mv MCprodForBc2JPsilnu/2018/Configuration/ .

#modify the ancestors scripts
mv MCprodForBc2JPsilnu/2018/PythiaFilterMultiMother.cc GeneratorInterface/GenFilters/src/.
mv MCprodForBc2JPsilnu/2018/PythiaFilterMultiMother.h GeneratorInterface/GenFilters/interface/.

#send on CRAB from GEN to PREMIX
cd MCprodForBc2JPsilnu/2018/
crab submit crab_GENtoPREMIX_prd.py
```

HLT production needs the CMSSW_10_2_16_UL environment                  
RECO e MiniAOD CMSSW_10_6_5 environment           
