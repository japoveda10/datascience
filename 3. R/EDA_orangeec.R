# Exploratory Data Analysis orangeec dataset

str(orangeec)

summary(orangeec)

platzi_time <- c(25,5,10,15,10)
reading_time <- c(30,10,5,10,15)
learning_time <- platzi_time + reading_time
learning_time

learning_days <- c("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
learning_days

days_more_than_20min <- c(TRUE,FALSE,FALSE,TRUE,TRUE)
days_more_than_20min

total_platzi_time <- sum(platzi_time)
total_platzi_time

total_reading_time <- sum(reading_time)
total_reading_time

total_additional_time <- total_platzi_time + total_reading_time
total_additional_time

# scatter plot
plot(orangeec$GDP.PC ~ orangeec$Creat.Ind...GDP,
     xlab="Orange Economy Contribution to GDP (%)",
     ylab="GDP Per Cápita (USD)",
     main="Orange Economy and GDP per capita ratio")

# install.packages("dplyr")

library(dplyr)

# GDP per capita average in latam

economy <- mean(orangeec$GDP.PC)
economy

# new variable
orangeec <- orangeec %>%
  mutate (strong_economy = ifelse(GDP.PC < economy,
          "below average", "at or above average"))

# install.packages("ggplot2")

library(ggplot2)

# Boxplot
ggplot(orangeec, aes(x=strong_economy, y=Services...GDP,
                     fill=strong_economy))+
  geom_boxplot()+
  labs(x="Type of Country", y="% Services in GDP",
       title = "Services Contribution in GDP in LATAM countries with high and low GDP per capita")
