# Send Email Using an Excel File
This Python program takes an input Excel, message, and subject file and sends a personalized email to each recipient listed in the Excel.

## SMTP Setup
**NOTE:** As of now, this program only works for Gmail, Outlook/Hotmail, and Yahoo accounts. I apologize for any inconvenience.

### For Gmail Accounts
There are several steps to follow in order to allow the SMTP module to send emails from your Gmail account.

1. Log onto [Gmail](https://gmail.com) and sign into your account.
2. Click the gear icon in the upper-right corner of the page and, from the drop-down, select settings.
3. From the menu bar on the top of the screen, select the "Forwarding and POP/IMAP" option.
4. Scroll down to the "IMAP Access" and enable IMAP. This can be left enabled, for it should not raise security issues.
5. Click the "Save Changes" button.
6. Go to [less secure app access](https://myaccount.google.com/lesssecureapps) on your Google account.
7. Enable less secure app access using the slider. After you finish sending emails, this should be turned off in order to not raise security issues.

## Configuration

### Message
The message text can be edited to say whatever you want. Anytime you want an instance of someone's full name, which will be provided by the Excel file, type "fullName" without the quotes. When an instance of someone's first name is required, type "name" without the quotes.

### Subject
The subject text can be edited to say whatever you want. Anytime you want an instance of someone's full name, which will be provided by the Excel file, type "fullName" without the quotes. When an instance of someone's first name is required, type "name" without the quotes.

### Excel File
**NOTE:** The information provided in the Excel file is not real and should not be used when running the program. It is exists purely as an example.

The Excel file can be filled in with however many emails and names you choose. The first row of text **SHOULD NOT** be edited, for it allows the Python script to properly read the data. Each row of emails and names should be in the format: email firstName lastName, with each piece of data having its own cell. Every new email and name pair should be placed on a separate line with no empty lines being placed in between pieces of data.

#### Google Sheets Instructions
If you do not have Microsoft Excel do not fret, for you can still edit the file containing the email list. Simply log onto [Google Drive](https://drive.google.com) using your Google account. From there, click the "New" button in the upper-left corner and select "File Upload." Next, navigate to the directory with the `email-list.xlsx` file, click the file, and select "Open." Once the file is done uploading to Google Drive, double click on it. You should be brought to a preview screen, from where you can click the "Open with Google Sheets" button. You should now be able to edit the file with the email addresses and names that you want. After you have finished editing the file with the information that you want, select the "File" button in the upper-left corner, and, from the drop-down, "Download As..." and "Microsoft Excel." When the file has finished downloading, open your file explorer and navigate to your "Downloads" directory. From there, click the downloaded file and move it into the directory containing the downloaded repository code. You should now be able to use the edited file as the email list.

## Running the Program
To run the program, download the repository and unzip if necessary. Next, open your terminal, command line, or shell and navigate into the directory containing these files. Install the necessary packages using either `conda install smtplib xlrd pandas` if you have the Anaconda distribution of Python, or `pip install smtplib xlrd pandas` otherwise. Finally, type `python sender.py` to run the script.

Please report any issued in the code in order to help improve this program. Suggestions are welcome. I hope you enjoy the tool! 😄
