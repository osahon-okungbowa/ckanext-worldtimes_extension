## DESCRIPTION

 This repo provides a ckan extension that displays the current time across the world timezones.
 The extension is called ***worldtimes_extension***
 
  

## How to install the extension

- You should already have a docker image of ckan (development version) installed. [Get instructions on installation](https://github.com/okfn/docker-ckan)  

- Clone this repo into the *src* sub folder of where your docker-ckan was setup
- Start up your ckan instance
- *The worldtimes_extension* is installed and ready to use at "/worldtimes"
- Open up your browser and visit : *[your_ckan_domain_name]/worldtimes* to see the extension in action


## EXTENSION DEPENDENCIES

The script depends on the following python packages:

- pytz
