##this file will be used to calculate anything that has to do with logistics

func unitsAvailableNow(donor) ##function returns how many units are available now
return donor.materialAvailable



func unitsAvailable(DonorID, date) ##function returns how many units will be available at a future date (estimated)
 - Must be future date
 time = calculate number of weeks between today and input date
 new product = time*donor.productionRate
 total product = materialAvailable + new product


func willBeAvailable(units, DonorID, date) ##function returns if a certain number of units will be available date (estimated)
-must be future date
 time = calculate number of weeks between today and input date
 new product = time*donor.productionRate
 total product = materialAvailable + new product
 if totalProduct>units
 return true
 else
 return false

func dateAvailable(units, DonorID) ##function returns date a certain number of units will be available (estimated)
new units = untis - donor.materialAvailable
time = new units / donor.productionRate
date = time + today
return date
