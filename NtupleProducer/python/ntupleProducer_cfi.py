import FWCore.ParameterSet.Config as cms

InfoOut = cms.EDProducer('NtupleProducer',
         L1TrackTag  = cms.InputTag('l1tPFTkProducersFromOfflineTracksStrips'),
         EcalTPTag   = cms.InputTag('l1tPFEcalProducerFromOfflineRechits','towers'),
         HGEcalTPTag = cms.InputTag('l1tPFHGCalEEProducerFromOfflineRechits','towers'),
         HcalTPTag   = cms.InputTag('l1tPFHcalProducerFromOfflineRechits','towers'),
         HGHcalTPTag = cms.InputTag('l1tPFHGCalFHProducerFromOfflineRechits','towers'),
         BHHcalTPTag = cms.InputTag('l1tPFHGCalBHProducerFromOfflineRechits','towers'),
         HFTPTag     = cms.InputTag('l1tPFHFProducerFromOfflineRechits','towers'),
         MuonTPTag   = cms.InputTag('gmtStage2Digis','Muon'), 
         genParTag   = cms.InputTag('genParticles'),
         zeroSuppress = cms.bool(False),
         corrector   = cms.string("FastPUPPI/NtupleProducer/data/pion_eta_phi.root"),
         corrector2  = cms.string("FastPUPPI/NtupleProducer/data/pion_eta_phi_res_old.root"),
         ecorrector  = cms.string("FastPUPPI/NtupleProducer/data/ecorr.root"),
         trackres    = cms.string("FastPUPPI/NtupleProducer/data/tkres.root"),
         eleres      = cms.string("FastPUPPI/NtupleProducer/data/eres.root"),
         pionres     = cms.string("FastPUPPI/NtupleProducer/data/pionres.root"),
         trkPtCut    = cms.double(2.0),
         metRate     = cms.bool(False),
         etaCharged  = cms.double(2.5),
         puppiPtCut  = cms.double(4.0),
         vtxRes      = cms.double(0.333),
         caloClusterer = cms.PSet(
            ecal = cms.PSet(
                zsEt = cms.double(0.4),
                seedEt = cms.double(0.5),
                minClusterEt = cms.double(0.5),
            ), 
            hcal = cms.PSet(
                zsEt = cms.double(0.4),
                seedEt = cms.double(0.5),
                minClusterEt = cms.double(0.8),
            ),
            linker = cms.PSet(
                hoeCut = cms.double(0.1),
                minPhotonEt = cms.double(1.0),
                minHadronEt = cms.double(1.0),
                useCorrectedEcal = cms.bool(True), # use corrected ecal enery in linking
            ),
         ),
         outputName  = cms.untracked.string("ntuple.root"),
         debug       = cms.untracked.int32(0),
)