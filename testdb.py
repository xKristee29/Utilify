# Import required modules
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
		"https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]



# Assign credentials ann path of style sheet
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("UtilifyDB").sheet1

data = sheet.get_all_records()

# Inserting data
insertRow = [6, "Ceva", "Purple"]
sheet.insert_row(insertRow,2)
print("\nAll Records after inserting new row : ")
pprint(data)


'''
# Deleting data
sheet.delete_row(2)
print("\nAll Records after deleting row 7 : ")
pprint(data)



# Update a cell
sheet.update_cell(5, 2, "Nitin Das")
print("\nAll Records after updating cell (5,2) : ")
pprint(data)

'''

# Display no. of rows, columns
# and no. of rows having content
numRows = sheet.row_count
numCol = sheet.col_count
print("Number of Rows : ", numRows)
print("Number of Columns : ", numCol)
print("Number of Rows having content : ", len(data))
