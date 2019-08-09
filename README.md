# MCprodForBc2JPsilnu

### To run the production for 2018 using CRAB
```
cmsrel CMSSW_10_2_9 
cd CMSSW_10_2_9/src
cmsenv


git clone git@github.com:cgalloni/MCprodForBc2JPsilnu.git
scram b -j 8
```

To run the AOD production, modify the settings in `crab_AOD_prod.py` to your needs for the number of events and storage on the T2 where you have writing rights. 
 
```
cd $CMSSW_BASE/src/MCprodForBc2JPsilnu/2018/
crab submit crab_AOD_prod.py 
```
at this point a CRAB_PROJ_DIR  should be created.

check the status submission with :
`crab status CRAB_PROJ_DIR`
and resubmit :
`crab resubmit CRAB_PROJ_DIR`

The `crab status` also lists the output_dataset_name, which needs to be written in  `config.Data.inputDataset='output_dataset_name'`  in c`rab_miniAOD_prod.py`. Modify also the settings for your needs for the number of events and storage on the T2 where you have writing rights. 
To run the miniAOD production:

```
crab submit crab_AOD_prod.py 
```
again it is possible to use the `crab status` and `crab submit`.






### To run the production on the Batch

Please see "run_local.sh" in each year of the production,
to see the sequence and configuration of the production. 

Note that, this script starts from the gridpack (rather than LHE) 
and then produce up to nanoAOD. 
So there are several changes needed. 
(But basic configuration settings are there)

Just for the record: the argument of the run_local.sh is, 

> sh run_local.sh [sample_name] [index] [input_gridpack] [# of events to be produced] [random seed]


I also created the directory crab, to take care of the grid submission, 
but this should be also changed. 