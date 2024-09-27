import re
import json

with open("./MyData.json", "r") as mydata_f1:
    MyData = json.load(mydata_f1)

    user_message=input("You: ")
    user_words=re.split(r'\s+|[,;?.-]\s*',user_message.lower())

    score_list=[]
    for answer_data in MyData:
        req_words = answer_data["required_word"]
        othr_words = answer_data["other_words"]
        answer_sent = answer_data["response"] 

        required_word_count = 0
        for word in req_words:
            if word in user_words:
                required_word_count +=1

        other_word_count = 0
        for word in user_words:
            if word in othr_words:
                other_word_count +=1
        score_list.append(other_word_count)
    
    best_score = max(score_list)

    if best_score<1:
        print("Bot : Can you please rephrase you question ?")
    else:
        best_score_index = score_list.index(best_score)
        response_data = MyData[best_score_index]["response"]
        print("Bot : "+response_data)