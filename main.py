# This is basic python script I wrote for sending out cover letters. You may edit however you please.
# The cover letter template is from a user on Reddit, his account has been deleted, so I cannot give him
# credit sadly. If anyone wants to help me improve, please reach out to me on linked.com/erhime-akpo
# No external libraries needed

import datetime

date = datetime.date.today()
date = date.strftime('%x')

# Enter your information here
applicant = {'name': 'Enter your name',  # Replace with your name
             'email': 'Enter your email',  # Replace with your email
             'number': '(XXX)XXX-XXXX',  # Replace with your phone number
             'address': 'Address',  # Replace with your address
             'state': 'NY',  # Replace with your state(NY)
             'city': 'New York',  # Replace with your city
             'zip': '10021'}  # Replace with your zip

# Enter hiring information here
hirer = {'cname': 'Enter company name',  # Replace with company's name
         'cstate': 'Enter company state',  # Replace with company's state
         'ccity': 'New York',  # Replace with company's city
         'role': 'Hiring Manager',  # Replace with hiring manager name if known/else leave as is
         'position': 'Part Time Help Desk',  # Replace with position applying for
         # Replace with company's requirements(usually listed as bullet-points)
         'requirement1': 'knowledge of Microsoft Windows Operating Systems',
         'requirement2': 'knowledge of office productivity software such as Microsoft Outlook, Word, Excel, etc.',
         'requirement3': 'knowledge of basic networking and connectivity – DHCP, DNS, Cabling, etc.',
         'requirement4': 'Knowledge of Virus and Spyware removal techniques'}

# Here is the string text for the cover letter. Look for [!!CHANGE] Text as you will need to edit
# that yourself
coverLetter = f"""
{applicant.get('name')}
{applicant.get('address')}, {applicant.get('city')}, {applicant.get('state')}
{applicant.get('zip')}
{applicant.get('number')} - {applicant.get('email')}
{date}


Mr./Ms. {hirer.get('role')}
{hirer.get('cname')}
{hirer.get('ccity')}, {hirer.get('cstate')}

Dear Mr./Ms. {hirer.get('role')}, The purpose of this letter is to apply for the {hirer.get('position')} position
you have posted on website on {date}. An excellent candidate for this position would have a strong 
{hirer.get('requirement1')}, {hirer.get('requirement2')}, 
and {hirer.get('requirement2')}. In addition,
the right candidate for this role should also {hirer.get('requirement3')}, {hirer.get('requirement4')}. I believe my 
resume will show a proven history of utilizing these various skills through my professional and educational experiences. 
-------------------------------------------------------------------------------------------------------------------
[!!CHANGE]]  Body of letter should specifically identify key requirements to show how applicant is qualified for
job description.  [!!CHANGE]]
--------------------------------------------------------------------------------------------------------------------
{hirer.get('cname')} is an outstanding company in {hirer.get('ccity')} with a proven track record of  [!!CHANGE]
outputting what company does/makes  [!!CHANGE]. I believe that as a {hirer.get('position')}, I could bring a
diverse set of skills to {hirer.get('cname')} and in return I can further develop my knowledge and experience
while working with your team at {hirer.get('cname')}. I’m very interested in discussing this opportunity further.
Please contact me at your earliest convenience, so I can learn more about the position. I’ve attached a
copy of my resume for your review. I look forward to hearing from you soon.
Thank you for your time and consideration.

Sincerely,
{applicant.get('name')}

"""

print(coverLetter)
