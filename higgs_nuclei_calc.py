"""
This program should calculate approximate set of 
isotopes, which nuclei have de-Broglie wavelength 
close to n-th part of de-Brogile wavelength of 
Higgs boson and his nonzero vacuum expectation.
All energies provided in MeV.

This program uses naive approach and doesn't take in 
account non-sphericity of nuclei and more complex effects. 
After all, this is only rough estimation.
In future estimations a nudat2 data should be used
for seeking for stable isotopes.
# TODO update weizsacker formulas - also, it gives wrong results
"""


from math import floor, fabs


resonance_range = 1
mass_higgs = 125180.0  # higgs boson mass in MeV
higgs_vacuum_average = 246000.0  # vacuum expectation of higgs boson in MeV
ener_delta = 1000  # mass range of differences between higgs and nuclei
neutron_mass = 939.565  # neutron mass in MeV
proton_mass = 938.272  # proton mass in MeV
a1 = 15.75  # a1 - a5 - parameters of Weizsacker formula
a2 = 17.8 
a3 = 0.711
a4 = 23.7


def calculate_mass_difference(charge, nuclei_mass, res_range):
    charge = float(charge)
    nuclei_mass = float(nuclei_mass)
    ranged_higgs = mass_higgs/float(res_range)
    ranged_higgs_vacuum_avg = higgs_vacuum_average/float(res_range)
    if (not nuclei_mass) or (not charge):
        print("Provide valid data, please.")
        return
    if charge % 2 == 0 and (nuclei_mass-charge) % 2 == 0:
        a5 = 34
    elif (charge % 2 == 0 and (nuclei_mass-charge) % 2 != 0) \
            or (charge % 2 != 0 and (nuclei_mass-charge) % 2 == 0):
        a5 = 0
    else:
        a5 = -34
    # nuclei mass = protons mass + neutrons mass - bound energy
    nuclei_mass = (
            charge * proton_mass + (nuclei_mass - charge) *
            neutron_mass - (a1 * nuclei_mass - a2 * nuclei_mass**(2.0/3.0) -
                            a3 * charge * charge / nuclei_mass**(1.0/3.0) -
                            a4 * (nuclei_mass / 2.0 - charge) *
                            (nuclei_mass / 2.0 - charge) +
                            a5 * nuclei_mass**(-3.0/4.0)))
    higgs_mass_difference = ranged_higgs - nuclei_mass  # difference for higgs mass
    higgs_vacuum_difference = ranged_higgs_vacuum_avg - nuclei_mass  # difference for higgs vacuum average
    return [higgs_mass_difference, higgs_vacuum_difference]


# number of neutrons to protons = 1+0.015*nuclei_mass^(2/3) ; nuclei_mass = n+p ~ 2p-2.5p~2.3p
def choose_nuclei_close_to_stability_valley_higgs(range_number):
    h_result_storage = []
    minimal_charge = 1
    maximal_charge = 95
    for i in range(minimal_charge, maximal_charge):
        charge = i
        nuclei_mass_probe = floor(2*charge+(2.5*charge)**(2/3)*0.015)
        neutron_rich = int(nuclei_mass_probe - floor(charge/3.0))
        proton_rich = int(nuclei_mass_probe + floor(charge/2)+1)
        mass_set = range(neutron_rich, proton_rich, 1)
        for j in mass_set:
            higgs_mass_delta = calculate_mass_difference(charge, j, range_number)[0]
            if fabs(higgs_mass_delta) < ener_delta:
                h_result_storage += [[charge, j, higgs_mass_delta]]
    return h_result_storage


def choose_nuclei_close_to_stability_valley_higgs_avg(range_number):
    higgs_vacuum_avg_result_storage = []
    minimal_charge = 1
    maximal_charge = 95
    for i in range(minimal_charge, maximal_charge):
        charge = i
        nuclei_mass_probe = floor(2*charge+(2.5*charge)**(2/3)*0.015)
        neutron_rich = int(nuclei_mass_probe - floor(charge/3.0))
        proton_rich = int(nuclei_mass_probe + floor(charge/2)+1)
        mass_set = range(neutron_rich, proton_rich, 1)
        for j in mass_set:
            higgs_vacuum_average_mass = calculate_mass_difference(charge, j, range_number)[1]
            if fabs(higgs_vacuum_average_mass) < ener_delta:
                higgs_vacuum_avg_result_storage = [[charge, j, higgs_vacuum_average_mass]]
    return higgs_vacuum_avg_result_storage


def show_all_nuclei_up_to_nth_resonance(resonance_number):
    resonance_number = int(resonance_number)
    resonance_number += 1
    for i in range(1, resonance_number):
        number = str(i)
        print("To seek parametric resonance for higgs frequencies on " + number+ "th resonance: \n")
        for rec in choose_nuclei_close_to_stability_valley_higgs(i):
            print(rec)
        print("To seek parametric resonance for higgs average frequencies on " +number+ "th resonance: \n")
        for rec in choose_nuclei_close_to_stability_valley_higgs_avg(i):
            print(rec)


show_all_nuclei_up_to_nth_resonance(resonance_range)
