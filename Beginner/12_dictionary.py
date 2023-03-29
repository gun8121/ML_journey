# dictionary - key value pair
# word - key / number - value

# example calendar
# Jan -> January / Mar -> March

month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "July": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(month_conversions["Jan"])
print(month_conversions.get("Luv", "Not a valid Key")) # get function to check if key exists