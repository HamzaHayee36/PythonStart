# Declaring a string variable 'name' with the value "fajjan"
name = "fajjan"

# Declaring a string template 'sen' with a placeholder for a string value
sen = "%s is 24 years old"

# Printing the 'sen' template with the 'name' variable as its value
print(sen % name)

# Declaring another string template 'sen' with placeholders for two string values
sen = "%s %s is the Prime Minister of Pakistan"

# Printing the 'sen' template with "Imran Khan" and "Niazi" as its values respectively
print(sen % ("Imran Khan", "Niazi"))

# Declaring yet another string template 'sen' with a placeholder for a string and an integer value
sen = "%s is %d years old now"

# Printing the 'sen' template with "Imran Khan" as the string and 71 as the integer value
print(sen % ("Imran Khan", 71))
