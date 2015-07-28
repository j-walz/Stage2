# Puts the information in HTML form

def generate_concept_html(con_title, con_description):
    html_title = '''
<div class = "concept">
     <div class = "concept-title">
          ''' + con_title
    html_description = '''
     </div>
     <div class = "concept-description">
          ''' + con_description
    html_close_tag = '''
     </div>
</div>'''
    full_html_text = html_text1 + html_text2 + html_text3
    return full_html_text

# Gets the descrption part of a piece of foramated text
def get_description(concept):
    start = concept.find("DESCRIPTION")
    stop = concept.find("TITLE", start)
    description = concept[start + 13: stop]
    return description
# Gets the title part of a piece of foramated text
def get_title(concept):
    start = concept.find(":")
    stop = concept.find("DESCRIPTION")
    title = concept[start + 1: stop]
    return title
# Gets a specified title and description from formatted text
def get_concept_by_number(text, concept_number):
    count = 0
    while count < concept_number:
        count +=1
        start = text.find("TITLE")
        stop = text.find("TITLE", start + 1)
        if stop >= 0:
            final_concept = text[start:stop]
        else:
            stop = len(text)
            final_concept = text[start:]
        text = text[stop:]
    return final_concept
    
    
# Puts all of the formatted text in HTML format
def generate_all_html(text):
    con_num = 1
    concept = get_concept_by_number(text, con_num)
    html = ""
    while concept != "":
        title = get_title(concept)
        description = get_description(concept)
        html = html + generate_concept_HTML(title, description)
        con_num += 1
        concept = get_concept_by_number(text, con_num)
    return html

