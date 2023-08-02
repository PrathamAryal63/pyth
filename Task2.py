import pandas as pd
import matplotlib.pyplot as plt

# Load data from "cities.csv" into a DataFrame called 'cities_df'
cities_df = pd.read_csv("cities.csv")

# Load data from "continents.csv" into a DataFrame called 'continents_df'
continents_df = pd.read_csv("continents.csv")

# Calculate the total land area for each continent
total_land_area_by_continent = cities_df.groupby("continent")["area"].sum().reset_index()

# Merge the land area data with the continents data
merged_df = total_land_area_by_continent.merge(continents_df, on="continent")

# Create the bar plot for land area by continent
plt.figure(figsize=(10, 6))
plt.bar(merged_df["continent"], merged_df["area"], color="skyblue")
plt.xlabel("Continent")
plt.ylabel("Land Area (sq.km)")
plt.title("Land Area by Continent")
plt.xticks(rotation=45)
plt.show()

# Find cities with highest elevation for each continent
highest_elevation_cities = cities_df.groupby("continent").apply(lambda x: x.nlargest(1, "elevation")).reset_index(drop=True)

# Find cities with lowest elevation for each continent
lowest_elevation_cities = cities_df.groupby("continent").apply(lambda x: x.nsmallest(1, "elevation")).reset_index(drop=True)

# Display the cities with highest and lowest elevation for each continent
print("Cities with highest elevation by continent:")
print(highest_elevation_cities[["continent", "city", "elevation", "latitude", "longitude"]])

print("\nCities with lowest elevation by continent:")
print(lowest_elevation_cities[["continent", "city", "elevation", "latitude", "longitude"]])

# Calculate population density for each city
cities_df["population_density"] = cities_df["population"] / cities_df["area"]

# Sort cities based on population density in ascending order (lowest density first)
cities_lowest_density = cities_df.sort_values("population_density").head(5)

# Sort cities based on population density in descending order (highest density first)
cities_highest_density = cities_df.sort_values("population_density", ascending=False).head(5)

# Display the cities with the lowest and highest population density
print("\nCities with the lowest population density:")
print(cities_lowest_density[["city", "country", "continent", "population_density"]])

print("\nCities with the highest population density:")
print(cities_highest_density[["city", "country", "continent", "population_density"]])
