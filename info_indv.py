
# section A
#CCAA, A_3B
def ccaa(str):

    switcher = {
        "01":"Andalucía",
        "02":"Aragón",
        "03":"Asturias (Principado de)",
        "04":"Balears (Illes)",
        "05":"Canarias",
        "06":"Cantabria",
        "07":"Castilla y León",
        "08":"Castilla-La Mancha",
        "09":"Cataluña",
        "10":"Comunidad Valenciana",
        "11":"Extremadura",
        "12":"Galicia",
        "13":"Madrid (Comunidad de)",
        "14":"Murcia (Región de)",
        "15":"Navarra (Comunidad Foral de)",
        "16":"País Vasco",
        "17":"Rioja (La)",
        "18":"Ceuta y Melilla"
    }
    
    ccaa_ = switcher.get(str, "NaN")
    return ccaa_

#sexo
def sex(str):
    switcher = {
        "1":"Male",
        "6":"Female"
    }
    
    sex_ = switcher.get(str, " ")
    return sex_

def months(str):
    
    switcher = {
        "01": "January",
        "02": "February",
        "03": "March",
        "04": "April",
        "05": "May",
        "06": "June",
        "07": "July",
        "08": "August",
        "09": "September",
        "10": "October",
        "11": "November",
        "12": "December"
    }
    month = switcher.get(str, " ")
    
    return month

#A_3A
def borned_spain(str):
    switcher = {
        "1":"Yes",
        "6":"No",
        "9":"No Data"
    }
    
    case = switcher.get(str, " ")

    return case

#A_3C
def borned_outside(str):
    switcher = {
        "01": "Country Inside the EU",
        "02": "Rumania",
        "03": "Other European Country",
        "04": "Canada or EE.UU.",
        "05": "Other Country in North America",
        "06": "Country in Central America",
        "07": "Colombia or Ecuador",
        "08": "Other Country in South America",
        "09": "A Country in Magreb",
        "10": "Country in Africa",
        "11": "Country in Asia",
        "12": "Country in Oceania",
        "99": "No Data"
    }
    country = switcher.get(str, "No")
    return country

#A_4A, A_4B, A_4C
def study_level(str):
    switcher = {
        "1":"Illiterate",
        "2":"Primary Studies Complete or Incomplete",
        "3":"First Stage General Secondary Education",
        "4":"Intermediate Vocational Training Degree",
        "5":"Second Stage General Secondary Education",
        "6":"Higher Vocational Training Degree",
        "7":"University Studies",
        "8":"Parent Educational Level Unknown"
    }
    
    study = switcher.get(str, " ")
    return study

#A_5
def economic_activity(str):
    switcher = {
        "01":"Working",
        "02":"Employed but temporarily absent",
        "03":"Unemployed but worked before",
        "04":"Unemployed and in search for work",
        "05":"Unable to work",
        "06":"Pensioner",
        "07":"Taking a Course",
        "08":"Dedicated mainly to housework (non-economic activity)",
        "09":"Dedicated to volunteering (NGOs, parishes, etc.)",
        "10":"Another situation without exercising any economic activity",
        "99":"No Data"
    }
    
    activity = switcher.get(str, " ")
    
    return activity

#All A_6's
def week_activity(str):
    switcher = {
        "0":"No",
        "1":"Yes"
    }
    
    activity = switcher.get(str, " ")
    
    return activity

#A_7
def worked_once(str):
    switcher = {
        "1":"Yes",
        "6":"No",
        "9":"No Data"
    }
    
    result = switcher.get(str, "No Response")
    
    return result

#A_8
def ocupation(str):
    switcher = {
        "00":"Army",
        "01":"Management of companies and public administrations",
        "02":"Scientific and intellectual technicians and professionals",
        "03":"Technicians and support professionals",
        "04":"Administrative type employee",
        "05":"Workers of catering services, personal, protection and vendors of shops",
        "06":"Skilled workers in agriculture and fishing",
        "07":"Artisans and skilled workers in the manufacturing, construction, and mining industries, except plant and machinery operators",
        "08":"Plant and machinery operators and assemblers",
        "09":"Unskilled workers",
        "99":"No Data"
    }
    
    ocupation_ = switcher.get(str, " ")
    return ocupation_

#A_9
def profesional_situation(str):
    switcher = {
        "1":"Employer (entrepreneur or professional with employees)",
        "2":"Entrepreneur without employees or independent worker",
        "3":"Family help",
        "4":"Fixed wage earner",
        "5":"Temporary or interim employee",
        "6":"Member of a cooperative",
        "7":"Other",
        "9":"No Data"
    }
    
    prof_situation = switcher.get(str, " ")
    
    return prof_situation

#A_10
def civil(str):
    switcher = {
        "1":"Single",
        "2":"Married",
        "3":"Legally separated",
        "4":"Divorced",
        "5":"Widow",
        "9":"No Data"
    }
    
    civil_ = switcher.get(str, " ")
    
    return civil_


# section B

def coexistance(str):
    switcher = {
        "1":"Other People",
        "6":"Alone",
        "9":"No Data"
    }
    
    coexistance_ = switcher.get(str, " ")
    return coexistance_

def coexistance_with(str):
    switcher = {
        "0":"No",
        "1":"Yes"
    }
    
    result = switcher.get(str, " ")
    return result

def night_outs(str):
    switcher = {
        "1":"Three or more days a week",
        "2":"One or two days a week",
        "3":"One or three days a month",
        "4":"Less than once a month",
        "5":"No",
        "9":"No Data"
    }
    
    out = switcher.get(str, " ")
    return out

def alcoholic_beverages(str):
    switcher = {
        "1":"Yes",
        "6":"No",
        "9":"No Data"
    }
    
    case = switcher.get(str, " ")
    return case

def freq_drink_alcoholic(str):
    switcher = {
        "1":"Daily",
        "2":"Four to six days a week",
        "3":"Two to three days a week",
        "4":"Once a week",
        "5":"Once each two weeks",
        "6":"Once a month",
        "7":"Less than once a month",
        "9":"No Data"
    }
    
    freq = switcher.get(str, " ")
    return freq

def num_cups(str):
    switcher = {
        "1":"One or two",
        "2":"Three or four",
        "3":"Five or six",
        "4":"More than six",
        "9":"No Data"
    }
    
    num = switcher.get(str, " ")
    return num

def drug_consumption(str):
    switcher = {
        "1":"Yes",
        "6":"No",
        "9":"No Data"
    }
    
    case = switcher.get(str, " ")
    return case


# section C

def communication_parents(str):
    switcher = {
        "1":"Very satisfactory",
        "2":"Quite satisfactory",
        "3":"Satisfactory",
        "4":"Unsatisfactory",
        "5":"Nothing satisfactory",
        "6":"I had no communication",
        "9":"No Data"
    }
    
    result = switcher.get(str, " ")
    return result

def reference_sex_ed(str):
    switcher = {
        "01":"Mother",
        "02":"Father",
        "03":"Siblings",
        "04":"Spouse/partner",
        "05":"Other family members",
        "06":"Teachers at school",
        "07":"Friends of the same age",
        "08":"Doctor, Nurse or other health personnel",
        "09":"Television/vides/radio",
        "10":"Books, newspaper or magazines",
        "11":"No one told me anything",
        "99":"No Data"
    }
    
    information = switcher.get(str, " ")
    return information

def sexual_relationship(str):
    switcher = {
        "1":"Yes",
        "6":"No",
        "9":"No Data"
    }
    
    case = switcher.get(str, "No response")
    return case

def intercourse_sex(str):
    switcher = {
        "1":"Only with women",
        "2":"More often with women, but at least once with a man",
        "3":"Same with men as with women",
        "4":"More often with men, but at least once also with a woman",
        "5":"Only with men"
    }
    
    result = switcher.get(str, "No response")
    return result

# section C3 Women

def perservative(str):
    
    switcher = {
        "1":"Yes",
        "2":"No",
        "6":"No",
        "3":"I don't remember",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    
    return result

def precaution_taken(str):
    
    switcher = {
        "1":"Yes",
        "2":"No",
        "3":"No, beacause there was no penetration",
        "9":"No Data"
    }
    
    result = switcher.get(str, "No response")
    
    return result

def anticonceptive_usage(str):
    switcher = {
    "1":"Yes",
    "0":"No",
    }
    
    result = switcher.get(str, "No response")
    return result

def sexual_partners(str):
    switcher = {
        "1":"With one man",
        "2":"With two men",
        "3":"Three or four men",
        "4":"Five to nine men",
        "5":"Ten or more men",
        "9":"No data"
    }
    num_sexual_partner = switcher.get(str, "No response")
    return num_sexual_partner

def perservative_ocasional_partner(str):
    switcher = {
        "1":"Never",
        "2":"Sometimes",
        "3":"Always",
        "9":"No Data"
    }
    
    result = switcher.get(str, "No response")
    return result

def relationship_type(str):
    switcher = {
        "1":"Just married",
        "2":"We were going to get married",
        "3":"We had a relationship",
        "4":"It was a man who practiced prostitution",
        "5":"We just met",
        "6":"We met before",
        "7":"Other",
        "9":"No Data"
    }
    
    result = switcher.get(str, "No response")
    return result

def drunk(str):
    switcher = {
        "1":"No",
        "2":"Just a little",
        "3":"Yes",
        "4":"I don't remember",
    }
    
    result = switcher.get(str, "No response")
    return result

def preservative_bring(str):
    switcher = {
        "1":"Me",
        "2":"My partner",
        "3":"Both",
        "4":"I don't remember",
    }
    
    result = switcher.get(str, "No response")
    return result

def reason_preservative_1(str):
    switcher = {
        "01":"We don't talk about it before having sex",
        "02":"It was very difficult for me to propose the condom, I was afraid of losing my partner",
        "03":"We did not have it at that time",
        "04":"I knew the man well",
        "05":"He didn't want to use it",
        "06":"I didn't want to use it",
        "07":"We use another contraceptive method",
        "08":"I thought there was no risk",
        "09":"We only practice oral sex",
        "10":"He had impotence problems with the condom",
        "11":"I was in love",
        "12":"Without condoms you feel more",
        "13":"We were drunk or had taken too much alcohol or other drugs",
        "14":"I had an uncontrolled desire",
        "15":"We were trying to have children",
        "16":"Other reasons",
        "99":"No Data"
    }
    
    information = switcher.get(str, "No response")
    return information

def reason_preservative_2(str):
    switcher = {
        "01":"We don't talk about it before having sex",
        "02":"It was very difficult for me to propose the condom, I was afraid of losing my partner",
        "03":"We did not have it at that time",
        "04":"I knew the woman well",
        "05":"She didn't want to use it",
        "06":"I didn't want to use it",
        "07":"We use another contraceptive method",
        "08":"I thought there was no risk",
        "09":"We only practice oral sex",
        "10":"I had impotence problems with the condom",
        "11":"I was in love",
        "12":"Without condoms you feel more",
        "13":"We were drunk or had taken too much alcohol or other drugs",
        "14":"I had an uncontrolled desire",
        "15":"We were trying to have children",
        "16":"Other reasons",
        "99":"No Data"
    }
    
    information = switcher.get(str, "No response")
    return information

def cheated(str):
    switcher = {
        "1":"Yes",
        "2":"Probably yes",
        "3":"Probably not",
        "4":"No",
        "5":"I don't know"
    }
    
    result = switcher.get(str, "No response")
    return result

def cheat_with(str):
    switcher = {
        "1":"Yes, with one man",
        "2":"Yes, with more than one",
        "3":"No",
        "4":"I don't remember"
    }
    
    result = switcher.get(str, "No response")
    return result


def attitude_preservatives(str):
    switcher = {
        "1":"We argue about the risks and then we stop using condoms",
        "2":"We both got tested for HIV and then stopped using condoms",
        "3":"We stopped using condoms, without discussing the risks or getting tested for HIV",
        "4":"We started using condoms",
        "5":"We continue to use condoms",
        "6":"We never use condoms",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    return result

def STD(str):
    switcher = {
        "0":"No",
        "1":"Yes"
    }
    
    result = switcher.get(str, "No response")
    return result

def last_STD(str):
    switcher = {
        "01":"Chlamydia infection",
        "02":"Gonorrhea",
        "03":"Syphilis",
        "04":"Trichomonas",
        "05":"Genital herpes",
        "06":"Genital ulcers or condyloma",
        "07":"Mycosis or fungus",
        "08":"Hepatitis B",
        "09":"Non-specific urethritis",
        "10":"Crabs or genital pediculosis",
        "11":"Other sexually transmitted disease",
        "99":"No Data",
        "1":"In the last 12 months",
        "2":"More than a year but less than five years",
        "3":"Five years ago or more",
        "9":"No data"
    }
    
    information = switcher.get(str, "No response")
    return information

def VIH(str):
    switcher = {
        "1":"Yes",
        "2":"No",
        "3":"I don't know, it is possible, it depends",
        "6":"No",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    
    return result

def VIH_testing(str):
    switcher = {
        "1":"Yes, once",
        "2":"Yes, more than once",
        "3":"No",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    
    return result

def VIH_time(str):
    switcher = {
        "1":"Less than 12 months",
        "2":"Between one and two years",
        "3":"Between two and five years",
        "4":"More than five years",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    
    return result

def VIH_reason(str):
    switcher = {
        "1":"I was pregnant",
        "2":"They asked me for it from an insurance company / for a mortgage / for a trip",
        "3":"I had had sex with a partner I didn't know and I didn't use a condom",
        "4":"The doctor told me",
        "5":"My partner asked me",
        "6":"Other",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    
    return result
def VIH_location(str):
    switcher = {
        "01":"During an admission to a hospital or clinic",
        "02":"At a family planning center",
        "03":"In the consultation of a specialist doctor (lung, gynecologist...)",
        "04":"At your GP's office/health center",
        "05":"In a private laboratory",
        "06":"In the outpatient clinic or emergency room of a hospital or clinic",
        "07":"In a center for sexually transmitted diseases or HIV/AIDS diagnosis",
        "08":"In a care center for people with drug problems",
        "09":"In other site",
        "99":"No Data"
    }
    
    result = switcher.get(str, "No response")
    return result

def VIH_risk(str):
    switcher = {
        "1":"High risk",
        "2":"Quite a risk",
        "3":"Low risk",
        "4":"No risk",
        "5":"I don't know",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    return result
    
def VIH_transmission(str):
    switcher = {
        "1":"Yes",
        "0":"No"
    }
    
    result = switcher.get(str, "No response")
    return result

def drug_risk(str):
    switcher = {
        "1":"High risk",
        "2":"Quite a risk",
        "3":"Low or no risk",
        "4":"Depends on whether or not they share syringes",
        "9":"No data"
    }
    result = switcher.get(str, "No response")
    return result

def VIH_pre_eff(str):
    switcher = {
        "1":"Very effective",
        "2":"Effective",
        "3":"Barely effective",
        "4":"Not effective",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    return result


def preservatives_opinion_0(str):
    switcher = {
        "1":"Totally agree",
        "2":"Quite agree",
        "3":"Somewhat agree",
        "4":"Do not agree",
        "9":"NDon't know"
    }
    
    result = switcher.get(str, "No response")
    return result

def preservatives_opinion_1(str):
    switcher = {
        "1":"High risk",
        "2":"Quite a risk",
        "3":"Low risk",
        "4":"No risk",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    return result

def preservatives_opinion_2(str):
    switcher = {
        "1":"No",
        "2":"Yes",
        "3":"Low risk",
        "4":"No risk",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    return result

def religion(str):
    switcher = {
        "1":"Catholic",
        "2":"Protestant",
        "3":"Muslim",
        "4":"Another religion",
        "5":"Has its own beliefs",
        "6":"Non-believer or agnostic",
        "7":"No answer"
    }
    
    result = switcher.get(str, "No response")
    return result

def religion_assistance(str):
    switcher = {
        "1":"More than one day a week",
        "2":"Once a week",
        "3":"Less than once a week",
        "4":"Never",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    return result

def size_municipy(str):
    switcher = {
        "1":"Up to 10,000 inhabitants",
        "2":"From 10001 to 50000 inhabitants",
        "3":"From 50001 to 500000 inhabitants",
        "4":"More than 500,000 inhabitants"
    }
    
    result = switcher.get(str, "No response")
    return result

def campany_12(str):
    switcher = {
        "1":"Spouse/Partner and no one else",
        "2":"Spouse/Partner and other",
        "3":"Parents or other relatives",
        "4":"Alone",
        "5":"Other people",
        "9":"No data"
    }
    
    result = switcher.get(str, "No response")
    return result