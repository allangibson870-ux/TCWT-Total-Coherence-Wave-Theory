# Create .ini for c3 = 0.1
cat << 'E' > c3_01.ini
h = 0.674
omega_b = 0.02237
omega_cdm = 0.1200
gravity_model = tcwt
tcwt_upsilon_breaking = 0.5
tcwt_c3_galileon = 0.1
output = mPk
z_pk = 0
root = output/study_c3_01_
E

# Create .ini for c3 = 1.0
cat << 'E' > c3_10.ini
h = 0.674
omega_b = 0.02237
omega_cdm = 0.1200
gravity_model = tcwt
tcwt_upsilon_breaking = 0.5
tcwt_c3_galileon = 1.0
output = mPk
z_pk = 0
root = output/study_c3_10_
E

# Create .ini for c3 = 2.0
cat << 'E' > c3_20.ini
h = 0.674
omega_b = 0.02237
omega_cdm = 0.1200
gravity_model = tcwt
tcwt_upsilon_breaking = 0.5
tcwt_c3_galileon = 2.0
output = mPk
z_pk = 0
root = output/study_c3_20_
E

# Create .ini for c3 = 5.0
cat << 'E' > c3_50.ini
h = 0.674
omega_b = 0.02237
omega_cdm = 0.1200
gravity_model = tcwt
tcwt_upsilon_breaking = 0.5
tcwt_c3_galileon = 5.0
output = mPk
z_pk = 0
root = output/study_c3_50_
E
