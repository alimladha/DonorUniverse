array: import Study types into array
import donor profiles

isSafe(donorID, [studyType])
look up donor ID in list of donors
if donor.unsafeStudy contains studyType, return false
else return true

getDonors([studyType])
create empty list of donors
for each donor in list:
	if donor.unsafeStudy doesn’t contain study type
		add to list
return list
