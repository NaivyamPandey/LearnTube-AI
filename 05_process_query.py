import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from 04_chunking import create_embedding

df = pd.read_pickle("chunks.pkl")

incoming_query = input("Ask your question? : ")
query_embedding = create_embedding([incoming_query])[0]

similarities = cosine_similarity(np.vstack(df['embedding']), [query_embedding]).flatten()

top_indices = 30

top_results = similarities.argsort()[::-1][:top_indices]

df_result = df.loc[top_results, ['start', 'end', 'text', 'video_name']]

print(df_result.head())

prompt = f"""
You are a helpful assistant that answers questions based on the following context:
I am teaching NextJs on youtube and i have all the chunks of the videos in my data frame and i have seperated some dataframe based on the similarity of the chunks to the query. I want you to answer the question based on the context provided below. If you don't know the answer, just say "I don't know". Do not try to make up an answer.
 ---------------------------------------------
 Here is the query: "{incoming_query}"
----------------------------------------------
You have the query and the chunks which include text, start time, end time and video name. You have to tell me the answer for the question user asked in form of query and you have to tell me what is the video name what is the start time and what is the end time of the chunk which is most relevant to the query. You have to tell me the answer in a very concise manner. If you don't know the answer, just say "I don't know". Do not try to make up an answer.
----------------------------------------------
Here is the chunks which are most relevant to the query:
{df_result.to_string(index=False)}
"""

with open("prompt.txt", "w", encoding="utf-8") as f:
    f.write(prompt)