addons_path = "/mnt/c/Users/keene/AppData/Roaming/Anki2/addons21/"

theme = input("Enter theme name: ")
if theme == "":
    theme = "gruvbox-material-dark-medium"

with open("newschemes/" + theme + ".yaml", "r") as file:
    lines = file.readlines()

base00 = str(lines[2][9:15])
base01 = str(lines[3][9:15])
base02 = str(lines[4][9:15])
base03 = str(lines[5][9:15])
base04 = str(lines[6][9:15])
base05 = str(lines[7][9:15])
base06 = str(lines[8][9:15])
base07 = str(lines[9][9:15])
base08 = str(lines[10][9:15])
base09 = str(lines[11][9:15])
base0A = str(lines[12][9:15])
base0B = str(lines[13][9:15])
base0C = str(lines[14][9:15])
base0D = str(lines[15][9:15])
base0E = str(lines[16][9:15])
base0F = str(lines[17][9:15])

with open("theme.json", "r") as file:
    lines = file.readlines()

replacements = {
    "ACCENT_CARD": base0D,
    "ACCENT_DANGER": base08,
    "ACCENT_NOTE": base0B,
    "\"BORDER\"": base03,
    "BORDER_FOCUS": base07,
    "BORDER_STRONG": base04,
    "BORDER_SUBTLE": base02,
    "BUTTON_BG": base02,
    "BUTTON_DISABLED": base02,
    "\"BUTTON_HOVER\"": base03,
    "BUTTON_HOVER_BORDER": base04,
    "BUTTON_PRIMARY": base0D,
    "\"CANVAS\"": base00,
    "CANVAS_CODE": base01,
    "CANVAS_ELEVATED": base01,
    "CANVAS_GLASS": base01 + "66",
    "CANVAS_OVERLAY": base01,
    "\"FG\"": base07,
    "FG_DISABLED": base06,
    "FG_FAINT": base05,
    "FG_LINK": base07,
    "FG_SUBTLE": base06,
    "FLAG_1": base08,
    "FLAG_2": base09,
    "FLAG_3": base0B,
    "FLAG_4": base0D,
    "FLAG_5": base0E,
    "FLAG_6": base0C,
    "FLAG_7": base07,
    "HIGHLIGHT_BG": base02,
    "HIGHLIGHT_FG": base07,
    "\"SCROLLBAR_BG\"": base00,
    "SCROLLBAR_BG_ACTIVE": base02,
    "SCROLLBAR_BG_HOVER": base00,
    "SELECTED_BG": base02,
    "SELECTED_FG": base07,
    "SHADOW": base00,
    "SHADOW_FOCUS": base09,
    "SHADOW_SUBTLE": base01,
    "STATE_BURIED": base02,
    "STATE_LEARN": base08,
    "STATE_MARKED": base07,
    "STATE_NEW": base0D,
    "STATE_REVIEW": base0B,
    "STATE_SUSPENDED": base06,
}

# Iterate through lines and replace accordingly
for i, line in enumerate(lines):
    for key, value in replacements.items():
        if key in line:
            lines[i + 2] = f'            "#{value}",\n'
            lines[i + 3] = f'            "#{value}",\n'

with open(addons_path + "688199788/themes/" + theme.replace("-", " ").title() + ".json", "w") as file:
    file.writelines(lines)

with open(addons_path + "494384865/config.json", "r") as file:
    lines = file.readlines()

lines[7] = f'    "2 answers": ["#{base09}", "#{base0B}"],\n'
lines[8] = f'    "3 answers": ["#{base09}", "#{base0B}", "#{base0D}"],\n'
lines[9] = f'    "4 answers": ["#{base09}", "#{base0A}", "#{base0B}", "#{base0D}"]\n'

with open(addons_path + "2494384865/config.json", "w") as file:
    file.writelines(lines)
