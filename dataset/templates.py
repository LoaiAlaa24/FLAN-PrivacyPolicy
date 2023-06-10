"""Templates for FLAN."""

# pylint: disable=line-too-long

PATTERNS = {
    'q&a': [
        ('Answer this question: \n\n{question} \n\ncontext: {context}'),
        ('Answer this question: \n\n{question} \n\ncontext: {context} \n\nanswer:{answer}')
    ],
    'opp115':[
        ('Text:\n{text}\nSelect the topics that this text is about?\nOPTIONS:\n-Data Retention \n-Data Security \n-Do Not Track \n-First Party Collection/Use \n-International and Specific Audiences \n-Introductory/Generic \n-Policy Change \n-Practice not covered \n-Privacy contact information \n-Third Party Sharing/Collection \n-User Access, Edit and Deletion \n-User Choice/Control')
    ],
    'policy_detection':[
        ('Text:\n{text}\nIs this text policy?\nOPTIONS:\n-Policy\n-Not Policy')
    ],
    'policy_ie_a':[
        ('Text:\n{text}\nWhich topic is this text about?\nOPTIONS:\n-Data Collection Usage\n-Not Policy')
    ],
    'privacy_qa':[
        ('Classify the relevance of the answer to the question:\n\nquestion: {question}\n\n answer: {answer} \n\nIs this answer relevant?\n\nOPTIONS:\n-Relevant \n-Irrelevant')
    ],
    
}