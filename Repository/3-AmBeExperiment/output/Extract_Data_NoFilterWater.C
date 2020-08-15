void Extract_Data_NoFilterWater(const char *filename="S1_NoFilter_Water.root", const char *outname="S1_NoFilter_Water.txt", const char *title1="Edep histogram - Moderated AmBe source, unfiltered", const char *title2="Edep histogram - Moderated AmBe source, unfiltered (centre pixel)")
{
    gROOT->Reset();
    TFile *f = new TFile(filename);
    TTree *Singles = (TTree*)gDirectory->Get("Singles");
    
    // Energy bounds in MeV
    Float_t const EMIN = 0;
    Float_t const EMAX = 600;
    Int_t const BIN = 600;
    //Declaration of leaves in TTree Singles
    Double_t time;
    Float_t energy;
    Float_t globalPosX;
    Float_t globalPosY;
    Float_t globalPosZ;
    Int_t pixelID;
    Int_t runID;
    Int_t eventID;
    Float_t rotationAngle;
    
    Singles -> SetBranchAddress( "time", &time);
    Singles -> SetBranchAddress( "energy", &energy);
    Singles -> SetBranchAddress( "globalPosX", &globalPosX);
    Singles -> SetBranchAddress( "globalPosY", &globalPosY);
    Singles -> SetBranchAddress( "globalPosZ", &globalPosZ);
    Singles -> SetBranchAddress( "pixelID", &pixelID);
    Singles -> SetBranchAddress( "runID", &runID);
    Singles -> SetBranchAddress( "eventID", &eventID);
    Singles -> SetBranchAddress( "rotationAngle", &rotationAngle);
    
    // Number of entries in the Singles tree
    Int_t entriesSingles = (Int_t)Singles->GetEntries();

    //Define histograms
    TH1F* energySpectrum = new TH1F("Total spectrum", title1, BIN, EMIN, EMAX);
    
    TH1F* energyPixel = new TH1F("One pixel", title2, BIN, EMIN, EMAX);
    
    Int_t const chosenpx = 3200;
    
    //Do loop
    for (Int_t i = 0; i != entriesSingles; ++i)
    {
        Singles->GetEntry(i);
        energySpectrum->Fill(energy*1000);
        if (pixelID == chosenpx)
        {
            energyPixel->Fill(energy*1000);
        }
    }
    
    ofstream outfile;
    outfile.open(outname);
     for (Int_t j=1; j<energySpectrum->GetNbinsX();j++){
         double bins=energySpectrum->GetBinCenter(j);
         double values=energySpectrum->GetBinContent(j);
         outfile << " " << bins << " " << values << endl;
     }
        
    delete Singles;
    //return 0;
}




