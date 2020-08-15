{
 float Ekine;
 float x, y, z;
 float dx, dy, dz;
 char volumeName[64];
 char particleName[64];
 char procName[64];

 TChain *  T = new TChain("PhaseSpace");
 
 // select one of the four following phase spaces you wish to visualize:

 T->Add("PhaseSpaceSecondaries.root");
  
 T->SetBranchAddress("ParticleName",&particleName);
 T->SetBranchAddress("ProductionVolume",&volumeName);
 T->SetBranchAddress("CreatorProcess",&procName);
 T->SetBranchAddress("Ekine",&Ekine);
 T->SetBranchAddress("X",&x);
 T->SetBranchAddress("Y",&y);
 T->SetBranchAddress("Z",&z);
 T->SetBranchAddress("dX",&dx);
 T->SetBranchAddress("dY",&dy);
 T->SetBranchAddress("dZ",&dz);
 
 int n = T->GetEntries();
 ofstream outfile;
 outfile.open("S2_PhaseSpace_Secondaries.txt");
 outfile << "Particle  xPos yPos zPos E EmittanceX EmittanceY Process" << endl;
    // distance in cm, direction in deg, energy in MeV
 for (int i=0; i<n; i++)
 {  T->GetEntry(i);
     if(strncmp(volumeName, "world_log", 10)!=0){
         outfile << particleName << " " << x << " " << y << " " << z << " " << Ekine << " " << atan(dx/dz)*(180/TMath::Pi()) << " " << atan(dy/dz)*(180/TMath::Pi()) << " " << procName << endl;
     }
 }
}
