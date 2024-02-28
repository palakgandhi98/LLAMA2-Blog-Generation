import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
##Function to get response from llama 2 model
def getLLamaresponse(input_text,no_words,blog_style):
    ##LLama 2 Model
    llm = CTransformers(model='model/llama-2-7b-chat.ggmlv3.q8_0.bin', model_type='llama', config={'max_new_tokens':256,'temperature':0.01})
    ## Prompt Template

    template="""Write a blog for {blog_style} job profile for a topic {input_text} within {no_words} words."""
    
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],template=template)
    
    ## Generate the ressponse from the LLama 2 model
    response=llm.invoke(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(response)
    return response

    

#streamlit config
st.set_page_config(page_title="Generate Blogs",page_icon='🤖',layout='centered',initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text=st.text_input("Enter the Blog Topic")

## creating to more columns for additonal 2 fields

col1,col2=st.columns([5,5])

with col1:
    no_words=st.text_input('No of Words')
with col2:
    blog_style=st.selectbox('Writing the blog for',('Researchers','Data Scientist','Common People'),index=0)
    
submit=st.button("Generate")

## Final response
if submit:
       # Validate input (optional)
    try:
        no_words = int(no_words)
        if no_words <= 0:
            raise ValueError("Number of words must be positive")
    except ValueError:
        st.error("Invalid number of words. Please enter a positive integer.")
    else:
        # Generate response and display
        response = getLLamaresponse(input_text, no_words, blog_style)
        st.write(response)
