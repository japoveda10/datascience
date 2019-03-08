# Exploratory Data Analysis mtcars dataset

# To clean Console hit control + L

# To execute a command, select it and hit control + return

# Structure of the dataset
str(mtcars)

# Help
?mtcars

# Class of column vs in mtcars
class(mtcars$vs)

# vs and am should be booleans

mtcars$vs = as.logical(mtcars$vs)
mtcars$am = as.logical(mtcars$am)

str(mtcars)

summary(mtcars)

# Weight in kilos
wt <- (mtcars$wt*1000)/2
wt

mtcars.new <- transform(mtcars,wt=wt*1000/2)
mtcars.new

summary(mtcars.new)
