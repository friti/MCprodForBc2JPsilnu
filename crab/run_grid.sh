echo "================= YT: input arguments =================="
echo $@

echo "================= YT: PSet.py file =================="
cat PSet.py

echo "================= YT: list files =================="
ls -alrt 


for i in "$@"
do
    case $i in
	sample=*)
	SAMPLE="${i#*=}"
	;;
	index=*)
	INDEX="${i#*=}"
	;;
	input=*)
	INPUT="${i#*=}"
	;;
	nmax=*)
	NMAX="${i#*=}"
	;;
	seed=*)
	SEED="${i#*=}"
	;;
    esac
done


echo "--------------------------"
echo "sample name = $SAMPLE"
echo "index = $INDEX"
echo "input file = $INPUT"
echo "max events = $NMAX"
echo "skip events = $SEED"
echo "--------------------------"


echo "================= YT: start processing =================="
if [ -r CMSSW_7_1_37 ] ; then
    echo "release CMSSW_7_1_37 already exists"
else
    scram p CMSSW CMSSW_7_1_37
    echo "seting up CMSSW_7_1_37"
fi

cd CMSSW_7_1_37/src
eval `scram runtime -sh` 
cd -

echo 'cms release = ', $CMSSW_BASE



echo "================= [LOG] GS step1 starts ===================="
cmsRun GS_step1_template.py $SAMPLE $INDEX $INPUT $NMAX $SEED
echo "================= [LOG] GS step1 ends ===================="

if [ -r CMSSW_8_0_21/src ] ; then
    echo "release CMSSW_8_0_21 already exists"
else
    scram p CMSSW CMSSW_8_0_21
fi

cd CMSSW_8_0_21/src
eval `scram runtime -sh`
cd -

echo 'cms release = ', $CMSSW_BASE

echo "================= [LOG] DR step1 starts ===================="
cmsRun DR_step1_template.py $SAMPLE $INDEX
echo "================= [LOG] DR step1 ends ===================="

echo "removing GS sample ..."
rm GS_${SAMPLE}_${INDEX}.root

echo "================= [LOG] DR step2 starts ===================="
cmsRun DR_step2_template.py $SAMPLE $INDEX
echo "================= [LOG] DR step2 ends ===================="

echo "removing DR step1 sample ..."
rm DR_step1_${SAMPLE}_${INDEX}.root


if [ -r CMSSW_9_4_9/src ] ; then
    echo "release CMSSW_8_0_21 already exists"
else
    scram p CMSSW CMSSW_9_4_9
fi

cd CMSSW_9_4_9/src
eval `scram runtime -sh`
cd -

echo 'cms release = ', $CMSSW_BASE


echo "================= [LOG] miniAOD starts ===================="
cmsRun miniAOD_template.py $SAMPLE $INDEX
echo "================= [LOG] miniAOD ends ===================="

echo "removing DR step2 sample ..."
rm DR_step2_${SAMPLE}_${INDEX}.root


if [ -r CMSSW_10_2_9/src ] ; then
    echo "release CMSSW_8_0_21 already exists"
else
    scram p CMSSW CMSSW_10_2_9
fi

cd CMSSW_10_2_9/src
eval `scram runtime -sh`
cd -

echo 'cms release = ', $CMSSW_BASE

echo "================= [LOG] nanoAOD starts ===================="
cmsRun nanoAOD_template.py $SAMPLE $INDEX
echo "================= [LOG] nanoAOD ends ===================="

echo "removing DR step2 sample ..."
rm miniAOD_${SAMPLE}_${INDEX}.root


cmsRun -j FrameworkJobReport.xml -p PSet.py
