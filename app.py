from instapy_cli import client

username='travelify_ca'
password='travelify@621'
image='/Users/rajathpurayil/Insta_automation/insta.jpg'
text='Sargalaya'

with client(username,password) as cli :
    cli.upload(image,text)