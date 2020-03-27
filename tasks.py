import json
import copy

from invoke import context

def build_colors():

    base_colors = ["#43B9D8", "#43bad875", "#FD971F"]

    features = {
        "orange": ["#FD971F", "#FD971F75", "#e7dc60" ],
        "green": ["#A6E22E", "#A6E22E75", "#43B9D8" ],
        "purple": ["#AE81FF", "#AE81FF75", "#43B9D8"],
        "yellow": ["#e7dc60", "#e7dc6075", "#FD971F"],
        "red": ["#f82a5d", "#f82a5d75", "#e7dc60"],
        "gray": ["#8f8f8f", "#8f8f8f75", "#43B9D8"],
        "white": ["#f1f1f1", "#f1f1f175", "#43B9D8"],
    }

    with open("themes/Monokai-Charcoal.json") as f:
        base_theme = json.load(f)

    for feature_name, colors in features.items():
        theme = copy.deepcopy(base_theme)
        theme["name"] = theme["name"] + f" ({feature_name})"

        for name, hex_code in theme["colors"].items():
            for i, base_hex_code in enumerate(base_colors):
                if base_hex_code == hex_code:
                    theme["colors"][name] = colors[i]

        file_name = f"themes/Monokai-Charcoal-{feature_name}.json"
        with open(file_name, "w") as f:
            json.dump(theme, f)
        context.Context().run(f"prettier --write {file_name}")


if __name__ == "__main__":
    build_colors()