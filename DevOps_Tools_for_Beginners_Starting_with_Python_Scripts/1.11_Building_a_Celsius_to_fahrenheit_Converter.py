#Celsius to Fahrenheit Converter with Extra Examples

#This script converts a temperature from Celsius to Fahrenheit and demonstrates various types and string manipulations

# Author:

#Date:

#Rev

days_in_week=7

celsius_temp=25.0#Temperature to convert

pi=3.14159 #Example of a float constant

greetings ="Hello , "

user_name ="Python learner "

is_summer =True

month =["January", "February", "March", "May", "June", "July", "August", "September", "October", "November""December"]#list
temp_scales={"Celsius":"°C","Fahrenheit":"°F"}#disnary
celsius_to_fahrenheit_factor=9/5
fahrenheit_offset=32
fahrenheit_temp= (celsius_temp*celsius_to_fahrenheit_factor)+fahrenheit_offset
fahrenheit_temp=round(fahrenheit_temp,1)
full_greeting = greetings+user_name #string concatenation

shouted_greeting=full_greeting.upper() #convert to uppercase
whispered_greeting=full_greeting.lower() #conver to lowercase

mount_count=len(month)
output1=str(celsius_temp)+temp_scales["Celsius"]+"is e"+str(fahrenheit_temp)+temp_scales["Fahrenheit"]
