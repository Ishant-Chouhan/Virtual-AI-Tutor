import weaviate
import google.generativeai as genai
import asyncio
import edge_tts

async def get_voice(text):
    communicate = edge_tts.Communicate(text, "en-IN-NeerjaNeural",rate="+10%")
    await communicate.save("output.mp3")
    print("Audio saved as output.mp3")


client = weaviate.connect_to_local()
questions = client.collections.get("School")

history=dict() # to store the history


while True:
    print("------------------------------------------")
    query=input("Ask Question: ")
    print("------------------------------------------")
    response = questions.generate.near_text(
        query=query,
        limit=5,
        grouped_task=f"you are a teacher, teaching a student and giving a mature and simplified in easy indian english answer in 500 words to thier query that is {query} ,a dicionary is given that is {history} it is history of the questions that student has asked previously along with the answers you have given means in ( query : answer format ) so that you should give answer accordingly. You should behave like you know the answer and don't reveal that you are using any reference."
    )

    from_rag=response.generated



    genai.configure(api_key="AIzaSyC3pCAiP_jYxMrYO8C6alZzCYTrP11EE8A")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"you are a teacher, teaching a student and giving a mature and simplified answer in easy english. It should be in 100 words. the query asked by that student is{query} in english, here is an output coming from a RAG model that is {from_rag} and a dicionary is given that is {history} it is history of the questions that student has asked previously along with the answers you have given means in ( query : answer format ) so that you should give answer accordingly. Don't reveal that you are using any reference and don't use any kind of  character like '*' and only use paragraph.")
    mytext=response.text
    print(mytext)
    history[query]=mytext
    asyncio.run(get_voice(mytext))




client.close()
print("successfully connected!!!")