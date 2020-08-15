void getRadCurve(const char *filename, const char *outnameenergy, const char *outnamerot){
    
    gROOT->Reset();
    TFile *f = new TFile(filename);
    TTree *Singles = (TTree*)gDirectory->Get("Singles");
    
    //Declaration of leaves in TTree Singles
    Float_t energy;
    Float_t rotationAngle;
    
    Singles -> SetBranchAddress( "energy", &energy);
    Singles -> SetBranchAddress( "rotationAngle", &rotationAngle);
    
    // Number of entries in the Singles tree
    Int_t entriesSingles = (Int_t)Singles->GetEntries();

    //Define histograms
    TH1F* energySpectrum = new TH1F("Energy Spectrum", "Detected energy spectrum", 600, 0, 600);
    
    TH1F* rotAngleHisto = new TH1F("Rotation Angle", "RadICAL curve", 180, 0, 180);
    
    //Do loop
    for (Int_t i = 0; i != entriesSingles; ++i)
    {
        Singles->GetEntry(i);
        energySpectrum->Fill(energy*1000);
        rotAngleHisto->Fill(rotationAngle);
    }
    
    ofstream outfile;
    outfile.open(outnamerot);
     for (Int_t j=1; j<rotAngleHisto->GetNbinsX();j++){
         double bins=rotAngleHisto->GetBinCenter(j);
         double values=rotAngleHisto->GetBinContent(j);
         outfile << " " << bins << " " << values << endl;
     }
    
    ofstream outfile2;
    outfile2.open(outnameenergy);
     for (Int_t j=1; j<energySpectrum->GetNbinsX();j++){
         double bins=energySpectrum->GetBinCenter(j);
         double values=energySpectrum->GetBinContent(j);
         outfile2 << " " << bins << " " << values << endl;
     }
        
}
