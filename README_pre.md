Mings weather app
present real time weather from a weather API

Feature 1: Search weather by location(major city in Australia)

Feature 2: Search weather by date

Feature 3 :Display search history and result

Feature 4: Help ( introduce each function and what command user should type)






Development Plan

Functionality 1: Show weather for a location

 Implement command check-weather to print formatted dummy weather info for Sydney. [formatting, writing stdout]
 Re-implement check-weather to look up real weather data from internet for Sydney today, and print it (in the same format). Show only basic weather data (e.g. temp). [curl, JSON manipulation]
 Implement a prompt at the beginning of check-weather to ask for location. [reading stdin]
 Retrieve weather data for given location. [handling variable input, input parsing]
 Print weather data for the right location. [handling variable output]
 Implement an optional argument where the user can specify a location with the command (e.g. --location=sydney), so that the command doesn't need to prompt for one. [libraries, input parsing]
 Optionally print more weather data (e.g. precipitation).
 Add more sophisticated options, e.g. choosing temperature meter. [input parsing, conditional algorithm, numeric conversion algorithm]

 
 Functionality 2: Show weather on any given date

 Amend check-weather to include an option --date that the user can input a valid date into. [input parsing]
 Amend check-weather to retrieve weather data for the date specified, or today if not specified. [handling variable input]


 Functionality 3: Show a history of weather checks

 Amend check-weather to save the weather result to a file each time it is run. [file writing]
 Improve check-weather to save a new file each time, but limit the saved results to a maximum of 5 (removing the oldest if limit is reached). [FIFO queues]
 Implement subcommands. [input parsing]
 Rename check-weather command to weather.
 Add subcommands weather history & weather check, with weather check doing what check-weather previously did.
 Implement weather history to read and print the saved weather result files. [file reading]


 Additional Functionality

 Implement a help function that prints a manual for using the command and its subcommands.