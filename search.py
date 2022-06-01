import pandas as pd
import numpy as np
import os
import info_indv as ii

'''
2003 Survey

We search for:
-Woman
-between 43 and 46 years old at the time of the survey (1957 - 1960)
-Is an Architect
-Worked as an independent architect at the time of the survey
-borned in Barcelona 
-lives in Barelona
-has 2-3 children 

'''

file_path="./datos_habisalud03"

listOfFiles = ""

for (dirpath ,  dirnames , filenames) in os.walk(file_path):
    listOfFiles = [os.path.join(dirpath ,  file) for file in filenames]

f = open(listOfFiles[0] ,  'r')

individuals = [] 

# total said by page:                                               13600
# total number of lines in the microdata:                           10838
# after selecting the data of individuals that live in cataluña:    587
# after selecting born in cataluña:                                 428
# after selecting universitary studies:                             136
# after selecting independent worker:                               12
# after born between 1957 - 1960:                                   1 

count = 0
for line in f:
    count +=1
    if line[:2]=='09'and line[2]=='6' and line[13:15]=='09' and line[17]=='7' and line[36]=='2':
        if line[5:9]=='1957' or line[5:9]=='1958' or line[5:9]=='1959' or line[5:9]=='1960':
            individuals.append(line)
            

f = open("Information.txt", "w+", encoding="utf-8")

f.write("Total of individuals who took the survey: %s\r" % str(count))
f.write("Total of individuals with the same profile: %s\r" % str(len(individuals)))
f.write("\r\n\n")
c = 0
for indv in individuals:
    c+=1
    f.write("INDIVIDUAL: %s\r\n\n" % str(c))
    f.write("ISOLATED RECORD: \r\n\n")
    f.write("%s\r\n\n" % indv)
    f.write("SOCIODEMOGRAPHIC CHARACTERISTICS\r")
    f.write("Region (CCAA):                    %s\r" % ii.ccaa(indv[:2]))
    f.write("Sex:                              %s\r" % ii.sex(indv[2]))
    f.write("Birth Month:                      %s\r" % ii.months(indv[3:5]))
    f.write("Birth Year:                       %s\r" % indv[5:9])
    f.write("Age:                              %s\r" % indv[9:12])
    f.write("Born in Spain:                    %s\r" % ii.borned_spain(indv[12]))
    f.write("CCAA of Birth:                    %s\r" % ii.ccaa(indv[13:15]))
    f.write("Born outside Spain:               %s\r" % ii.borned_outside(indv[15:17]))
    f.write("Study Level:                      %s\r" % ii.study_level(indv[17]))
    f.write("Father Study Level:               %s\r" % ii.study_level(indv[18]))
    f.write("Mother Study Level:               %s\r" % ii.study_level(indv[19]))
    f.write("Economic Status Activity:         %s\r\n\n" % ii.economic_activity(indv[20:22]))
    
    f.write("Economic activity (last week)------------------------------------ \r")
    f.write("Working:                                                     %s\r" % ii.week_activity(indv[22]))
    f.write("Employed but temporarily absent:                             %s\r" % ii.week_activity(indv[23]) )
    f.write("Unemployed but worked before:                                %s\r" % ii.week_activity(indv[24]))
    f.write("Unemployed and in search for work:                           %s\r" % ii.week_activity(indv[25]))
    f.write("Unable to work:                                              %s\r" % ii.week_activity(indv[26]))
    f.write("Pensioner:                                                   %s\r" % ii.week_activity(indv[27]))
    f.write("Taking a Course:                                             %s\r" % ii.week_activity(indv[28]))
    f.write("Dedicated mainly to housework:                               %s\r" % ii.week_activity(indv[29]))
    f.write("Dedicated to volunteering:                                   %s\r" % ii.week_activity(indv[30]))
    f.write("Another situation without exercising any economic activity:  %s\r" % ii.week_activity(indv[31]))
    f.write("No Data:                                                     %s\r" % ii.week_activity(indv[32]))
    f.write("----------------------------------------------------------------- \r\n\n")
    
    f.write("Worked once before:               %s\r" % ii.worked_once(indv[33]))
    f.write("Ocupation:                        %s\r" % ii.ocupation(indv[34:36]))
    f.write("Professional Situation:           %s\r" % ii.profesional_situation(indv[36]))
    f.write("Marital status:                   %s\r\n\n" % ii.civil(indv[37]))
    
    f.write("LIFESTYLE\r")
    f.write("Coexistance with others:             %s\r\n\n" % ii.coexistance(indv[38]))
    f.write("Coexistance with --------------------------------- \r")
    f.write("Spouse/Partner:                      %s\r" % ii.coexistance_with(indv[39]))
    f.write("Parents/Tutor:                       %s\r" % ii.coexistance_with(indv[40]))
    f.write("Own Children:                        %s\r" % ii.coexistance_with(indv[41]))
    f.write("Spouse/Partner's Children:           %s\r" % ii.coexistance_with(indv[42]))
    f.write("Other blood or political relatives:  %s\r" % ii.coexistance_with(indv[43]))
    f.write("Friends/Flatmates:                   %s\r" % ii.coexistance_with(indv[44]))
    f.write("Other People:                        %s\r" % ii.coexistance_with(indv[45]))
    f.write("No Data:                             %s\r" % ii.coexistance_with(indv[46]))
    f.write("-------------------------------------------------- \r\n\n")
    f.write("Nights-out Frequency:                                    %s\r" % ii.night_outs(indv[47]))
    f.write("Nights-out Frequency because of work or studies:         %s\r" % ii.night_outs(indv[48]))
    f.write("Alcohol Consumption:                                     %s\r" % ii.alcoholic_beverages(indv[49]))
    f.write("Frequency of alcohol consumption:                        %s\r" % ii.freq_drink_alcoholic(indv[50]))
    f.write("Number of cups a day:                                    %s\r" % ii.num_cups(indv[51]))
    f.write("Number of days in the last month of alcohol consumption: %s\r" % indv[52:54])
    f.write("Drug consumption:                                        %s\r\n\n" % ii.drug_consumption(indv[54]))
    
    f.write("INFORMATION AND SEXUAL EXPERIENCE\r")
    f.write("Communication with parents about sex:                    %s\r" % ii.communication_parents(indv[55]))
    f.write("Preferred source of sexual information:                  %s\r" % ii.reference_sex_ed(indv[56:58]))
    f.write("Main source of sexual information:                       %s\r" % ii.reference_sex_ed(indv[58:60]))
    f.write("Source of information on contraceptive methods:          %s\r" % ii.reference_sex_ed(indv[60:62]))
    f.write("Have you had sexual intercourse?:                        %s\r" % ii.sexual_relationship(indv[62]))
    f.write("With whom (man/woman) have you had sexual intercourse?:  %s\r\n\n" % ii.intercourse_sex(indv[63]))
    
    f.write("Sexual experience: Women\r")
    f.write("Performing sexual practices with women: %s\r\n\n" % ii.sexual_relationship(indv[172]))
    
    f.write("FOR WOMEN\r\n\n")
    f.write("First sexual relationship\r")
    f.write("Age of beginning of sexual intercourse:                        %s\r" % indv[174:176])
    f.write("Partner's age with whom she had her first sexual relationship: %s\r" % indv[176:178])
    f.write("Use of condoms at first sexual intercourse:                    %s\r" % ii.perservative(indv[178]))
    f.write("Did you take precautions to avoid pregnancy?                   %s\r\n\n" % ii.precaution_taken(indv[179]))
    f.write("Contraceptive methods used------------------------------------------------------\r")
    f.write("Preservative:                                    %s\r" % ii.anticonceptive_usage(indv[180]))
    f.write("Pill:                                            %s\r" % ii.anticonceptive_usage(indv[181]))
    f.write("Reverse or retreat:                              %s\r" % ii.anticonceptive_usage(indv[182]))
    f.write("Morning-after pill:                              %s\r" % ii.anticonceptive_usage(indv[183]))
    f.write("'Ogino' (rhythm method):                         %s\r" % ii.anticonceptive_usage(indv[184]))
    f.write("Other methods:                                   %s\r" % ii.anticonceptive_usage(indv[185]))
    f.write("We felt safe because it was during menstruation: %s\r" % ii.anticonceptive_usage(indv[186]))
    f.write("No Data:                                         %s\r" % ii.anticonceptive_usage(indv[187]))
    f.write("--------------------------------------------------------------------------------\r\n\n")
    
    f.write("Sexual relationship during life\r")
    f.write("Number of sexual partners:                          %s\r" % ii.sexual_partners(indv[188]))
    f.write("Use of condoms:                                     %s\r" % ii.perservative(indv[189]))
    f.write("Use of preservative in the last sexual intercourse: %s\r\n\n" % ii.perservative(indv[190]))
    
    f.write("Sexual relationship in the last 12 months\r")
    f.write("Did you have sexual relationships?         %s\r" % ii.sexual_relationship(indv[191]))
    f.write("Number of sexual partners:                 %s\r" % indv[192:194])
    f.write("Use of condoms:                            %s\r" % ii.perservative(indv[194]))
    f.write("Sexual relationship with casual partners:  %s\r" % ii.sexual_relationship(indv[195]))
    f.write("Use of condoms with casual partners:       %s\r\n\n" % ii.perservative_ocasional_partner(indv[196]))
    
    f.write("Sexual relationship in the last month\r")
    f.write("Did you have sexual relationships?     %s\r" %  ii.sexual_relationship(indv[197]))
    f.write("Number of days you had sex:            %s\r\n\n" % indv[198:200])
    
    f.write("Sexual relationship with a new partner in the last 12 months\r")
    f.write("Did you have sexual relationships?     %s\r" % ii.sexual_relationship(indv[200]))
    f.write("Number of new sexual partners:         %s\r\n\n" % indv[201:203])
    
    f.write("Sexual relationship with the last partner\r")
    f.write("Was this the first time in your life that you have had sexual intercourse?  %s\r" % ii.sexual_relationship(indv[203]))
    f.write("Partner's age when they first had sex:                                      %s\r" % indv[204:206])
    f.write("Type of relationship with last new partner the first time they had sex:     %s\r" % ii.relationship_type(indv[206]))
    f.write("Were you drunk the first time you had sex with your partner?                %s\r" % ii.drunk(indv[207]))
    f.write("Use of condom the dirst time:                                               %s\r" % ii.perservative(indv[208]))
    f.write("Who brought the condom?                                                     %s\r" % ii.preservative_bring(indv[209]))
    f.write("Reason for not using condoms (1):                                           %s\r" % ii.reason_preservative_1(indv[210:212]))
    f.write("Reason for not using condoms (2):                                           %s\r" % ii.reason_preservative_1(indv[212:213]))
    f.write("Did you take precautions against pregnacy?                                  %s\r\n\n" % ii.precaution_taken(indv[214]))
    
    f.write("Contraceptive methods used------------------------------------------------------\r")
    f.write("Condom:                                          %s\r" % ii.anticonceptive_usage(indv[215]))
    f.write("Pill:                                            %s\r" % ii.anticonceptive_usage(indv[216]))
    f.write("Reverse or retreat:                              %s\r" % ii.anticonceptive_usage(indv[217]))
    f.write("Morning-after pill:                              %s\r" % ii.anticonceptive_usage(indv[218]))
    f.write("'Ogino' (rhythm method):                         %s\r" % ii.anticonceptive_usage(indv[219]))
    f.write("Other methods:                                   %s\r" % ii.anticonceptive_usage(indv[220]))
    f.write("We felt safe because it was during menstruation: %s\r" % ii.anticonceptive_usage(indv[221]))
    f.write("No Data:                                         %s\r" % ii.anticonceptive_usage(indv[222]))
    f.write("--------------------------------------------------------------------------------\r\n\n")
    
    f.write("Do you think this couple had sexual relations with other people?               %s\r" % ii.cheated(indv[223]))
    f.write("Did you have sex with other people?                                            %s\r" % ii.cheat_with(indv[224]))
    f.write("After this first sexual intercourse, did you have sexual intercourse again?    %s\r" % ii.sexual_relationship(indv[225]))
    f.write("Use of a condom last time:                                                     %s\r" % ii.perservative(indv[226]))
    f.write("Did you take precautions against pregnacy?                                     %s\r\n\n" % ii.precaution_taken(indv[227]))
    
    f.write("Contraceptive methods used------------------------------------------------------\r")
    f.write("Condom:                                          %s\r" % ii.anticonceptive_usage(indv[228]))
    f.write("Pill:                                            %s\r" % ii.anticonceptive_usage(indv[229]))
    f.write("Reverse or retreat:                              %s\r" % ii.anticonceptive_usage(indv[230]))
    f.write("Morning-after pill:                              %s\r" % ii.anticonceptive_usage(indv[231]))
    f.write("'Ogino' (rhythm method):                         %s\r" % ii.anticonceptive_usage(indv[232]))
    f.write("Other methods:                                   %s\r" % ii.anticonceptive_usage(indv[233]))
    f.write("We felt safe because it was during menstruation: %s\r" % ii.anticonceptive_usage(indv[234]))
    f.write("No Data:                                         %s\r" % ii.anticonceptive_usage(indv[235]))
    f.write("--------------------------------------------------------------------------------\r\n\n")
    
    f.write("Attitude towards the use of condoms: %s\r" % ii.attitude_preservatives(indv[236]))

    f.write("SEXUAL HEALTH\r")
    f.write("Have you ever been diagnosed with the following STD:-----------------------------\r")
    f.write("Chlamydia infection:                                       %s\r" % ii.STD(indv[237]))
    f.write("Gonorrhea:                                                 %s\r" % ii.STD(indv[238]))
    f.write("Syphilis:                                                  %s\r" % ii.STD(indv[239]))
    f.write("Trichomonas:                                               %s\r" % ii.STD(indv[240]))
    f.write("Genital herpes:                                            %s\r" % ii.STD(indv[241]))
    f.write("Genital ulcers or condyloma:                               %s\r" % ii.STD(indv[242]))
    f.write("Mycosis or fungus:                                         %s\r" % ii.STD(indv[243]))
    f.write("Hepatitis B:                                               %s\r" % ii.STD(indv[244]))
    f.write("Non-specific urethritis:                                   %s\r" % ii.STD(indv[245]))
    f.write("Crabs or genital pediculosis:                              %s\r" % ii.STD(indv[246]))
    f.write("Other sexually transmitted disease:                        %s\r" % ii.STD(indv[247]))
    f.write("I have not been diagnosed with any STD:                    %s\r" % ii.STD(indv[248]))
    f.write("No data:                                                   %s\r" % ii.STD(indv[249]))
    f.write("---------------------------------------------------------------------------------\r\n\n")
    f.write("Last diagnosed STD:    %s\r" % ii.last_STD(indv[250:252]))
    f.write("Time since last STD:   %s\r\n\n" % ii.last_STD(indv[252]))
    
    f.write("HIV TEST\r")
    f.write("Blood donation:                                %s\r" % ii.VIH(indv[253]))
    f.write("HIV specific test:                             %s\r" % ii.VIH_testing(indv[254]))
    f.write("Time since the last specific HIV test:         %s\r" % ii.VIH_time(indv[255]))
    f.write("Reason for testing:                            %s\r" % ii.VIH_reason(indv[256]))
    f.write("Test location:                                 %s\r" % ii.VIH_location(indv[257:259]))
    f.write("Did you get to know the results of the test?   %s\r\n\n" % ii.VIH(indv[259]))
    
    f.write("ATTITUDES\r")
    f.write("Opinion about the risk of HIV infection they have----------------------------------------------------------------------------------------------------------------------------------\r")
    f.write("People who only have sexual relations with their stable partner of the opposite sex or within marriage:                                                                %s\r" % ii.VIH_risk(indv[260]))
    f.write("People with a stable partner of the opposite sex or married, who occasionally have sexual relations with another person of the opposite sex, other than their partner: %s\r" % ii.VIH_risk(indv[261]))
    f.write("People who have sex with multiple partners of the opposite sex:                                                                                                        %s\r" % ii.VIH_risk(indv[262]))
    f.write("Men who only have homosexual relationships with their stable same-sex partner:                                                                                         %s\r" % ii.VIH_risk(indv[263]))
    f.write("Men with a stable same-sex partner who occasionally have homosexual relationships with another man:                                                                    %s\r" % ii.VIH_risk(indv[264]))
    f.write("Men who have same-sex relationships with other men:                                                                                                                    %s\r" % ii.VIH_risk(indv[265]))
    f.write("Women who engage in sexual practices with other women:                                                                                                                 %s\r" % ii.VIH_risk(indv[266]))
    f.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\r\n\n")
    
    f.write("Do you think that HIV can be transmitted in the following situation---------------------\r")
    f.write("In sexual intercourse:                                             %s\r" % ii.VIH_transmission(indv[267]))
    f.write("Receiving blood:                                                   %s\r" % ii.VIH_transmission(indv[268]))
    f.write("In public restrooms:                                               %s\r" % ii.VIH_transmission(indv[269]))
    f.write("Drinking from the glass of an infected person:                     %s\r" % ii.VIH_transmission(indv[270]))
    f.write("For a mosquito bite:                                               %s\r" % ii.VIH_transmission(indv[271]))
    f.write("When donating blood:                                               %s\r" % ii.VIH_transmission(indv[272]))
    f.write("Being hospitalized in the same place as an infected person:        %s\r" % ii.VIH_transmission(indv[273]))
    f.write("In none of these situations:                                       %s\r" % ii.VIH_transmission(indv[274]))
    f.write("No Data:                                                           %s\r" % ii.VIH_transmission(indv[275]))
    f.write("--------------------------------------------------------------------------------------\r\n\n")
    
    f.write("Opinion on the risk of infection of people who inject drugs:   %s\r" % ii.drug_risk(indv[276]))
    f.write("Perception of own risk of contracting AIDS:                    %s\r" % ii.VIH_risk(indv[277]))
    f.write("Have you been afraid of having contracted AIDS?                %s\r" % ii.VIH(indv[278]))
    f.write("Would work or study with a person infected with HIV:           %s\r\n\n" % ii.VIH(indv[279]))
    
    f.write("Opinion on the effectiveness of the following preventive measure to protect against HIV--\r")
    f.write("Wash after intercourse:                    %s\r" % ii.VIH_pre_eff(indv[280]))
    f.write("Choose the partner correctly:              %s\r" % ii.VIH_pre_eff(indv[281]))
    f.write("Have few partners:                         %s\r" % ii.VIH_pre_eff(indv[282]))
    f.write("Use a male condom:                         %s\r" % ii.VIH_pre_eff(indv[283]))
    f.write("Use spermicides:                           %s\r" % ii.VIH_pre_eff(indv[284]))
    f.write("Request an AIDS test from the partner:     %s\r" % ii.VIH_pre_eff(indv[285]))
    f.write("Get tested for HIV often:                  %s\r" % ii.VIH_pre_eff(indv[286]))
    f.write("Ask couples about their sexual past:       %s\r" % ii.VIH_pre_eff(indv[287]))
    f.write("Use a female condom:                       %s\r" % ii.VIH_pre_eff(indv[288]))
    f.write("-----------------------------------------------------------------------------------------\r\n\n")
    
    f.write("Opinion about condoms-------------------------------------------------------------\r")
    f.write("They are complicated to use:                                       %s\r" % ii.preservatives_opinion_0(indv[289]))
    f.write("They create distrust between the couple:                           %s\r" % ii.preservatives_opinion_1(indv[290]))
    f.write("Women are cut off by desire:                                       %s\r" % ii.preservatives_opinion_2(indv[291]))
    f.write("Men are cut off by desire:                                         %s\r" % ii.preservatives_opinion_2(indv[292]))
    f.write("They prevent you from truly feeling each other's body:             %s\r" % ii.preservatives_opinion_2(indv[293]))
    f.write("They allow you to enjoy more because of the security they give:    %s\r" % ii.preservatives_opinion_2(indv[294]))
    f.write("They're safe:                                                      %s\r" % ii.preservatives_opinion_2(indv[295]))
    f.write("----------------------------------------------------------------------------------\r\n\n")
    
    f.write("Religious belief:                                      %s\r" % ii.religion(indv[296]))
    f.write("Attendance at religious acts:                          %s\r" % ii.religion_assistance(indv[297]))
    f.write("Lift factor:                                           %s\r" % indv[298:309])
    f.write("Size of the municipality of residence:                 %s\r" % ii.size_municipy(indv[309]))
    f.write("Parents' highest educational level:                    %s\r" % ii.study_level(indv[310]))
    f.write("People with whom you have lived in the last 12 months: %s\r" % ii.campany_12(indv[311]))


