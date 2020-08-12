import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(True),
    comEnergy = cms.double(13000.0),

    PythiaParameters = cms.PSet(
            pythia8CommonSettingsBlock,
            pythia8CP5SettingsBlock,
            processParameters = cms.vstring(
                    'ParticleDecays:limitTau0 = off',
                    'HardQCD:hardbbbar = on',
                    'PhaseSpace:pTHatMin = 10',
            ),
            parameterSets = cms.vstring('pythia8CommonSettings',
                                        'pythia8CP5Settings',
                                        'processParameters',
                                        )
    )
)

# B hadron pdgIDs
b_hadrons_pdgids = [
    # b-mesons
    511,
    521,
    513,
    523,
    515,
    525,
    531,
    533,
    535,
    541,
    543,
    545,

    # bbbar-mesons
    551,
    553,
    557,
    555,

    # baryons
    5122,
    5212,
    5222,
    5232,
    5312,
    5132,
    5342,
    5434,
    5442,
    5444,
    5512,
    5112,
    5114,
    5214,
    5142,
    5242,
    5412,
    5422,
    5414,
    5424,
    5432,
    5524,
    5532,
    5534,
    5542,
    5544,
    5324,
    5322,
    5522,
    5514,
    5224,
    5554,
    5334,
    5314,
    5332,
]

jpsi_from_b_hadron_filter = cms.EDFilter(
    "PythiaFilterMultiMother",
    ParticleID      = cms.untracked.int32 (443),
    MinPt           = cms.untracked.double( 6.),
    MinEta          = cms.untracked.double(-3.),
    MaxEta          = cms.untracked.double( 3.),
    MotherIDs       = cms.untracked.vint32([5]), 
    DaughterIDs     = cms.untracked.vint32([-13, 13]), 
    DaughterMinPts  = cms.untracked.vdouble([3., 3.]), 
    DaughterMaxPts  = cms.untracked.vdouble([100000., 100000.]), 
    DaughterMinEtas = cms.untracked.vdouble([-2.6, -2.6]), 
    DaughterMaxEtas = cms.untracked.vdouble([2.6, 2.6]), 
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('\$Revision$'),
    name = cms.untracked.string('\$Source$'),
    annotation = cms.untracked.string(
        'QCD bbbar production, '\
        'pThat>=10 GeV, '\
        'Jpsi (pt>6, |eta|<3) from b hadron (meson or baryon), '\
        'Jpsi->mumu, mu pt>3 & |eta|<2.6, '\
        '13 TeV, '\
        'TuneCP5'
    )
)

ProductionFilterSequence = cms.Sequence(generator*jpsi_from_b_hadron_filter)
