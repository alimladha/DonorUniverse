from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd
from StringIO import StringIO
from profile import Donor
import sets
import file_setter

def loadTable(url):
    '''
    loads google spreadsheet table from a google spreadsheet url
    returns table until one of the rows in the first column is null
    '''
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(file_setter.resource_path('credentials.json'), scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url(url)
    emr = sheet.get_worksheet(0)
    csvEmr = emr.export('csv')
    TESTDATA = StringIO(csvEmr)
    table = pd.read_csv(TESTDATA)   
    ##get index of table that isn't null
    index = 1
    for index, row in table.iterrows():
        if pd.isnull(row[0]):
            break
        index = index+1
    table = table[:index]
    return table

def loadDonorData():
    '''
    loads the donor data from google drive
    returns all screening groups as the first return value in the return list
    returns list of loaded donors as the second value in the return list
    '''
    table = loadTable('https://docs.google.com/spreadsheets/d/197EsVg-p8xZkxfdwpf1wgjhKaJQtrt8lDiDegwOuap0/edit?ts=577188f8#gid=58702749')
    donorNumList = []
    infoArrays = []
    screeningGroups = sets.Set()
    for row in table.itertuples():
        donorNumList.append(row.Donor_Number)
        infoDict = {#'Safety Rating': row.SafetyRating#, 
                    'Group': row.Group, 'BMI': row.BMI, 'WC': row.WC,
                    'Age': row.Age_at_enrollment, 'Gender': row.Sex, 'Abnormal Lab Results': row.Abnormal_Lab_Results, 
                    'Clinical Notes': row.Clinical_Notes, 'Allergies': row.Allergies, 'Diet': row.Diet,
                    'Other' :row.Other}
        if not pd.isnull(row.Group):
            screeningGroups.add(str(row.Group))
        infoArrays.append(infoDict)
        
    ##must add safety rating, and clinical studies from ryan's google doc here
    table_2 = loadTable('https://docs.google.com/spreadsheets/d/1YcwwbZD7UItz-2KY53QH8WvNYMLt1txObI_U1_a-MxQ/edit?ts=5773ecc8#gid=0')
    for row in table_2.itertuples():
        for donor, donorInfoDict in zip(donorNumList, infoArrays):
            if row.Donor == donor:
                donorInfoDict['Safety Rating'] = row.Safety_Rating
                donorInfoDict['Current Studies'] = row.Current_Studies
            
        
    donorList=[]
    for donorNum, donorInfo in zip(donorNumList,infoArrays):
        newDonor = Donor(donorNum)
        newDonor.addInfo(donorInfo)
        donorList.append(newDonor)
        
    return [screeningGroups, donorList]


