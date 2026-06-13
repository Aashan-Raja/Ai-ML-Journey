from pathlib import Path
class Patient():
    def __init__(self ,pt_id, pt_name , pt_age , scan_type , total_bill):
        self.pt_id = pt_id
        self.pt_name = pt_name
        self.pt_age = pt_age
        self.scan_type = scan_type
        self.total_bill = total_bill

class Hospital:
    def patient(self , pt_obj):
        self.patient_list = []
        self.patients = pt_obj
        self.patient_list.append(self.patients)
        self.patient_file = "patient.txt"
    def show_patients_data (self):
        for i in self.patient_list:
            print(f"Patient ID : {i.pt_id} | Patient Name : {i.pt_name} | Patient Age : {i.pt_age} | Scan type : {i.scan_type} | Total Bill : {i.total_bill}")
    def savedata(self):
        self.p = Path(self.patient_file)
        with open(self.p ,"w") as fs:
            for i in self.patient_list:
             text = f"Patient ID : {i.pt_id} | Patient Name : {i.pt_name} | Patient Age : {i.pt_age} | Scan type : {i.scan_type} | Total Bill : {i.total_bill}"
             fs.write(text)
        print("File Saved Successfully")
while True:
    print(" 1 : Enter new patient data:")
    print("2 : Show Patient Data:")
    print("3 : Save and exit")
    choice = int(input("Enter choice"))
    if choice == 1:
        pt_id = int(input("Enter Patient id: "))
        pt_name = input("Enter patient name :")
        pt_age = int(input("Enter Patient age :"))
        scan_type = input("Type of scan name: ")
        total_bill = int(input("Enter Total bill :"))
        
        new_patient = Patient(pt_id , pt_name , pt_age ,scan_type ,total_bill)
        hosp = Hospital()
        hosp.patient(new_patient)
        hosp.show_patients_data()
        print("=== Patient Added Successfully === ")
    if choice == 2:
        hosp.show_patients_data()
    if choice == 3:
        hosp.savedata()
    
