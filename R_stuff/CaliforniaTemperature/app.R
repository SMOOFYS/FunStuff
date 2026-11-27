#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    https://shiny.posit.co/
#

library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
  
  
  # Application title
  titlePanel("Average Temperatures Over Last Month"),
  

  # Sidebar with a slider input for number of bins 
  sidebarLayout(
    sidebarPanel(
      
      h3("How to Interpret the Graph"),
      
      p("The graph shown will display two things: the last 30 days and the average temperatures for each day."),
      
      p("You can change what city you want to display by clicking on the dropdown menu and selecting any city of your choosing."),
      
      p("Every graph plots the average temperature for each day and makes a polynomial regression."),
      
      p("By looking at a point on the line, you can figure out the average temperature for any chosen day you would like to learn about."),
      
      p(),
      
      selectInput("City",
                  "Choose a Californian city:",
                  choices = c("Sacramento" = "SacClimate",
                              "San Francisco" = "SFClimate",
                              "Los Angeles" = "LAClimate",
                              "Anaheim" = "AnaClimate",
                              "San Diego" = "SDClimate",
                              "Long Beach" = "LBClimate",
                              "San Jose" = "SJClimate",
                              "Oakland" = "OakClimate"),
                  selected = "SacClimate")
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      
      plotOutput("plot", height="95vh"),
      
    )
  )
)

#Call Packages

library(ISLR)
library(ggplot2)
library(rsconnect)

#Import Data sets

SacClimate = read.csv("Sac Climate - Sheet1.csv")
SFClimate = read.csv("SF Climate - Sheet1.csv")
LAClimate = read.csv("LA Climate - Sheet1.csv")
AnaClimate = read.csv("Ana Climate - Sheet1.csv")
SDClimate = read.csv("SD Climate - Sheet1.csv")
LBClimate = read.csv("LB Climate - Sheet1.csv")
SJClimate = read.csv("SJ Climate - Sheet1.csv")
OakClimate = read.csv("Oak Climate - Sheet1.csv")

# Define server logic for shinyapps
server <- function(input, output) {
  
  # Reactive expression to generate the plot based on selected dataset
  # (This is what makes the graph interactive)
  selected_data <- reactive({
    switch(input$City,
           "SacClimate" = SacClimate,
           "SFClimate" = SFClimate,
           "LAClimate" = LAClimate,
           "AnaClimate" = AnaClimate,
           "SDClimate" = SDClimate,
           "LBClimate" = LBClimate,
           "SJClimate" = SJClimate,
           "OakClimate" = OakClimate)
  })
  
  # Render the plot for shinyapps based on selected dataset
  output$plot <- renderPlot({
    
    # Get the selected dataset from the reactive function earlier
    dataset <- selected_data()
    
    # Fit polynomial model (For data input the dataset variable)
    temp.lm <- lm(Temperature...F. ~ poly(Day, 3), data = dataset)
    
    # make a grid of values for the predictor, Day, to make predictions
    # used predict() 
    
    #find the max range of the predictor
    
    Daylims <- range(dataset$Day)
    
    #Then make a grid
    day.grid <- seq(from = Daylims[1], to = Daylims[2])
    
    #use predict() to make predictions for Day
    
    preds <- predict(temp.lm, newdata = list(Day = day.grid), se = TRUE)
    se.bands <- cbind(preds$fit + 2 * preds$se.fit, preds$fit - 2 * preds$se.fit)
    
    # Plotting using ggplot2
    ggplot(data = dataset, aes(x = Day, y = Temperature...F.)) +
      geom_point(color = "darkgrey") + 
      geom_smooth(method = "lm", formula = y ~ poly(x, 3), se = FALSE, color = "darkgreen") +
      labs(title = paste("Average Temperature Over the Last 30 Days -", input$dataset),
           x = "Day", y = "Temperature (°F)") +
      theme_minimal()
  })
}
# Run the application 
shinyApp(ui = ui, server = server)

