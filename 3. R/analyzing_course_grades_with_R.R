# Print title
print("ANALYZING COURSE GRADES WITH R")
print("By Marco Ramirez and Julio Poveda")
# Read data.txt
my_data <- read.delim("data.txt")

#----------------------------------------------------------------
# Functions
#----------------------------------------------------------------

# Function to convert a caracter to numeric value
convert_character_to_numeric <- function(a_character) {
  a_numeric <- as.numeric(a_character)
  a_numeric
}

# Function to select a column
select_column <- function(column_number) {
  selected_column <- my_data[column_number]
  selected_column
}

# Function to find the maximum value in a column
find_max_value_column <- function(column_search) {

  maximum_value <- -Inf
  
  for (i in 1:35)
  {
    if (column_search[i,1] >= maximum_value) {
      maximum_value <- column_search[i,1]
    }
  }
  
  maximum_value
}

# Function to find the minimum value in a column
find_min_value_column <- function(column_search) {

  minimum_value <- Inf
  
  for (i in 1:35)
  {
    if (column_search[i,1] <= minimum_value) {
      minimum_value <- column_search[i,1]
    }
  }
  
  minimum_value
}

# Function to find the average value of a column
find_average_column <- function(column_average) {
 
  average <- 0
  num_elements <- 0
  sum_of_elements <- 0
  
  for (i in 1:35)
  {
    sum_of_elements <- sum_of_elements + column_average[i,1]
    num_elements <- num_elements + 1
  }
  
  average <- (sum_of_elements / num_elements)
  average
}

# Functions to find the row with the maximum value in a column
find_row_max_value <- function(find_row) {
  max_value <- -Inf
  for (i in 1:length(find_row))
  {
    if (find_row[i] >= max_value)
    {
      max_value <- find_row[i]
    }
  }
  
  max_value
}

find_row_max_value_column <- function(column_search) {
  max_value <- -Inf
  row_max_value <- -Inf

  
  for (i in 1:35)
  {
    if (column_search[i,1] >= max_value) {
      row_max_value <- i
      max_value <- column_search[i,1]
    }
  }
  
  row_max_value
}

#----------------------------------------------------------------
# Find maximum value
#----------------------------------------------------------------

# Ask user to enter a column number
col_num_character <- readline(prompt = "Enter a column number in order to find its maximum value please: ")

# Convert character to numeric
col_num_numeric <- convert_character_to_numeric(col_num_character)

# Select the column according to user input
column_to_search_maximum <- select_column(col_num_numeric)

# Loop the column selected by the user to find maximum value
column_maximum_value <- find_max_value_column(column_to_search_maximum)

print(paste("The maximum value of the selected column is ",column_maximum_value))


#----------------------------------------------------------------
# Find minimum value
#----------------------------------------------------------------

# Ask user to enter a column number
col_num_character <- readline(prompt = "Enter a column number in order to  find its minimum value please: ")

# Convert character to numeric
col_num_numeric <- convert_character_to_numeric(col_num_character)

# Select the column according to user input
column_to_search_maximum <- select_column(col_num_numeric)

# Loop the column selected by the user to find minimum value
column_minimum_value <- find_min_value_column(column_to_search_maximum)

print(paste("The minimum value of the selected column is ",column_minimum_value))


#----------------------------------------------------------------
# Find average
#----------------------------------------------------------------

# Ask user to enter a column number
col_num_character <- readline(prompt = "Enter a column number in order to calculate its average: ")

# Convert character to numeric
col_num_numeric <- convert_character_to_numeric(col_num_character)

# Select the column according to user input
column_find_average <- select_column(col_num_numeric)

# Calculate the average
column_average <- find_average_column(column_find_average)

print(paste("The average of the selected column is ",column_average))


#----------------------------------------------------------------
# Find column with highest average
#----------------------------------------------------------------

column_find_average_1 <- my_data[1]
column_find_average_2 <- my_data[2]
column_find_average_3 <- my_data[3]
column_find_average_4 <- my_data[4]
column_find_average_5 <- my_data[5]
column_find_average_6 <- my_data[6]
column_find_average_7 <- my_data[7]
column_find_average_8 <- my_data[8]
column_find_average_9 <- my_data[9]

# Calculate average for column 1
column_1_average <- find_average_column(column_find_average_1)

# Calculate average for column 2
column_2_average <- find_average_column(column_find_average_2)

# Calculate average for column 3
column_3_average <- find_average_column(column_find_average_3)

# Calculate average for column 4
column_4_average <- find_average_column(column_find_average_4)

# Calculate average for column 5
column_5_average <- find_average_column(column_find_average_5)

# Calculate average for column 6
column_6_average <- find_average_column(column_find_average_6)

# Calculate average for column 7
column_7_average <- find_average_column(column_find_average_7)

# Calculate average for column 8
column_8_average <- find_average_column(column_find_average_8)

# Calculate average for column 9
column_9_average <- find_average_column(column_find_average_9)


values <- c(column_1_average, column_2_average, column_3_average, column_4_average, column_5_average, column_6_average, column_7_average, column_8_average, column_9_average)
column_highest_average <- 0
highest_average <- 0

for (i in 1:9)
{
  if (values[i] >= highest_average)
  {
    column_highest_average <- i
    highest_average <- values[i]
  }
}

print(paste("The column with the highest average is column ", column_highest_average))


#----------------------------------------------------------------
# Find row with highest value given a column number
#----------------------------------------------------------------

# Ask user to enter a column number
col_num_character <- readline(prompt = "Enter a column number in order to find the row with the maximum value: ")

# Convert character to numeric
col_num_numeric <- convert_character_to_numeric(col_num_character)

# Select the column according to user input
column_to_search_maximum <- select_column(col_num_numeric)

# Loop the column selected by the user to find row where the maximum value is
column_maximum_value_row <- find_row_max_value_column(column_to_search_maximum)

print(paste("The row with the maximum value of the selected column is row ",column_maximum_value_row))






