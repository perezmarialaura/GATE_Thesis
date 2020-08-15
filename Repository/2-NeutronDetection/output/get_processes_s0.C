void get_processes_s0(const char *name1, const char *name2){//, const char *finalnameA, const char *finalnameB){
        char particleName[64];
        char procName[64];
        
        TChain *  T1 = new TChain("PhaseSpace");

        T1->Add(name1);
        //T1->SetBranchAddress("ParticleName",&particleName);
        T1->SetBranchAddress("CreatorProcess",&procName);
        //TH1F *histoParticleDetector;
        //TH1F *histoProcessDetector;
        //histoParticleDetector = new TH1F("histoParticle", "Particles", 10, 0, 10);
        //histoProcessDetector = new TH1F("histoProcess", "Physical processes", 10, 0, 10);
        
        int n1 = T1->GetEntries();
        int ncapture_counter = 0;
        int phot_counter = 0;
        int compt_counter = 0;
        int conv_counter = 0;
        int eBrem_counter = 0;
        int annihil_counter = 0;
        int primaries_counter = 0;
        int eIoni_counter = 0;
        int decay_counter = 0;
        int photnuc_counter = 0;
        int ninel_counter = 0;
        int hIoni_counter = 0;
        int hadElastic_counter = 0;
        int ionIoni_counter = 0;
        int protonInel_counter = 0;
        int dInelastic_counter = 0;
        for (int i1=0; i1<n1; i1++){
            T1->GetEntry(i1);
            //histoParticleDetector->Fill(particleName, 1);
            //histoProcessDetector->Fill(procName, 1);
            if (strcmp(procName, "nCapture")==0) {
                ncapture_counter += 1;
            }
            else if (strcmp(procName, "phot")==0){
                phot_counter += 1;
            }
            else if (strcmp(procName, "compt")==0){
                compt_counter += 1;
            }
            else if (strcmp(procName, "conv")==0){
                conv_counter += 1;
            }
            else if (strcmp(procName, "eBrem")==0){
                eBrem_counter += 1;
            }
            else if (strcmp(procName, "annihil")==0){
                annihil_counter += 1;
            }
            else if (strcmp(procName, "eIoni")==0){
                eIoni_counter += 1;
            }
            else if (strcmp(procName, "RadioactiveDecayBase")==0){
                decay_counter += 1;
            }
            else if (strcmp(procName, "photonNuclear")==0){
                photnuc_counter += 1;
            }
            else if (strcmp(procName, "neutronInelastic")==0){
                ninel_counter += 1;
            }
            else if (strcmp(procName, "hIoni")==0){
                hIoni_counter += 1;
            }
            else if (strcmp(procName, "hadElastic")==0){
                hadElastic_counter += 1;
            }
            else if (strcmp(procName, "ionIoni")==0){
                ionIoni_counter += 1;
            }
            else if (strcmp(procName, "protonInelastic")==0){
                protonInel_counter += 1;
            }
            else if (strcmp(procName, "dInelastic")==0){
                dInelastic_counter += 1;
            }
            else if (strcmp(procName, "")==0){
                primaries_counter += 1;
            }
            else {
                cout<<procName<<endl;
            }
        }
        ofstream outfile;
        outfile.open(name2);
        outfile << "Process Counts" << endl;
        outfile << "nCapture "<<ncapture_counter<<endl;
        outfile << "Photoelectric "<<phot_counter<<endl;
        outfile << "Compton "<<compt_counter<<endl;
        outfile << "Conversion "<<conv_counter<<endl;
        outfile << "eBremsstrahlung "<<eBrem_counter<<endl;
        outfile << "Annihilation "<<annihil_counter<<endl;
        outfile << "eIonisation "<<eIoni_counter<<endl;
        outfile << "RadioactiveDecay "<<decay_counter<<endl;
        outfile << "NuclearPhoton "<<photnuc_counter<<endl;
        outfile << "nInelastic "<<ninel_counter<<endl;
        outfile << "hIonisation "<<hIoni_counter<<endl;
        outfile << "hadElastic "<<hadElastic_counter<<endl;
        outfile << "ionIoni "<<ionIoni_counter<<endl;
        outfile << "protonInelastic "<<protonInel_counter<<endl;
        outfile << "dInelastic "<<dInelastic_counter<<endl;
        outfile << "Primaries "<<primaries_counter<<endl;
}
