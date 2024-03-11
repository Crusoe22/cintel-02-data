import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly, output_widget, render_widget
import palmerpenguins  # This package provides the Palmer Penguins dataset
import pandas
from shiny import render
import seaborn as sns

# Use the built-in function to load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()

ui.page_opts(title="Nolan's Penguin Data", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")

# Add a Shiny UI sidebar for user interaction
# Use the ui.sidebar() function to create a sidebar
# Set the open parameter to "open" to make the sidebar open by default
# Use a with block to add content to the sidebar

with ui.sidebar(open="open"):

# Use the ui.h2() function to add a 2nd level header to the sidebar
#   pass in a string argument (in quotes) to set the header text to "Sidebar"
    ui.h2("Sidebar")
    
# Use ui.input_selectize() to create a dropdown input to choose a column
#   pass in three arguments:
#   the name of the input (in quotes), e.g., "selected_attribute"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) 
#   e.g. ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"]
    
    ui.input_selectize("selected_attribute", "Body Measurement in Millimeters", ["bill_length_mm", 
                                                                                 "bill_depth_mm", 
                                                                                 "flipper_length_mm", 
                                                                                 "body_mass_g"]) #Maybe change categories


    
# Use ui.input_numeric() to create a numeric input for the number of Plotly histogram bins
#   pass in two arguments:
#   the name of the input (in quotes), e.g. "plotly_bin_count"
#   the label for the input (in quotes)

    ui.input_numeric("plotly_bin_count", "Bin Count", 10)

    
# Use ui.input_slider() to create a slider input for the number of Seaborn bins
#   pass in four arguments:
#   the name of the input (in quotes), e.g. "seaborn_bin_count"
#   the label for the input (in quotes)
#   the minimum value for the input (as an integer)
#   the maximum value for the input (as an integer)
#   the default value for the input (as an integer)
    ui.input_slider("seaborn_bin_count", "Label for Input", 1, 100, 50)

# Use ui.input_checkbox_group() to create a checkbox group input to filter the species
#   pass in five arguments:
#   the name of the input (in quotes), e.g.  "selected_species_list"
#   the label for the input (in quotes)
#   a list of options for the input (in square brackets) as ["Adelie", "Gentoo", "Chinstrap"]
#   a keyword argument selected= a list of selected options for the input (in square brackets)
#   a keyword argument inline= a Boolean value (True or False) as you like

    ui.input_checkbox_group("selected_species_lis", "Selected Species of Penguins", ["Adelie", "Gentoo", "Chinstrap"], selected="", inline=False)


    
# Use ui.hr() to add a horizontal rule to the sidebar

    ui.hr()

# Use ui.a() to add a hyperlink to the sidebar
#   pass in two arguments:
#   the text for the hyperlink (in quotes), e.g. "GitHub"
#   a keyword argument href= the URL for the hyperlink (in quotes), e.g. your GitHub repo URL
#   a keyword argument target= "_blank" to open the link in a new tab

    ui.a("GitHub", href="https://github.com/Crusoe22/cintel-02-data.git", target="_blank")


# When passing in multiple arguments to a function, separate them with commas.


with ui.layout_columns():

    @render.data_frame
    def penguins_datatable():
        return render.DataTable(penguins_df) 

    @render.data_frame
    def penguins_grid():
        return render.DataGrid(penguins_df)

with ui.layout_columns():
    @render_plotly  
    def plot_plt():  
        return px.histogram(penguins_df,
            x="body_mass_g",
            title="Penguin Mass",
            labels={"body_mass_g": "Body Mass (g)", "count": "Count"})
        
    @render.plot  
    def plot_sns():  
        return sns.histplot(penguins_df, x="species", kde=False)


with ui.card(full_screen=True):

    ui.card_header("Plotly Scatterplot: Species")

    @render_plotly
    def plotly_scatterplot():
        # Create a Plotly scatterplot using Plotly Express
        # Call px.scatter() function
        # Pass in six arguments:
        return px.scatter(penguins_df, x="flipper_length_mm", y="bill_length_mm", color="species", 
                          facet_row="species", facet_col="sex", title="Penguin Scatterplot")


