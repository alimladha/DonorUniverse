from oauth2client.service_account import ServiceAccountCredentials
import gspread
import pandas as pd
from StringIO import StringIO
from profile import Donor

def loadTable():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    gc = gspread.authorize(credentials)
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/197EsVg-p8xZkxfdwpf1wgjhKaJQtrt8lDiDegwOuap0/edit?ts=577188f8#gid=58702749')
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
    table = loadTable()
    donorNumList = []
    infoArrays = []
    for row in table.itertuples():
        donorNumList.append(row.Donor_Number)
        infoDict = {#'Safety Rating': row.SafetyRating#, 
                    'Group': row.Group, 'BMI': row.BMI, 'WC': row.WC,
                    'Age': row.Age_at_enrollment, 'Gender': row.Sex, 'Abnormal Lab Results': row.Abnormal_Lab_Results, 
                    'Clinical Notes': row.Clinical_Notes, 'Allergies': row.Allergies, 'Diet': row.Diet,
                    'Other' :row.Other}
        infoArrays.append(infoDict)
        
    ##must add safety rating, and clinical studies from ryan's google doc here
    
        
    donorList=[]
    for donorNum, donorInfo in zip(donorNumList,infoArrays):
        newDonor = Donor(donorNum)
        newDonor.addInfo(donorInfo)
        donorList.append(newDonor)
        
    return donorList
loadDonorData()