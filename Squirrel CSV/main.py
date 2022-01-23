import pandas
data = pandas.read_csv("squirrel_data.csv")
fur_color = data["Primary Fur Color"]
output = {
    "color": [],
    "count": [],
}
for color in fur_color:
    color = str(color)
    if color == "nan":
        continue

    if color in output["color"]:
        pos = output["color"].index(color)
        output["count"][pos] += 1
        continue
    output["color"].append(color)
    output["count"].append(1)
final = pandas.DataFrame(output)
final.to_csv("color_data.csv")
