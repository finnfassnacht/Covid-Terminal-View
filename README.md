# COVID Terminal View

Covid-Terminal-View is a Python script that allows you to view the current COVID-19 cases, recovered, and death numbers in your terminal with a simple "covid" command, making it a convenient and easy-to-use tool for tracking the global pandemic. The script employs web-scraping with the Beautiful Soup module to extract the information from the [Worldometers website](https://www.worldometers.info/coronavirus/#countries) and presents the data in an easily understandable, color-coded format.

## Installation

To install Covid-Terminal-View, follow these steps:

1. Clone the repository and change the directory.
```
git clone https://github.com/finnfassnacht/Covid-Terminal-View.git 
cd Covid-Terminal-View
```
2. Install the required dependencies with pip3:
```
pip3 install -r requirements.txt
```

3. Execute the install.sh bash-script:
```
sudo bash install.sh
```
This will add the covid script to your /usr/bin directory, which requires administrative permissions. Using sudo grants the necessary permissions to execute the script and add the covid command to your system.

## Usage

To view the current COVID-19 cases, simply type the following command in your terminal:

```
covid
```
This will display the total cases, recovered and dead numbers in color-coded form.
