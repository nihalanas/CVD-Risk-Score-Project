import numpy as np

def cvd_female_raw(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_migraine, b_ra, b_renal, b_semi, b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town):
    survivor = np.array([
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0.988876402378082,
        0,
        0,
        0,
        0,
        0
    ])

    # The conditional arrays
    Iethrisk = np.array([0, 0, 0.28040314332995425, 0.56298994142075398, 0.29590000851116516, 0.07278537987798255, -0.17072135508857317, -0.39371043314874971, -0.32632495283530272, -0.17127056883241784])
    Ismoke = np.array([0, 0.13386833786546262, 0.56200858012438537, 0.66749593377502547, 0.84948177644830847])

    # Applying the fractional polynomial transforms (which includes scaling)
    dage = age
    dage = dage / 10
    age_1 = dage**(-2)
    age_2 = dage
    dbmi = bmi
    dbmi = dbmi / 10
    bmi_1 = dbmi**(-2)
    bmi_2 = dbmi**(-2) * np.log(dbmi)

    # Centring the continuous variables
    age_1 = age_1 - 0.053274843841791
    age_2 = age_2 - 4.332503318786621
    bmi_1 = bmi_1 - 0.154946178197861
    bmi_2 = bmi_2 - 0.144462317228317
    rati = rati - 3.476326465606690
    sbp = sbp - 123.13001251220703
    sbps5 = sbps5 - 9.002537727355957
    town = town - 0.392308831214905

    # Start of Sum
    a = 0

    # The conditional sums
    a += Iethrisk[ethrisk]
    a += Ismoke[smoke_cat]

    # Sum from continuous values
    a += age_1 * -8.1388109247726188
    a += age_2 * 0.79733376689699098
    a += bmi_1 * 0.29236092275460052
    a += bmi_2 * -4.1513300213837665
    a += rati * 0.15338035820802554
    a += sbp * 0.013131488407103424
    a += sbps5 * 0.0078894541014586095
    a += town * 0.077223790588590108

    # Sum from boolean values
    a += b_AF * 1.5923354969269663
    a += b_atypicalantipsy * 0.25237642070115557
    a += b_corticosteroids * 0.59520725304601851
    a += b_migraine * 0.301267260870345
    a += b_ra * 0.21364803435181942
    a += b_renal * 0.65194569493845833
    a += b_semi * 0.12555308058820178
    a += b_sle * 0.75880938654267693
    a += b_treatedhyp * 0.50931593683423004
    a += b_type1 * 1.7267977510537347
    a += b_type2 * 1.0688773244615468
    a += fh_cvd * 0.45445319020896213

    # Sum from interaction terms
    a += age_1 * (smoke_cat == 1) * -4.7057161785851891
    a += age_1 * (smoke_cat == 2) * -2.7430383403573337
    a += age_1 * (smoke_cat == 3) * -0.86608088829392182
    a += age_1 * (smoke_cat == 4) * 0.90241562369710648
    a += age_1 * b_AF * 19.938034889546561
    a += age_1 * b_corticosteroids * -0.98408045235936281
    a += age_1 * b_migraine * 1.7634979587872999
    a += age_1 * b_renal * -3.5874047731694114
    a += age_1 * b_sle * 19.690303738638292
    a += age_1 * b_treatedhyp * 11.872809733921812
    a += age_1 * b_type1 * -1.2444332714320747
    a += age_1 * b_type2 * 6.86523420000096
    a += age_1 * bmi_1 * 23.802623412141742
    a += age_1 * bmi_2 * -71.184947692087007
    a += age_1 * fh_cvd * 0.99467807940435127
    a += age_1 * sbp * 0.034131842338615485
    a += age_1 * town * -1.0301180802035639
    a += age_2 * (smoke_cat == 1) * -0.075589244643193026
    a += age_2 * (smoke_cat == 2) * -0.11951192874867074
    a += age_2 * (smoke_cat == 3) * -0.10366306397571923
    a += age_2 * (smoke_cat == 4) * -0.13991853591718389
    a += age_2 * b_AF * -0.076182651011162505
    a += age_2 * b_corticosteroids * -0.12005364946742472
    a += age_2 * b_migraine * -0.065586917898699859
    a += age_2 * b_renal * -0.22688873086442507
    a += age_2 * b_sle * 0.077347949679016273
    a += age_2 * b_treatedhyp * 0.00096857823588174436
    a += age_2 * b_type1 * -0.28724064624488949
    a += age_2 * b_type2 * -0.097112252590695489
    a += age_2 * bmi_1 * 0.52369958933664429
    a += age_2 * bmi_2 * 0.045744190122323759
    a += age_2 * fh_cvd * -0.076885051698423038
    a += age_2 * sbp * -0.0015082501423272358
    a += age_2 * town * -0.031593414674962329

    # Calculate the score itself
    score = 100.0 * (1 - np.power(survivor[surv], np.exp(a)))

    return score


def cvd_male_raw(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_impotence2, b_migraine, b_ra, b_renal, b_semi,
                 b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town):
    # The conditional arrays
    survivor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.977268040180206, 0, 0, 0, 0, 0]

    Iethrisk = [0, 0, 0.27719248760308279, 0.47446360714931268, 0.52961729919689371, 0.035100159186299017,
                -0.35807899669327919, -0.4005648523216514, -0.41522792889830173, -0.26321348134749967]

    Ismoke = [0, 0.19128222863388983, 0.55241588192645552, 0.63835053027506072, 0.78983819881858019]

    # Applying the fractional polynomial transforms
    # (which includes scaling)

    dage = age
    dage = dage / 10
    age_1 = np.power(dage, -1)
    age_2 = np.power(dage, 3)
    dbmi = bmi
    dbmi = dbmi / 10
    bmi_2 = np.power(dbmi, -2) * np.log(dbmi)
    bmi_1 = np.power(dbmi, -2)

    # Centring the continuous variables

    age_1 = age_1 - 0.234766781330109
    age_2 = age_2 - 77.284080505371094
    bmi_1 = bmi_1 - 0.149176135659218
    bmi_2 = bmi_2 - 0.141913309693336
    rati = rati - 4.300998687744141
    sbp = sbp - 128.571578979492190
    sbps5 = sbps5 - 8.756621360778809
    town = town - 0.526304900646210

    # Start of Sum
    a = 0

    # The conditional sums

    a += Iethrisk[ethrisk]
    a += Ismoke[smoke_cat]

    # Sum from continuous values

    a += age_1 * -17.8397816660055750000000000
    a += age_2 * 0.0022964880605765492000000
    a += bmi_1 * 2.4562776660536358000000000
    a += bmi_2 * -8.3011122314711354000000000
    a += rati * 0.1734019685632711100000000
    a += sbp * 0.0129101265425533050000000
    a += sbps5 * 0.0102519142912904560000000
    a += town * 0.0332682012772872950000000

    # Sum from boolean values

    a += b_AF * 0.8820923692805465700000000
    a += b_atypicalantipsy * 0.1304687985517351300000000
    a += b_corticosteroids * 0.4548539975044554300000000
    a += b_impotence2 * 0.2225185908670538300000000
    a += b_migraine * 0.2558417807415991300000000
    a += b_ra * 0.2097065801395656700000000
    a += b_renal * 0.7185326128827438400000000
    a += b_semi * 0.1213303988204716400000000
    a += b_sle * 0.4401572174457522000000000
    a += b_treatedhyp * 0.5165987108269547400000000
    a += b_type1 * 1.2343425521675175000000000
    a += b_type2 * 0.8594207143093222100000000
    a += fh_cvd * 0.5405546900939015600000000

    # Sum from interaction terms

    a += age_1 * (smoke_cat == 1) * -0.2101113393351634600000000
    a += age_1 * (smoke_cat == 2) * 0.7526867644750319100000000
    a += age_1 * (smoke_cat == 3) * 0.9931588755640579100000000
    a += age_1 * (smoke_cat == 4) * 2.1331163414389076000000000
    a += age_1 * b_AF * 3.4896675530623207000000000
    a += age_1 * b_corticosteroids * 1.1708133653489108000000000
    a += age_1 * b_impotence2 * -1.5064009857454310000000000
    a += age_1 * b_migraine * 2.3491159871402441000000000
    a += age_1 * b_renal * -0.5065671632722369400000000
    a += age_1 * b_treatedhyp * 6.5114581098532671000000000
    a += age_1 * b_type1 * 5.3379864878006531000000000
    a += age_1 * b_type2 * 3.5461356261000910000000000
    a += age_1 * bmi_1 * -10.6342645818781000000000000
    a += age_1 * bmi_2 * 35.2008260509874000000000000
    a += age_1 * fh_cvd * 0.3600910380734261600000000
    a += age_1 * sbp * -0.0134364516987222440000000
    a += age_1 * town * -0.0552398380916210060000000
    a += age_2 * (smoke_cat == 1) * -0.0000960140102431733920000
    a += age_2 * (smoke_cat == 2) * -0.0007680722878363999100000
    a += age_2 * (smoke_cat == 3) * -0.0004299111000048944600000
    a += age_2 * (smoke_cat == 4) * -0.0001519287101292208500000
    a += age_2 * b_AF * -0.0003310887434857609500000
    a += age_2 * b_corticosteroids * -0.0001557129222197479600000
    a += age_2 * b_impotence2 * -0.0005299721410128503000000
    a += age_2 * b_migraine * -0.0002017177481402563400000
    a += age_2 * b_renal * -0.0000112657735361305300000
    a += age_2 * b_treatedhyp * 0.0001183621885788562700000
    a += age_2 * b_type1 * 0.0000624990960985706620000
    a += age_2 * b_type2 * 0.0000470970792765428300000
    a += age_2 * bmi_1 * -0.0001094872683167021200000
    a += age_2 * bmi_2 * 0.0002233876368502521800000
    a += age_2 * fh_cvd * -0.0000067518688021490131000
    a += age_2 * sbp * 0.0000008444307651925531300
    a += age_2 * town * -0.0000363190736906057940000

    # Calculate the score itself
    score = 100.0 * (1 - np.power(survivor[surv], np.exp(a)))

    return score



# Example input values (replace these with your actual values)
age = 45
gender = 'female'  # or 'female'
b_AF = 0
b_atypicalantipsy = 0
b_corticosteroids = 0
b_impotence2 = 0
b_migraine = 1
b_ra = 0
b_renal = 0
b_semi = 0
b_sle = 0
b_treatedhyp = 0
b_type1 = 0
b_type2 = 1
bmi = 25
ethrisk = 0
fh_cvd = 1
rati = 5
sbp = 150
sbps5 = 0
smoke_cat = 3
surv = 10
town = 0

def calculate_cvd_score(age, gender, b_AF, b_atypicalantipsy, b_corticosteroids, b_impotence2, b_migraine, b_ra, b_renal, b_semi,
                        b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town):
    if gender == 'male':
        return cvd_male_raw(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_impotence2, b_migraine, b_ra, b_renal, b_semi,
                            b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town)
    elif gender == 'female':
        return cvd_female_raw(age, b_AF, b_atypicalantipsy, b_corticosteroids, b_migraine, b_ra, b_renal, b_semi, b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town)
    else:
        raise ValueError("Invalid gender. Please specify 'male' or 'female'.")

# Call the function and print the result
result = calculate_cvd_score(age, gender, b_AF, b_atypicalantipsy, b_corticosteroids, b_impotence2, b_migraine, b_ra, b_renal, b_semi,
                              b_sle, b_treatedhyp, b_type1, b_type2, bmi, ethrisk, fh_cvd, rati, sbp, sbps5, smoke_cat, surv, town)

print("Risk Score:", result)
