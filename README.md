# Send Email Using a CSV File
This Python program takes an input CSV, message, and subject file and sends a personalized email to each recipient listed in the CSV.

## SMTP Setup
**NOTE:** As of now, this program only works for Gmail accounts. I apologize for any inconvenience.

There are several steps to follow in order to allow the SMTP module to send emails from your account.

1. Log onto [Gmail]("gmail.com") and sign into your account.
2. Click the gear icon in the upper-right corner of the page and, from the dropdown, select settings.
3. From the menu bar on the top of the screen, select the "Forwarding and POP/IMAP" option.
4. Scroll down to the "IMAP Access" and enable IMAP. This can be left enabled, for it should not raise security issues.
5. Click the "Save Changes" button.
6. Go to [less secure app access]("myaccount.google.com/lesssecureapps") on your Google account.
7. Enable less secure app accesss using the slider. After you finish sending emails, this should be turned off in order to not raise security issues.

## Configuration

### Message
The message text can be edited to say whatever you want. Anytime you want an instance of someone's full name, which will be provided by the CSV file, type "fullName" without the quotes. When an instance of someone's first name is required, type "name" without the quotes.

### Subject
The subject text can be edited to say whatever you want. Anytime you want an instance of someone's full name, which will be provided by the CSV file, type "fullName" without the quotes. When an instance of someone's first name is required, type "name" without the quotes.

### CSV File
**NOTE:** The information provided in the CSV file is not real and should not be used when running the program. It is exists purely as an example.

The CSV file can be filled in with however many emails and names you choose. The first row of text **SHOULD NOT** be edited, for it allows the Python script to properly read the data. Each row of emails and names should be in the format: email,firstName,lastName. No spaces should be placed between the commas and the next piece of data. Every new email and name pair should be placed on a separate line with no empty lines being placed in between pieces of data.

## Running the Program
To run the program, download the repository and unzip if necessary. Next, open your terminal, command line, or shell and navigate into the directory containing these files. Finally, type `python sender.py` to run the script.

Please report any issued in the code in order to help improve this program. Suggestions are welcome. I hope you enjoy the tool! 😄
