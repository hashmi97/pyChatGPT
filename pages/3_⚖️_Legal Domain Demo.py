import streamlit as st
from openai_conn import openai_conn, construct_message


conn = openai_conn()


st.title("LawGPT demo!")

with st.form("my_form"):
# Role info
    role = st.text_input("What type of role should I assume?", "Lawyer")

    # Main query
    question = st.text_input("What would you like me to do?", "Prepare an employment agreement}")

    # More data to use such as names and dates
    use_an_example = st.checkbox("I would like to provide an example", value=True)

    example = st.text_area("Insert any examples you'd like the system to emulate when coming up with a response",

                         '''Employee Contract Template:
Employment Contract

This contract, dated on the __ day of ____ in the year 20____, is made between [company name] and [employee name] of [city, state]. This document constitutes an employment agreement between these two parties and is governed by the laws of [state or district].

WHEREAS the Employer desires to retain the services of the Employee, and the Employee desires to render such services, these terms and conditions are set forth.

IN CONSIDERATION of this mutual understanding, the parties agree to the following terms and conditions:

Employment
The Employee agrees that he or she will faithfully and to the best of their ability to carry out the duties and responsibilities communicated to them by the Employer. The Employee shall comply with all company policies, rules and procedures at all times.

Position
As a [job title], it is the duty of the Employee to perform all essential job functions and duties. From time to time, the Employer may also add other duties within the reasonable scope of the Employee’s work.

Compensation
As compensation for the services provided, the Employee shall be paid a wage of $_______ [per hour/per annum] and will be subject to a(n) [quarterly/annual] performance review. All payments shall be subject to mandatory employment deductions (State & Federal Taxes, Social Security, Medicare).

Benefits
The Employee has the right to participate in any benefits plans offered by the Employer. The employer currently offers [list benefits, if any]. Access to these benefits will only be possible after the probationary period has passed.

Probationary Period
It is understood that the first [time frame] of employment constitutes a probationary period. During this time, the Employee is not eligible for paid time off or other benefits. During this time, the Employer also exercises the right to terminate employment at any time without advanced notice.

Paid Time Off
Following the probationary period, the Employee shall be eligible for the following paid time off: • [length of time for vacation] • [length of time for sick/personal days] • Bereavement leave may be granted if necessary.

The employer reserves the right to modify any paid time off policies.

Termination
It is the intention of both parties to form a long and mutually profitable relationship. However, this relationship may be terminated by either party at any time provided [length of time] written notice is delivered to the other party.
The Employee agrees to return any Employer property upon termination.

Non-Competition and Confidentiality
As an Employee, you will have access to confidential information that is the property of the Employer. You are not permitted to disclose this information outside of the Company.
During your time of Employment with the Employer, you may not engage in any work for another Employer that is related to or in competition with the Company. You will fully disclose to your Employer any other Employment relationships that you have and you will be permitted to seek other employment provided that (a.) it does not detract from your ability to fulfill your duties, and (b.) you are not assisting another organization in competing with the employer.

It is further acknowledged that upon termination of your employment, you will not solicit business from any of the Employer’s clients for a period of at least [time frame].

Entirety
This contract represents the entire agreement between the two parties and supersedes any previous written or oral agreement. This agreement may be modified at any time, provided the written consent of both the Employer and the Employee.

Legal Authorization
The Employee agree that he or she is fully authorized to work in [country name] and can provide proof of this with legal documentation. This documentation will be obtained by the Employer for legal records.

Severability
The parties agree that if any portion of this contract is found to be void or unenforceable, it shall be struck from the record and the remaining provisions will retain their full force and effect.

Jurisdiction
This contract shall be governed, interpreted, and construed in accordance with the laws of [state, province or territory].

In witness and agreement whereof, the Employer has executed this contract with due process through the authorization of official company agents and with the consent of the Employee, given here in writing.

Employee Signature

Date

Company Official Signature

Date''',
                           height=500)



    # More data to use such as names and dates
    use_params = st.checkbox("I would like to provide more information",  value=True)

    params = st.text_area("Insert any additional information you would like to be included in the final response",
                         "Starting Date: 20/03/2023,\nEmployer: PhazeRo,\nEmployee: Hisham Al Hashmi,\nCountry: Oman",
                          height=150)


    submitted = st.form_submit_button("Submit")

    if submitted:
        query = construct_message(role, question, (use_an_example, example), (use_params, params))

        response = openai_conn().create_chat(messages=query)
        st.subheader("The output of your query is")
        st.write(response['choices'][0]['message']['content'])
