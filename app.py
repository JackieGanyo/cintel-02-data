import plotly.express as px
from shiny.express import input, ui
from shinywidgets import render_plotly
import palmerpenguins # This package providesthe Palmer Penguins dataset

# Palmer Penguins Dataset
# Column names for the penguins data set include:
# - species: Penguin species (Chinstrap, Adelie, or Gentoo)
# - island:  island name (Dream, Torgersen, or Biscoe)
# - bill_length_mm:  length of the bill in millimeters
# - bill_depth_mm:  depth of the bill in millimeters
# - flipper_length_mm:  length of the flipper in millimeters
# - body_mass_g:  body mass in grams
# - sex:  MALE or FEMALE

# Load the dataset into a pandas Dataframe
#Use the built-in functionto load the Palmer Penguins dataset
penguins_df = palmerpenguins.load_penguins()


ui.page_opts(title="Palmer Penguins JGanyo", fillable=True)
with ui.layout_columns():

    @render_plotly
    def plot1():
        return px.histogram(px.data.tips(), y="tip")

    @render_plotly
    def plot2():
        return px.histogram(px.data.tips(), y="total_bill")