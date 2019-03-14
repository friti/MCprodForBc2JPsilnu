# MCprodForBc2JPsilnu

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