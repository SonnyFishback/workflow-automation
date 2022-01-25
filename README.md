# Workflow automation

### Objective:
- User has Excell speadsheet to hold data about leads. Each row will be data on a lead. this data will most likely be a link to lead in salesforce, the formateed address of the lead and an empty box that will be populateed by a checkmark emoji or an x emoji onced checked for internet availabilty. Another idea is to process the data and then send out an email with all the links of the leads that have internet available but, this is probably gonna roll out in version two if we take the REST API/Serverless approach.

- There needs to be a proceess to convert the spreadsheet into a .CSV file. Users can also save the data as an .csv file and this process should still be able to work.

- The bot should be able to parse/iterate through .csv file and preform an action on each iteration, if necessary.

- The bot ideally will check a live excell document each time it is edited if the process is not too heavy. For now we just need to take the .csv file and parse out that data.

## Will need:
- Link to internet checker.
- A library/Tool  for web process automation that works best with the sack the website is created with.
- A library/Tool to interact with Excell spreadsheets.
- Test data. (A .CSV file of an address, phone number and link to the lead in salesforce).



## How will it work:
### Version one:

Step 1: Enter the leads address and salesforce link inside of Excel spreadsheet.
Step 2: Convert spreadsheet into a .CSV
Step 3: Take a commannd in the terminal to run the "check for internet availabilty" program.
Step 4: Run program

        ```python
        """
        Function parse_csv(.CSV file))  needs to take a .csv file of leads and decode them to return a dictionary of lead objects.
        """
        class Lead:
            """ Lead Object"""
            __init__(self, salesforce_link: String, address = String, isAvailable = False)
            url = self.salesforce_link
            address = self.address
            isAvailable = self.isAvalable

        # def parse_csv(fd, ddt) -> Array of [desired_object] or Dict?
        def parse_csv(file_data, desired_object):
            pass
        """
        Function is_internet_available(Lead()) needs to take a lead object and perform a check the lead. This will be a multi step process:

        1. Open a web browser with the automation/webscrapping technology chosen.
        2. Take the leads address and use a dummy number as input for the internet availabilty form.
        3. Submit the form.
        4. Figure out a way to determine if the lead can get internet by what is displayed on the page.
        4. Set the Lead.isAvaliable value to True if it can get internet and set it to False if cant get internet
        """
        def is_internet_available():
            return

        ```