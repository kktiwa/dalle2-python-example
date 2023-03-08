from dalle2 import Dalle2
import pandas as pd

dalle = Dalle2("sess-wSHBpDydzRMfk0M8F11QEnGyWGREpltaCKMs3Soe")  # your bearer key

toy_items = pd.read_csv("data/toy_list.csv")
items = toy_items.to_dict(orient="records")
matching_ids = [29]
matching_item = [d for d in items if d['style_ref'] in matching_ids]

for i in matching_item:
    text = "Women's" + " " + i["Colour"] + " " + i["Style "] + " " + i["Sleeve length"] + " " + i[
        "sleeve shape"] + " " + i["neck shape"] + " " + i[
               "Fabric Composition"] + " " + i["Pattern"] + " " + "pattern"
    generations = dalle.generate_and_download(text)
