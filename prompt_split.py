rule = """The total length of the content that I want to send you is too large to send in only one piece.
For sending you that content, I will follow this rule:    
[START PART 1/10]
this is the content of the part 1 out of 10 in total
[END PART 1/10]      
Then you just answer: "Received part 1/10"
And when I tell you "ALL PARTS SENT", then you can continue processing the data and answering my requests."""

prefix = """Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part 2/6 received" and wait for the next part.
[START PART 2/6]
"""
postfix = ""

def prompts_split(separeted_text_list: list[str]) -> list[str]:
    '''
    separeted_text_list должен хранить список разделенных текстов.
    Example:
    separeted_text_list # [str_less_1500_characters, ...]
    or
    separeted_text_list # [str_less_500_words, ...]
    '''
    handled_text = []
    if len(separeted_text_list) <= 1:
        return separeted_text_list
    
    handled_text.append(rule)
    for i,chunk in enumerate(separeted_text_list):
        handled_text.append(f"""Do not answer yet. This is just another part of the text I want to send you. Just receive and acknowledge as "Part {i+1}/{len(separeted_text_list)} received" and wait for the next part.
[START PART {i+1}/{len(separeted_text_list)}]
{chunk}
[END PART {i+1}/{len(separeted_text_list)}]
Remember not answering yet. Just acknowledge you received this part with the message "Part {i+1}/{len(separeted_text_list)} received" and wait for the next part.""")

    return handled_text

if __name__ == "__main__":
    print(len(rule))