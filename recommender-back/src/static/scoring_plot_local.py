# File to easily test the scoring without dependencies to anything
# Includes basic plot structure
import pandas as pd
import seaborn as sns
import math as math
from matplotlib import pyplot as plt

def get_out_score(temperature, wind_speed, humidity, precipitation, clouds, sunrise, sunset, cur_time):
    '''
    Calculates an outdoor score based on weather conditions and time.

    Args:
        temperature (float): Air temperature.
        wind_speed (float): Wind speed.
        humidity (float): Humidity level.
        precipitation (float): Precipitation amount.
        clouds (float): Cloud coverage.
        sunrise (str): Sunrise time in HH:MM format.
        sunset (str): Sunset time in HH:MM format.
        cur_time (str): Current time in HH:MM format.

    Returns:
        float: Calculated outdoor score.
    '''
    precipitation_weight = 0.35
    temperature_weight = 0.3
    clouds_weight = 0.04
    wind_speed_weight = 0.04
    humidity_weight = 0.02
    score = precipitation_weight * math.exp(-precipitation)
    temperature_comp = 0
    if 20 <= temperature <= 25:
        temperature_comp = 1
    elif temperature < 20:
        temperature_comp = math.exp(-0.1 * (20 - temperature))
    else:
        temperature_comp = math.exp(0.1 * (25 - temperature))
    score += temperature_weight * temperature_comp
    if sunrise <= cur_time <= sunset:
        day_time_weight = 0.2
        score += day_time_weight
    score += clouds_weight * math.exp(-clouds)
    score += wind_speed_weight * math.exp(-wind_speed)
    if 0.4 <= humidity <= 0.55:
        humidity_weight = 0.02
        score += humidity_weight
    return score

def get_in_score(temperature, wind_speed, humidity, precipitation, clouds, sunrise, sunset, cur_time):
    '''
    Calculates an indoor score based on weather conditions and time.

    Args:
        temperature (float): Air temperature.
        wind_speed (float): Wind speed.
        humidity (float): Humidity level.
        precipitation (float): Precipitation amount.
        clouds (float): Cloud coverage.
        sunrise (str): Sunrise time in HH:MM format.
        sunset (str): Sunset time in HH:MM format.
        cur_time (str): Current time in HH:MM format.

    Returns:
        float: Calculated indoor score.
    '''
    precipitation_weight = 0.7
    temperature_weight = 0.1
    clouds_weight = 0.04
    wind_speed_weight = 0.03
    score = precipitation_weight * (1 - math.exp(-10 * precipitation))
    temperature_comp = 0
    if 20 <= temperature <= 25:
        temperature_comp = 0
    elif temperature < 20:
        temperature_comp = 1 - math.exp(-0.04 * (20 - temperature))
    else:
        temperature_comp = 1 - math.exp(0.2 * (25 - temperature))
    score += temperature_weight * temperature_comp
    if sunrise > cur_time or cur_time > sunset:
        day_time_weight = 0.06
        score += day_time_weight
    score += clouds_weight * (1 - math.exp(-3 * clouds))
    score += wind_speed_weight * (1 - math.exp(-0.3 * wind_speed))
    if humidity < 0.4 or humidity > 0.55:
        humidity_weight = 0.02
        score += humidity_weight
    return score

def build_chart(var_vals, scores, label):
    '''
    Builds and displays a chart to visualize scores.

    Args:
        var_vals (list): List of variable values.
        scores (list): List of corresponding scores.
        label (str): Label for the x-axis.

    Displays a chart to visualize the relationship between variable values and scores.
    '''
    var_df= pd.DataFrame({"var" : var_vals, "score" : scores})
    fig, ax = plt.subplots(figsize=(4, 4))
    sns.lineplot(data=var_df, x="var", y="score", ax=ax)
    ax.set_xlabel(label, fontsize=15)
    ax.set_ylabel("score", fontsize=15)
    ax.tick_params(labelsize=15)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Test cases and plot generation...
    print('Outdoor')
    print("min", get_out_score(-40, 20, 0.9, 20, 0.9,"06:00", '20:00', '23:00'))
    # Expected 0.01700...
    print("max", get_out_score(24, 0, 0.5, 0, 0, '06:00' , '20:00', '10:00'))
    # Expected 1
    print('Indoor')
    print("min", get_in_score(24, 0, 0.5, 0, 0, '06:00' , '20:00', '10:00'))
    # Expected 0
    var_vals= [*range(-40, 40)]
    scores = [get_out_score(var, 0, 0.5, 0, 0,"06:00", '20:00', '23:00') for var in var_vals]
    build_chart(var_vals, scores, "temperature")
