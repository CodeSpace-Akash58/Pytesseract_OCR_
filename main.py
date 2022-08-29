
import os,sys
import re
import pytesseract  
import json
import pandas as pd

db = {}        #dict database To Store all record

class People_record:

    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

        
    @classmethod
    def displayData(cls):              #To display all record in database

        with open(os.path.join(sys.path[0],'record.json'),'w') as fp:   #write json file
            json.dump(db,fp)

        with open(os.path.join(sys.path[0],'record.json'),'r') as fp:   #Read json file
            json_obj    =   json.load(fp)
        
        # print(json_obj)                       #print json object

        for k,v in db.items():           #iterates Key and values of dict
            print(k,':',v)

        # df = pd.DataFrame(db)
        # df.fillna(0)
        # print(df)

    def aadharData(self):

        dir_path =r'C:\Users\Akash_HP\Pythaneer\ClassProjects\Pytesseract\People_data\Aadhar_data'
        files = os.listdir(dir_path)

        self.aadhar_list = []
        # aadhar_dict = {}  #dict to store aadhar data
        for img in files:
            
            img_path = dir_path + '\\' + img                    #Extracting each image file path
            # print(img_path) 

            aadhar_text = pytesseract.image_to_string(img_path)      #extract text from each image
             
            aadhar_pattern = re.findall(r'\d{4} \d{4} \d{4}',aadhar_text)  #check match found on pattern
            for aadhar_no in aadhar_pattern:
                self.aadhar_list.append(aadhar_no)
            
        print('Aadhar data extracted successfully..\n')
        print('Display aadhar data:\n\n',self.aadhar_list)    
        db['aadhar_info'] = self.aadhar_list
        print('\nAadhar data added successfully to database record')

    def panData(self):

        dir_path =r'C:\Users\Akash_HP\Pythaneer\ClassProjects\Pytesseract\People_data\pan_data'
        files = os.listdir(dir_path)

        self.pan_list = []        # list to store pan data
        for img in files:
            img_path = dir_path + '\\' + img
            # print(img_path) 

            pan_text = pytesseract.image_to_string(img_path)
            # print(text)
            
            pan_pattern = re.findall(r'[A-Z]{5}\d{4}[A-Z]',pan_text)
            for pan_no in pan_pattern:
                self.pan_list.append(pan_no)
                
        print('Pancard data extracted successfully..\n')
        print('Display pancard data:\n\n',self.pan_list)    
        db['pan_info'] = self.pan_list
        print('\nPancard data added successfully to database record')
     
    def drLicenceData(self):

        dir_path =r'C:\Users\Akash_HP\Pythaneer\ClassProjects\Pytesseract\People_data\driving_licence'
        files = os.listdir(dir_path)

        self.dl_list    =   []        # list to store drlicence data
        for img in files:
            img_path = dir_path + '\\' + img
            # print(img_path) 

            dl_text = pytesseract.image_to_string(img_path)
            # print(text)
            
            dl_pattern = re.findall(r'[A-Z0-9]{2,10}\W[0-9]{10,15}',dl_text)
            for dl_no in dl_pattern:
                self.dl_list.append(dl_no)
                
        print('Driving licence data extracted successfully..\n')
        print('Display Driving licence data:\n\n',self.dl_list)    
        db['licence_info'] = self.dl_list
        print('\nDriving licence data added successfully to database record')

    def voterData(self):
        
        dir_path =r'C:\Users\Akash_HP\Pythaneer\ClassProjects\Pytesseract\People_data\voter_card'
        files = os.listdir(dir_path)

        self.voter_list    =   []
        for img in files:
            imgpath = dir_path + '\\' + img
            # print(imgpath)

            voter_text = pytesseract.image_to_string(imgpath)
            # print(voter_text)

            voter_pattern = re.findall(r'[A-Z]{3,4}[0-9]{6,10}',voter_text)
            for voter_no in voter_pattern:
                self.voter_list.append(voter_no)
            
        print('Voter Card data extracted successfully..\n')
        print('Display Voter Card data:\n\n',self.voter_list)    
        db['voter_info'] = self.voter_list
        print('\nVoter Card data added successfully to database record')


obj1 = People_record()

while True:
    print('''

                <<<<<<<<<<< Miscellaneous Dataset Extraction >>>>>>>>>>>

        -----------------------------------------------------------------------------    

                            Enter 1 : To Load Aadhar Data
                            Enter 2 : To Load Pancard Data
                            Enter 3 : To Load Driving Licence Data
                            Enter 4 : To Load Votercard Data
                            Enter 5 : To Display All Data
                            Enter 6 : To Exit From System

        -----------------------------------------------------------------------------    
        ''')

    ch = int(input('Enter Your Choice: '))

    if ch == 1 :
        obj1.aadharData()
        # print('Aadhar data extracted from files successfully..')

    elif ch == 2 :
        obj1.panData()

    elif ch == 3:
        obj1.drLicenceData()

    elif ch == 4:
        obj1.voterData()

    elif ch == 5:
        print('\n\nDisplay all data: \n')
        obj1.displayData()

    elif ch == 6:
        print('Exit From System..')
        sys.exit()

    else:
        print('Enter The Valid choice..')



















