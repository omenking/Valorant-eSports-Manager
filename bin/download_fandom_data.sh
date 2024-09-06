# To be honest this data is useless and better to just scrape our own data.

aws s3 cp s3://vcthackathon-data/fandom/valorant_esports_pages.xml.gz valorant_esports_pages.xml.gz
aws s3 cp s3://vcthackathon-data/fandom/valorant_pages.xml.gz valorant_pages.xml.gz

gunzip valorant_esports_pages.xml.gz 
gunzip valorant_pages.xml.gz 