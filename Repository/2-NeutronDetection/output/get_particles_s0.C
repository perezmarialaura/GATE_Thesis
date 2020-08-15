void get_particles_s0(const char *name1, const char *name2){//, const char *finalnameA, const char *finalnameB){
        char particleName[64];
        char procName[64];
        
        TChain *  T1 = new TChain("PhaseSpace");

        T1->Add(name1);
        T1->SetBranchAddress("ParticleName",&particleName);

        int n1 = T1->GetEntries();
        int neutron_counter = 0;
        int gamma_counter = 0;
        int electron_counter = 0;
        int positron_counter = 0;
        int neutrino_counter = 0;
        int antinu_counter = 0;
        int cd_counter = 0;
        int gd_counter = 0;
        int te_counter = 0;
        int proton_counter = 0;
        int alpha_counter = 0;
        int others_counter = 0;
    
        for (int i1=0; i1<n1; i1++){
            T1->GetEntry(i1);
            if (strcmp(particleName, "neutron")==0) {
                neutron_counter += 1;
            }
            else if (strcmp(particleName, "gamma")==0){
                gamma_counter += 1;
            }
            else if (strcmp(particleName, "e-")==0){
                electron_counter += 1;
            }
            else if (strcmp(particleName, "e+")==0){
                positron_counter += 1;
            }
            else if (strcmp(particleName, "nu_e")==0){
                neutrino_counter += 1;
            }
            else if (strcmp(particleName, "anti_nu_e")==0){
                antinu_counter += 1;
            }
            else if (strncmp(particleName, "Cd",2)==0){
                cd_counter += 1;
            }
            else if (strncmp(particleName, "Te",2)==0){
                te_counter += 1;
            }
            else if (strncmp(particleName, "Gd",2)==0){
                gd_counter += 1;
            }
            else if (strcmp(particleName, "proton")==0){
                proton_counter += 1;
            }
            else if (strcmp(particleName, "alpha")==0){
                alpha_counter += 1;
            }
            else {
                others_counter += 1;
            }
        }
    ofstream outfile;
    outfile.open(name2);
    outfile << "Particle Counts" << endl;
    outfile << "gamma "<<gamma_counter<<endl;
    outfile << "electron "<<electron_counter<<endl;
    outfile << "positron "<<positron_counter<<endl;
    outfile << "neutrino "<<neutrino_counter<<endl;
    outfile << "antineutrino "<<antinu_counter<<endl;
    outfile << "proton "<<proton_counter<<endl;
    outfile << "alpha "<<alpha_counter<<endl;
    outfile << "Cdisot "<<cd_counter<<endl;
    outfile << "Teisot "<<te_counter<<endl;
    outfile << "Gdisot "<<gd_counter<<endl;
    outfile << "others "<<others_counter<<endl;
    outfile << "neutron "<<neutron_counter<<endl;
}

