import userInterface as userInterface
import TextSuggestion as TextSugg
#從userInterface.py中導入哪個checkbox被選擇
#如果IAI被勾選則從TextSuggestion.py中導入IAI的建議
selected_checkbox = userInterface.get_selected_checkbox()

def get_suggestion():
    if selected_checkbox == "IAI":
        return TextSugg.SuggestionKey["IAI"]
    elif selected_checkbox == "CAP":
        return TextSugg.SuggestionKey["CAP"]
    elif selected_checkbox == "HAP":
        return TextSugg.SuggestionKey["HAP"]
    else:
        return "No suggestion available for the selected condition."



