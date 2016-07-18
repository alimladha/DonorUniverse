'''
This file will be used to calculate anything that has to do with logistics

THIS CODE IS USED TO ACCESS DATACLIPS FILES IF THE SEPARATE DATA APP SHUTS DOWN
from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://id.heroku.com/login')
email = browser.find_element_by_id("email")
password = browser.find_element_by_id("password")
loginButton = browser.find_element_by_name("commit")

email.send_keys("alim@openbiome.org")
password.send_keys("Wolfpuck1!")
loginButton.click()
browser.get('https://dataclips.heroku.com/xuxyyihpajhswmajwsfgewefelws-donor-stats')
time.sleep(5)
browser.get('https://dataclips.heroku.com/xuxyyihpajhswmajwsfgewefelws-donor-stats.json')
elem = browser.find_element_by_tag_name("pre")
content = elem.text
print content
'''

import urllib2
import json
import sets
import ast
from PyQt4 import QtCore, QtGui
import datetime
import math
Statuses = sets.Set()
MaterialTypes = sets.Set()



def loadLogistics(donorList):
    '''
    loads logistic data for donors from the json file given by loadPooAppData()
    '''
    if not donorList:
        return
    data = loadPooAppData()
    for donor in donorList:
        for logisticDict in data:
            if int(logisticDict['donor_number'])==donor.donorID:
                materialAvailable = str(logisticDict['inventory'])
                materialAvailable = materialAvailable.replace("null", "None")
                donor.materialAvailable = ast.literal_eval(materialAvailable)
                reformatMaterialDict(donor)
                donor.processingStatus = logisticDict['eligibility_state']
                global Statuses
                Statuses.add(str(logisticDict['eligibility_state']))
                holdList = logisticDict['hold_types']
                holdList = str(holdList)
                holdList = holdList[2:-2]
                holdList = holdList.split(",")
                donorShippingHold = False
                for hold in holdList:
                    hold = hold.strip()
                    if hold == 'shipping':
                        donor.shippingStatus = 'Hold'
                        donorShippingHold = True
                if not donorShippingHold:
                    donor.shippingStatus = 'Available'
                donor.productionRate = logisticDict['average_grams_per_week']
                
    
def loadPooAppData():
    '''
    loads the data from the poo app and returns it in json format
    '''
    username = 'sQWhBrIJ43FLmNSqkIN7beX8OumIp85V'
    password = 'ovQR8JY0UwRtG7k4W6QzwnoAuSsANnun'
    theurl = 'https://ob-donor-stats.herokuapp.com/'
    passman = urllib2.HTTPPasswordMgrWithDefaultRealm()
    passman.add_password(None, theurl, username, password)
    authhandler = urllib2.HTTPBasicAuthHandler(passman)
    opener = urllib2.build_opener(authhandler)
    urllib2.install_opener(opener)
    pagehandle = urllib2.urlopen(theurl)
    returnJson = pagehandle.read()
    parsed_json = json.loads(returnJson)
    return parsed_json

'''
Data check test:
testData = loadPooAppData()
testDonor = testData[0]
testDict = testDonor['inventory']
testDict = ast.literal_eval(str(testDict))
print testDict
newDict = {'Quarantined': {}, 'Available': {}}
for item in testDict:
    qState = item['quarantine_state']
    count = item['count']
    count_type = item['count_type']
    product = item['product']
    if qState == 'available':
        curDict = newDict['Available']
    else:
        curDict = newDict['Quarantined']
    curDict[product] = (count, count_type)
    
newDictString = {}
for key in newDict.keys():
    curList = []
    for item in newDict[key].keys():
        curItemVal = newDict[key][item]
        curItemCount = curItemVal[0]
        unitType = curItemVal[1]
        itemString = item + ": " + str(curItemCount) + " " + unitType + "s"
        curList.append
    newDictString[key] = curList
        
        

print tabulate.tabulate(newDictString, headers="keys")
'''
def reformatMaterialDict(donor):
    '''
    takes list form of inventory and turns it into a dictionary format with quarantined and
    available as the top level keys
    '''
    if isinstance(donor.materialAvailable, list):
        newDict = {'Quarantined': {}, 'Available': {}}
        for item in donor.materialAvailable:
            qState = item['quarantine_state']
            count = item['count']
            count_type = item['count_type']
            product = item['product_name']
            global MaterialTypes
            MaterialTypes.add(product)
            if qState == 'available':
                curDict = newDict['Available']
            else:
                curDict = newDict['Quarantined']
            curDict[product] = (count, count_type)
        donor.materialAvailable = newDict
        
        
def logisticSearch(answers, donors, form):
    '''
    given a dictionary of logistics answers, a list of donors, and the appropriate form:
    this function is the high level logistic search function used in DonorUniverseGUI
    '''
    unitSearchBool = answers[form.unitSearchCheck]
    dateSearchBool = answers[form.dateSearchCheck]
    # if unitSearchBool and dateSearchBool:
    # raiseBothError(form)
    # return
    if not(unitSearchBool) and not(dateSearchBool):
        raiseNoneError(form)
        return
    if not getMaterialAnswers(answers, form):
        raiseNoMaterialSelected(form)
        return
    materialWanted = getMaterialAnswers(answers, form)
    if len(materialWanted) != len(set(materialWanted)):
        raiseDuplicateMaterial(form)
        return
    donors_valid = []
    for donor in donors:
        if donor.productionRate or donor.productionRate >0 :
            donors_valid.append(donor)
        
    if dateSearchBool and not unitSearchBool:
        results = dateSearch(answers, donors_valid, form)
        displayDateSearch(results, form)
    
    if unitSearchBool and not dateSearchBool:
        results = unitSearch(answers, donors_valid, form)
        displayUnitSearch(results, form)
    
    if unitSearchBool and dateSearchBool:
        results = unitSearch(answers, donors_valid, form)
        new_results = cutDownResults(answers, results, form)
        if not new_results:
            error = QtGui.QErrorMessage()
            error.showMessage(QtCore.QString("No Donors Found"))
            error.exec_()
            return
        displayUnitSearch(new_results, form)
        
def displayDateSearch(results, form):
    '''
    displays results from date search to the given form
    '''
    if not results:
        resetResultsTable(form.tableWidget_2)
        return
    table = form.tableWidget_2
    numCols = int(table.columnCount())
    while numCols > 0:
        numCols = numCols-1
        table.removeColumn(numCols)
    headers = ["Donor"]
    numCols = len(results[0][1])+1
    for key in results[0][1].keys():
        headers.append(key)
    table.setRowCount(len(results))
    for i in xrange(numCols):
        table.insertColumn(i)
        item = QtGui.QTableWidgetItem()
        if not headers[i] == "Donor":
            item.setText("Estimated #: " + headers[i] + " (% available now)")
        else:
            item.setText(headers[i])
        table.setHorizontalHeaderItem(i, item)
        for j in xrange(len(results)):
            if headers[i] == "Donor":
                widgetItem = QtGui.QTableWidgetItem()
                widgetItem.setSizeHint(QtCore.QSize(50,10))
                widgetItem.setData(QtCore.Qt.DisplayRole, results[j][0].getDonorID())
                table.setItem(j, i, widgetItem)
            else:
                donorDict = results[j][1]
                if donorDict.has_key(headers[i]):
                    widgetItem = QtGui.QTableWidgetItem()
                    units = donorDict[headers[i]][0]
                    percentAvail = donorDict[headers[i]][1]
                    displayString = '%d (%d %%)' %(units,percentAvail)
                    widgetItem.setText(displayString)
                    table.setItem(j,i,widgetItem)
                else:
                    continue
    table.resizeColumnsToContents()
    
def displayUnitSearch(results, form):
    '''
    displays unit search results to the given form
    '''
    table = form.tableWidget_2
    if not results:
        resetResultsTable(table)
        return
    numCols = int(table.columnCount())
    while numCols > 0:
        numCols = numCols-1
        table.removeColumn(numCols)
    headers = ["Donor", "Estimated Date of Fulfillment"]
    numCols = 2
    table.setRowCount(len(results))
    for i in xrange(numCols):
        table.insertColumn(i)
        item = QtGui.QTableWidgetItem()
        item.setText(QtCore.QString(headers[i]))
        table.setHorizontalHeaderItem(i, item)
        for j in xrange(len(results)):
            if i == 0:
                widgetItem = QtGui.QTableWidgetItem()
                widgetItem.setSizeHint(QtCore.QSize(30,10))
                widgetItem.setData(QtCore.Qt.DisplayRole, results[j][0].getDonorID())
            if i == 1:
                widgetItem = QtGui.QTableWidgetItem()
                widgetItem.setText(str(results[j][1]))
            table.setItem(j,i, widgetItem)
    table.resizeColumnsToContents()
    
def dateSearch(answers, donors, form):
    '''
    performs a date search given answers, a list fo donors, and the appropriate form
    returns tuple of donors, with estimated material dictionaries as the second value
    '''
    futureDate = answers[form.dateEdit]
    efficiency = answers[form.efficiencySpin]/100.0
    today = datetime.date.today()
    time = (futureDate - today).days/7
    if time<0:
        error =  QtGui.QErrorMessage()
        error.showMessage(QtCore.QString("Cannot Input Previous Date"))
        error.exec_()
        return
    
    requestedMaterials = getMaterialAnswers(answers, form)
    donorResults = []
    for donor in donors:
        prodRatePerMaterial = donor.productionRate * efficiency /float(len(requestedMaterials))
        currentMaterials = donor.materialAvailable
        totalMaterialDict = {}
        for material in requestedMaterials:
            totalCur = getCurrentUnitsByMaterial(currentMaterials, material)
            curAvail = totalCur[1]
            totalCur = totalCur[0]            
            totalNewWeight = time*prodRatePerMaterial
            numNewUnits = totalNewWeight# / weights[material]#
            units = totalCur + numNewUnits
            if units ==0:
                percentAvailableNow = 100
            else:
                percentAvailableNow = curAvail/units*100
            totalMaterialDict[material] = (units, percentAvailableNow)
        donorResults.append((donor, totalMaterialDict))
    return donorResults
    
    
def unitSearch(answers, donors, form):
    '''
    performs unit search given answers, list of donors, and appropriate form
    returns list of tuples with donor as first value and estimated complete date as second value
    '''
    requestedMaterials = getMaterialAnswers(answers, form)
    requestedUnits = []
    efficiency = answers[form.efficiencySpin]/100.0
    spinBoxes = [form.unitsSpin_Log1, form.unitsSpin_Log2, form.unitsSpin_Log3, form.unitsSpin_Log4]
    for spinBox in spinBoxes:
        requestedUnits.append(answers[spinBox])
    donorResults = []
    for donor in donors:
        currentMaterials = donor.materialAvailable
        totalWeight = 0
        for i in xrange(len(requestedMaterials)):
            material = requestedMaterials[i]
            totalCur = getCurrentUnitsByMaterial(currentMaterials, material)
            curAvail = totalCur[1]
            totalCur = totalCur[0]
            newUnitsNeeded = requestedUnits[i] - totalCur
            if newUnitsNeeded>0:
                newWeight = newUnitsNeeded #*weights[material]
                totalWeight = totalWeight + newWeight
        productionRate = donor.productionRate *efficiency
        daysRequired = totalWeight/productionRate * 7
        today = datetime.date.today()
        completeDate = today + datetime.timedelta(days = int(math.ceil(daysRequired)))
        donorResults.append((donor, completeDate))

    return donorResults
def raiseBothError(form):
    '''
    raises error if both date and unit are checked (old function that is no longer used)
    '''
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString("Can't Perform Both Date and Unit Search"))
    error.exec_()
    return

def raiseNoneError(form):
    '''
    error raised when no searches are selected
    '''
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString("No Searches Selected"))
    error.exec_()
    return

def getMaterialAnswers(answers, form):
    '''
    gets material combo answers given the answers dictionary and returns them as a list
    '''
    materialCombos = [form.materialTypeCombo_Log1, form.materialTypeCombo_Log2, form.materialTypeCombo_Log3, form.materialTypeCombo_Log4]
    requestedMaterials = []
    for combo in materialCombos:
        response = answers[combo]
        if response:
            requestedMaterials.append(response)
    return requestedMaterials

def getCurrentUnitsByMaterial(currentMaterials, material):
    '''
    gets total current amount of material available
    returns list with first value as the total, second value is current amount available
    '''
    curAvailableDict = currentMaterials["Available"]
    if curAvailableDict.has_key(material):
        curAvailable = curAvailableDict[material][0]
    else:
        curAvailable = 0
    curQuarDict = currentMaterials['Quarantined']
    if curQuarDict.has_key(material):
        curQuar = curQuarDict[material][0]
    else:
        curQuar = 0
    totalCur = curQuar + curAvailable
    return [totalCur, curAvailable]

def cutDownResults(answers, results, form):
    '''
    cuts down results if both date and unit search are selected so the cutoff date is reflected 
    in the results
    '''
    dateRequired = answers[form.dateEdit]
    donors_valid = []
    for donorTuple in results:
        dateComplete = donorTuple[1]
        if dateComplete <= dateRequired:
            donors_valid.append(donorTuple)
        else:
            continue
    return donors_valid
    

def raiseNoMaterialSelected(form):
    '''
    if no material is selected, this error is raised
    '''
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString("No Material Selected"))
    error.exec_()
    return

def raiseDuplicateMaterial(form):
    '''
    if two of the same material are selected, this error is raised
    '''
    error = QtGui.QErrorMessage()
    error.showMessage(QtCore.QString("No Duplicate Materials Allowed"))
    error.exec_()
    return
    
def resetResultsTable(table):
    '''
    resets table to one column with header = "Results"
    '''
    numCols = int(table.columnCount())
    numRows = int(table.rowCount())
    while numCols > 1:
        table.removeColumn(numCols-1)
        numCols = numCols-1
    while numRows > 0:
        table.removeRow(numRows-1)
        numRows = numRows - 1
    item = QtGui.QTableWidgetItem()
    item.setText(QtCore.QString("Results"))
    table.setHorizontalHeaderItem(0, item)
    
    