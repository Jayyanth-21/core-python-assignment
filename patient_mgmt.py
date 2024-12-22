class Patient:
    def __init__(self):
        self.patients = []

    def addPatient(self):
        name = input("Enter patient's name: ")
        try:
            age = int(input("Enter patient's age: "))
            disease = input("Enter patient's disease: ")
            self.patients.append({"Name": name, "Age": age, "Disease": disease})
            print(f"Patient {name} added successfully")
        except ValueError:
            print("Invalid input for age...Please enter a valid age")

    def search(self, disease):
        found_patients = [patient["Name"] for patient in self.patients if patient["Disease"] == disease]
        if found_patients:
            print(f"Patients with {disease}: {found_patients}")
        else:
            print(f"No patients found with {disease}.")

    def manageRecords(self):
        while True:
            print("1. Add a patient")
            print("2. Search for patients by disease")
            print("3. Exit")
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    self.addPatient()
                elif choice == 2:
                    disease = input("Enter the disease to search for: ")
                    self.search(disease)
                elif choice == 3:
                    print("Exiting the system.")
                    break
                else:
                    print("Invalid choice. Please enter a valid option (1, 2, or 3).")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

ps = Patient()
ps.manageRecords()
