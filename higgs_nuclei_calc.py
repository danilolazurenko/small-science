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
"""
<<<<<<< HEAD

from math import floor, fabs
from sys import argv
#from future import pprint
script, res_range = argv  # range of parametric resonance

mass_higgs = 125090.0  # higgs boson mass
higgs_vacuum_average = 246000.0  # vacuum expectation of higgs boson
ener_delta = 3000  # mass range of differences between higgs and nuclei
neutron_mass = 939.565  # neutron mass in MeV
proton_mass = 938.272  # proton mass in MeV
a1 = 15.75  # a1 - a5 - parameters of Weizsacker formula
=======
from math import floor, fabs
from sys import argv
script, ra = argv #ra is range of parametric resonance

mh = 125090.0 #higgs boson mass
hva = 246000.0#vacuum expectation of higgs boson
ener_delta = 3000 #mass range of differences between higgs and nuclei
n = 939.565 #neutron mass in MeV
p = 938.272 #proton mass in MeV
a1 = 15.75 #a1 - a5 - parameters of Weizsacker formula
>>>>>>> a463c088d124e222d556aa14179cdb08e44b3e06
a2 = 17.8 
a3 = 0.711
a4 = 23.7

<<<<<<< HEAD

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
    elif (charge % 2 == 0 and (nuclei_mass-charge) % 2 != 0) or (charge % 2 != 0 and (nuclei_mass-charge) % 2 == 0):
        a5 = 0
    else:
        a5 = -34
    # nuclei mass = protons mass + neutrons mass - bound energy
    nuclei_mass = charge*proton_mass+(nuclei_mass-charge)*neutron_mass-(a1*nuclei_mass-a2*nuclei_mass**(2.0/3.0)-a3*charge*charge/nuclei_mass**(1.0/3.0)-a4*(nuclei_mass/2.0-charge)*(nuclei_mass/2.0-charge)+a5*nuclei_mass**(-3.0/4.0))
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
        print("To seek parametric resonance for higgs frequencies on " + number+ "th resonance:")
        print(choose_nuclei_close_to_stability_valley_higgs(i))
        print("To seek parametric resonance for higgs average frequencies on " +number+ "th resonance:")
        print(choose_nuclei_close_to_stability_valley_higgs_avg(i))


show_all_nuclei_up_to_nth_resonance(res_range)
=======
def calculateMassDifference(z, a, ra):
    z = float(z)
    a = float(a)
    rah = mh/float(ra)
    rahva = hva/float(ra)
    if (not a) or (not z):
        print("Provide valid data, please.")
        return
    if (z%2 == 0 and (a-z)%2 ==0 ):
        a5 = 34
    elif ((z%2 ==0 and (a-z)%2 !=0) or (z%2 !=0 and (a-z)%2 ==0)):
        a5 = 0
    else:
        a5 = -34
#nuclei mass = protons mass + neutrons mass - bound energy
    nuclei_mass=z*p+(a-z)*n-(a1*a-a2*a**(2.0/3.0)-a3*z*z/a**(1.0/3.0)-a4*(a/2.0-z)*(a/2.0-z)+a5*a**(-3.0/4.0))
    hd = rah - nuclei_mass #difference for higgs mass
    hvd = rahva - nuclei_mass #difference for higgs vacuum average
    return [hd, hvd]

# neutron to proton n/p = 1+0.015*a^(2/3) ; a = n+p ~ 2p-2.5p~2.3p
def chooseNucleiCloseToStabilityValleyHiggs(nr):
    h_result_storage = []
    for i in range(1,95):
        z = i
        a_probe = floor(2*z+(2.5*z)**(2/3)*0.015)
        p1 = int(a_probe - floor(z/3.0))
        p2 = int(a_probe + floor(z/2)+1)
        mass_set = range(p1,p2,1)
        for j in mass_set:
            h_m = calculateMassDifference(z, j, nr)[0]
            if fabs(h_m)< ener_delta:
                h_result_storage += [[z, j, h_m]]
    return h_result_storage

def chooseNucleiCloseToStabilityValleyHiggsAvg(nr):
    hva_result_storage = []
    for i in range(1,95):
        z = i
        a_probe = floor(2*z+(2.5*z)**(2/3)*0.015)
        p1 = int(a_probe - floor(z/3.0))
        p2 = int(a_probe + floor(z/2)+1)
        mass_set = range(p1,p2,1)
        for j in mass_set:
            hva_m = calculateMassDifference(z, j, nr)[1]
            if fabs(hva_m)< ener_delta:
                hva_result_storage = [[z, j, hva_m]]
    return hva_result_storage

def showAllNucleiUpToNthResonance(nth):
    nth = int(nth)
    nth +=1
    for i in range(1, nth):
        print "To seek parametric resonance for higgs frequencies on " + str(i) + "th resonance:"
        print chooseNucleiCloseToStabilityValleyHiggs(i)
        print "To seek parametric resonance for higgs average frequencies on " + str(i) + "th resonance:"
        print chooseNucleiCloseToStabilityValleyHiggsAvg(i)

showAllNucleiUpToNthResonance(ra)
>>>>>>> a463c088d124e222d556aa14179cdb08e44b3e06
raw_input()
