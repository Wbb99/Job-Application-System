# Job Application System

class job_application_system:
    def __init__(self, job_listing):
        self.job_listing = job_listing
        self.application_data = {}

    def get_valid_input(self, prompt, validation_func):
        while True:
            user_input = input(prompt)
            try:
                if validation_func(user_input):
                    return user_input
                else:
                    raise ValueError("Invalid input. Please enter a valid input.")
            except ValueError as e:
                print(e)

    def validate_location(self, location):
        if not location.isalpha():
            raise ValueError("Invalid input. Please enter a valid location only using letters")
        return location.lower() == self.job_listing["location"].lower()

    def validate_contact_number(self, contact_number):
        if not contact_number.isdigit():
            raise ValueError("Invalid input. Please enter a valid phone number only using numbers")
        return contact_number.isdigit() and len(contact_number) == 11

    def run_application(self):
        print(f"\nApplying for the position: {self.job_listing['title']}")
        print(f"\nLocation: {self.job_listing['location']}")
        print(f"\nContact Number: {self.job_listing['contact_number']}")

        try:
            location = self.get_valid_input("\nPlease enter your location: ", self.validate_location)
            contact_number = self.get_valid_input("\nPlease enter your contact number: ", self.validate_contact_number)

            self.application_data["location"] = location
            self.application_data["contact_number"] = contact_number

            print("\nApplication created successfully!")
            print("\nApplication Details:")
            print(f"Job Title: {self.job_listing['title']}")
            print(f"Location: {self.application_data['location']}")
            print(f"Contact Number: {self.application_data['contact_number']}\n")
        except KeyboardInterrupt:
            print("\nApplication process cancelled.")


job_listing = {
    "title": "Software Developer",
    "location": "London",
    "contact_number": "12345678910"
}

job_app_system = job_application_system(job_listing)
job_app_system.run_application()
