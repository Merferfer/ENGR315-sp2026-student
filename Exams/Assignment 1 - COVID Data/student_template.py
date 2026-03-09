import sys


def parse_nyt_data(file_path=''):
    """
    Parse the NYT covid database and return a list of tuples. Each tuple describes one entry in the source data set.
    Date: the day on which the record was taken in YYYY-MM-DD format
    County: the county name within the State
    State: the US state for the entry
    Cases: the cumulative number of COVID-19 cases reported in that locality
    Deaths: the cumulative number of COVID-19 death in the locality

    :param file_path: Path to data file
    :return: A List of tuples containing (date,county, state, fips, cases, deaths) information
    """
    # data point list
    data=[]

    # open the NYT file path
    try:
        fin = open(file_path)
    except FileNotFoundError:
        print('File ', file_path, ' not found. Exiting!')
        sys.exit(-1)

    # get rid of the headers
    fin.readline()

    # while not done parsing file
    done = False

    # loop and read file
    while not done:
        line = fin.readline()

        if line == '':
            done = True
            continue

        # format is date,county,state,fips,cases,deaths
        (date,county, state, fips, cases, deaths) = line.rstrip().split(",")

        # clean up the data to remove empty entries
        if cases=='':
            cases=0
        if deaths=='':
            deaths=0

        # convert elements into ints
        try:
            entry = (date,county,state, fips, int(cases), int(deaths))
        except ValueError:
            print('Invalid parse of ', entry)

        # place entries as tuple into list
        data.append(entry)


    return data

def first_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    :return:
    """
    # your code here
    RockinghamFirstCase = (None,None,None,None,None,None)
    HarrisonburgFirstCase = (None,None,None,None,None,None)
    for entry in data:
        if(RockinghamFirstCase[0] != None and HarrisonburgFirstCase[0] != None):
            # print("break")
            break
        elif(entry[1] == "Harrisonburg city" and HarrisonburgFirstCase[0] == None):
            # print(entry)
            HarrisonburgFirstCase = entry
        elif(entry[1] == "Rockingham" and entry[2] == "Virginia" and RockinghamFirstCase[0] == None):
            # print(entry)
            RockinghamFirstCase = entry

    print("The first positive COVID case in Rockingham County was ", RockinghamFirstCase[0])
    print("The first positive COVID case in Harrisonburg City was ", HarrisonburgFirstCase[0])
    return

def second_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    :return:
    """
    # your code here
    maxNewDailyCasesHarrisonburg = 0
    maxNewDailyCasesRockingham = 0
    
    RockinghamSpike = (None,None,None,None,None,None)
    HarrisonburgSpike = (None,None,None,None,None,None)
    
    prevCaseHarrisonburg = 0
    prevCaseRockingham = 0

    for entry in data:

      if(entry[1] == "Harrisonburg city"):
        if((entry[4] - prevCaseHarrisonburg) > maxNewDailyCasesHarrisonburg):
          maxNewDailyCasesHarrisonburg = entry[4] - prevCaseHarrisonburg
          HarrisonburgSpike = entry

        prevCaseHarrisonburg = entry[4]

      elif(entry[1] == "Rockingham" and entry[2] == "Virginia"):
        if((entry[4] - prevCaseRockingham) > maxNewDailyCasesRockingham):
          maxNewDailyCasesRockingham = entry[4] - prevCaseRockingham
          RockinghamSpike = entry

        prevCaseRockingham = entry[4]

    print("The day in Harrisonburg City with the greatest number of new daily cases was ",HarrisonburgSpike[0]," with an increase of ",maxNewDailyCasesHarrisonburg," cases.")
    print("The day in Rockingham County with the greatest number of new daily cases was ",RockinghamSpike[0]," with an increase of ",maxNewDailyCasesRockingham," cases.")
    return

def third_question(data):
    """
    # Write code to address the following question: Use print() to display your responses.
    # What was the worst 7-day period in either the city and county for new COVID cases?
    # This is the 7-day period where the number of new cases was maximal.
    :return:
    """
    # your code here
    HarrisonburgWeek = []
    HarrisonburgWorstWeek = []
    HarrisonburgWeekRecord = 0
    RockinghamWeek = []
    RockinghamWorstWeek = []
    RockinghamWeekRecord = 0

    for entry in data:
      if(entry[1] == "Harrisonburg city"):
        HarrisonburgWeek.append(entry)

        if(len(HarrisonburgWeek) <= 7):
          continue

        HarrisonburgWeek.pop(0)

        if((HarrisonburgWeek[6][4] - HarrisonburgWeek[0][4]) > HarrisonburgWeekRecord):
          HarrisonburgWeekRecord = HarrisonburgWeek[6][4] - HarrisonburgWeek[0][4]
          HarrisonburgWorstWeek = HarrisonburgWeek

      elif(entry[1] == "Rockingham" and entry[2] == "Virginia"):
        RockinghamWeek.append(entry)

        if(len(RockinghamWeek) <= 7):
          continue

        RockinghamWeek.pop(0)

        if((RockinghamWeek[6][4] - RockinghamWeek[0][4]) > RockinghamWeekRecord):
          RockinghamWeekRecord = RockinghamWeek[6][4] - RockinghamWeek[0][4]
          RockinghamWorstWeek = RockinghamWeek


    print("The worst week in Harrisonburg City started on ",HarrisonburgWorstWeek[0][0]," and had a total new case number of ",HarrisonburgWeekRecord)
    print("The worst week in Rockingham County started on ",RockinghamWorstWeek[0][0]," and had a total new case number of ",RockinghamWeekRecord)
    return

if __name__ == "__main__":
    data = parse_nyt_data('./Exams/Assignment 1 - COVID Data/us-counties.csv')

    # for (date,county, state, fips, cases, deaths) in data:
    #     print('On ', date, ' in ', county, ' ', state, ' there were ', cases, ' cases and ', deaths, ' deaths')


    # write code to address the following question: Use print() to display your responses.
    # When was the first positive COVID case in Rockingham County?
    # When was the first positive COVID case in Harrisonburg?
    first_question(data)


    # write code to address the following question: Use print() to display your responses.
    # What day was the greatest number of new daily cases recorded in Harrisonburg?
    # What day was the greatest number of new daily cases recorded in Rockingham County?
    second_question(data)

    # write code to address the following question: Use print() to display your responses.
    # What was the worst seven day period in Harrisonburg for new COVID cases (in terms of absolute number of cases)?
    # What was the worst seven day period in Rockingham County for new COVID cases (in terms of absolute number of cases)?
    third_question(data)


