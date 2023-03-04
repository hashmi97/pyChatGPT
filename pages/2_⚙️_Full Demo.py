import streamlit as st
from openai_conn import openai_conn, construct_message


conn = openai_conn()

m = [{"role": "system", "content": "You are a lawyer writing a document."},
    {"role": "user",
     "content": "with referencing the following data, write an employment agreement document"}]

st.title("allGPT demo!")

with st.form("my_form"):
# Role info
    role = st.text_input("What type of role should I assume?", "Storyteller")

    # Main query
    question = st.text_input("What would you like me to do?", "Write a short story about a firefighter")

    # More data to use such as names and dates
    use_an_example = st.checkbox("I would like to provide an example")

    example = st.text_area("Insert any examples you'd like the system to emulate when coming up with a response",
                           "",
                           height=500)



    # More data to use such as names and dates
    use_params = st.checkbox("I would like to provide more information")

    params = st.text_area("Insert any additional information you would like to be included in the final response",
                         "The name of the firefighter is John",
                          height=150)


    submitted = st.form_submit_button("Submit")

    if submitted:
        query = construct_message(role, question, (use_an_example, example), (use_params, params))

        response = openai_conn().create_chat(messages=query)
        st.subheader("The output of your query is")
        st.write(response['choices'][0]['message']['content'])
