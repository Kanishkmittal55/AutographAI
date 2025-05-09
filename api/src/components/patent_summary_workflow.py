
from llm.openai import OpenAIChat
import httpx
from typing import Callable, List, Dict, Any
import tiktoken
import os
openai_key = os.getenv("OPENAI_API_KEY")
if not openai_key:
    raise RuntimeError("Missing OPENAI_API_KEY in environment")



# Now retrieve the API key as a string
api_key = openai_key

# Initialize LLM 
llm = OpenAIChat(
    openai_api_key=api_key, model_name="gpt-4o-mini", max_tokens=4096
)

async def openai_generate(prompt: str) -> str:
    """
    Sends a prompt to the OpenAI endpoint and returns the raw output.

    :param prompt: The input prompt to send to the OpenAI API.
    :return: The raw output generated by the OpenAI API.
    """
    messages = [
        {"role": "user", "content": prompt}  # Construct the message payload
    ]
    print(f"Sending request to OpenAI endpoint with messages: {messages}")
    
    # Assuming `llm.generate()` is correctly configured to accept the messages
    output = llm.generate(messages)
    print("The output is:", output)
    return output

async def calculate_max_tokens_per_chunk() -> int:
    # This depends on the section of the patent we are trying to analyse so 
    # Section of the patent we are trying to analyse , this is again a revolutionary idea
    # Now to solve our context problem we break that main context down to smaller context being maintained for new information coming in.
    # So first we need to calculate the number of sections present in the patent or research document.
    # No of context windows atleast equal to the number of sections in the patent document or greater than it.
    # So we will go section by section , the same subgraph will be populated for every new meaningfull secret extracted.
    return -1

async def process(chunk: str, provider: str) -> str:
    """
    Process a single chunk by making an asynchronous request to the specified provider's endpoint.
    :param chunk: The chunk to process.
    :param provider: The provider name (e.g., "ollama", "openai", "groq").
    :return: The processed response as a string.
    """
    try:
        # Prepare the request payload with only the chunk (prompt)
        payload = {
            "prompt": chunk  # Assuming the API expects a field named "chunk" for the prompt
        }

        # Route to appropriate provider using a match-case structure
        if provider == "ollama":
            print(f"Sending request to http://localhost:7860/ollama/chat with payload: {payload}")
            async with httpx.AsyncClient() as client:
                response = await client.post("http://localhost:7860/ollama/chat", json=payload)
            response.raise_for_status()
            result = response.json()
            message = result.get('generated_text', {}).get('message', {})
            content = message.get('content', None)

        elif provider == "openai":
            output = await openai_generate(chunk)
            return output

        elif provider == "groq":
            print(f"Sending request to Groq endpoint with payload: {payload}")
            async with httpx.AsyncClient() as client:
                response = await client.post("http://localhost:7860/groq/chat", json=payload)
            response.raise_for_status()
            result = response.json()
            content = result.get('response', None)  # Adjust based on Groq's API response structure

        else:
            raise ValueError(f"Unsupported provider: {provider}")

        return content

    except httpx.RequestError as e:
        print(f"Error communicating with {provider}: {e}")
        return f"Error: {e}"
    except ValueError as e:
        print(f"Invalid JSON received from {provider}: {e}")
        return f"Invalid JSON received: {e}"
    
async def research_or_patent_classifier(chunk: str, provider: str) -> str:
    research_patent_classifier = f"""
    ### Input:
    {chunk}

    ### Instruction:
    You are a smart assistant and your job is to classify the document , based on the input chunk above classify into either a patent or a research paper, you will only answer in true or false , "True" for research paper and "False" for patent document, dont add any extra comments or suggestions.
    """

    # Send the prompt to the LLM model to classify the document
    classification_response = await process(research_patent_classifier, provider)
    print("The classification response is :", classification_response)

    return classification_response

def splitString(string, max_length) -> List[str]:
    return [string[i : i + max_length] for i in range(0, len(string), max_length)]

def num_tokens_from_string(string: str) -> int: 
    """
    Estimate the number of tokens in a string using the LLaMA tokenizer.
    :param string: The input string.
    :return: The number of tokens in the string.
    """
    # Use tiktoken's cl100k_base tokenizer to encode the input string
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(string)
    return len(tokens)

def splitDataIntoChunksOf(max_token_chunk_size: int, token_size_of_prompt_to_be_used: int, data: str) -> List[str]:
    # So this allowed tokens is the bandwidth we have , we set a max allowed tokens for the chunk, and substract the input token size of the prompt to be used from it before only so that only the remaining space is filled.
    allowed_tokens = max_token_chunk_size - token_size_of_prompt_to_be_used
    print("The allowed tokens for the chunk is :", allowed_tokens)
    chunked_data = splitString(data, 500)  # Split based on approximate length
    print("The number of chunks created are :", len(chunked_data))

    combined_chunks = []
    current_chunk = ""
    
    for chunk in chunked_data:
        # Calculate token count for the combined chunk
        current_chunk_tokens = num_tokens_from_string(current_chunk)
        chunk_tokens = num_tokens_from_string(chunk)
        print("The number of token the prompt had is fixed at 200 , and the number of tokens in the chunk is :", chunk_tokens)

        if current_chunk_tokens + chunk_tokens <= allowed_tokens:
            current_chunk += chunk
        else:
            # Append the non-empty current chunk and start a new one
            if current_chunk.strip():
                combined_chunks.append(current_chunk.strip())
            current_chunk = chunk
    
    # Append any remaining chunk after the loop
    if current_chunk.strip():
        combined_chunks.append(current_chunk.strip())

    return combined_chunks

async def extract_sections_from_research(chunk: str, provider: str) -> List[str]:

    # output_format = """
    # {
    # "patent_no": "the_patent_number_of_the_document",
    # "sections": [
    #     "section1",
    #     "section2",
    #     "section3"
    #     ]
    # }
    # """

    # # A better chunking output response.
    # # output_format = """
    # # {
    # # "patent_no": "US1234567",
    # # "sections": [
    # #     {"name":"section1", "starting_sentence":"first sentence of section1", "ending_sentence":"last sentence of section1"},
    # #     {"name":"section2", "starting_sentence":"first sentence of section2", "ending_sentence":"last sentence of section2"},
    # #     {"name":"section3", "starting_sentence":"first sentence of section3", "ending_sentence":"last sentence of section3"}
    # #     ]
    # # }
    # # """

    research_paper_prompt = f"""
    ### Document:
    {chunk}

    ### Instruction:
    You are a data scientist working for a company that is trying to analyse new research papers. Your task is to extract the sections from the given document which will be a research paper. Provide the extracted sections and sub-sections in a list format. If no sections and subsections are found, respond with "No sections or subsections found in this chunk". Dont include any extra comments , suggestions or notes. Also for the purpose of verifiction I need the first (10 words or first sentence) and (last 10 words or the last sentence) of the section and subsection recognized. You will only inlclude the sections and subsections like shown below:

    Section : name of the section, first 10 words or first sentence, last 10 words or last sentence 
    Subsection : name of the subsection section, first 10 words or first sentence, last 10 words or last sentence.

    So the above output for all the sections and subsections found in the document.
    """

    # Send the prompt to the LLM model to extract the sections
    sections_response = await process(research_paper_prompt, provider)
    print("The sections response is :", sections_response)

    # Extract the sections from the response
    sections = sections_response.split("\n")
    print("The extracted sections are :", sections)

    return sections

async def extract_sections_from_patent(chunk: str, provider: str) -> List[str]:
    # Define the prompt for extracting the sections
    patent_prompt = f"""
    ### Document:
    {chunk}

    ### Instruction:
    You are a data scientist working for a company that is building a report for a patent document. Your task is to extract the sections from the given document which will a patent document confusing and hard to read. Provide the extracted sections and sub-sections in a list format. If no sections and subsections are found, respond with "No sections or subsections found in this chunk". Dont include any extra comments , suggestions or notes. Also for the purpose of verifiction I need the first (10 words or first sentence) and (last 10 words or the last sentence) of the section and subsection recognized. You will only inlclude the sections and subsections like shown below:

    Section : name of the section, first 10 words or first sentence, last 10 words or last sentence 
    Subsection : name of the subsection section, first 10 words or first sentence, last 10 words or last sentence.

    So the above output for all the sections and subsections found in the document.
    """

    # Send the prompt to the LLM model to extract the sections
    sections_response = await process(patent_prompt, provider)
    print("The sections response is :", sections_response)

    # Extract the sections from the response
    sections = sections_response.split("\n")
    print("The extracted sections are :", sections)

    return sections


async def patent_summary_workflow(chunked_data: List[str], provider: str) -> List[dict]:
    unique_sections = set()

    # Here we have the information that the document is a patent.
    for i, chunk in enumerate(chunked_data, start=1):
        print(f"\nProcessing Chunk {i}:")

        sections = await extract_sections_from_patent(chunk, provider)
        print(f"Chunk {i} processed response: {sections}")

        # Convert sections to lowercase and add to the set for uniqueness
        for section in sections:
            unique_sections.add(section.lower())

    return list(unique_sections)


async def research_summary_workflow(chunked_data: List[str], provider: str) -> List[dict]:
    unique_sections = set()

    # Here we have the information that the document is a research paper.
    for i, chunk in enumerate(chunked_data, start=1):
        print(f"\nProcessing Chunk {i}:")

        sections = await extract_sections_from_research(chunk, provider)
        print(f"Chunk {i} processed response: {sections}")

        # Convert sections to lowercase and add to the set for uniqueness
        for section in sections:
            unique_sections.add(section.lower())

    return list(unique_sections)

async def new_section_workflow(sentences: List[str], provider: str) -> List[dict]:
     prompt = f"""
        You are a data scientist analyzing a patent document.
        Now you will get a sentence from the document , now based on this line
        you will have to first classify that line has a section or not, if it is a section then you would return the name

        Chunk:
        {chunk}
        """


async def workflow_classifier(data: str, provider: str) -> List[str]:
   # The Ground rules the final JSON ojbect will be a list of dictionaries or json object.
    print("Patent Summarization worlflow started")

    # So we before finding the sections we need to now cut the chunks of the patent or research document.
    # The Input size is variable for different tasks we do with the chunk.
    # For example the number of tokens in the section discovery prompt would be different from the number 
    # of tokens in the summarization prompt, so for now we calculate the number of tokens in the section 
    # discovery prompt manually and provide the number.
    chunked_data = splitDataIntoChunksOf(4096, 200, data)
    print("The number of chunks created are :", len(chunked_data))

    # Section deduction of the patent or research document.
    # We could string manipulation to find the sections in the document.
    # We use LLMs to find that too.

    research = None
    combined_chunks = ""
    num_chunks_to_combine = min(2, len(chunked_data))
    
    # First Loop to decide whether the document is a patent or a research paper.
    for i in range(num_chunks_to_combine):
        combined_chunks += chunked_data[i]

    # Now pass the combined text for classification
    print("Processing combined chunks for classification...")
    research = await research_or_patent_classifier(combined_chunks, provider)
    print("Research or Patent Classifier Response:", research)

    lines = None

    if research == "True":
        # print("The document is a research paper.")
        # sections = await research_summary_workflow(chunked_data, provider)
        lines = data.split("\n")
        print("The research lines are :", lines)
        print("The length of the research lines are :", len(lines))

        sentences = []
        for i, line in enumerate(lines):
            print(f"\033[91mThe line {i+1} is - {line}\033[0m")
            sentences.extend(line.split('.'))

        print("The sentences are :", sentences)
        print("The number of sentences are :", len(sentences))
        sections = await new_section_workflow(sentences, provider)
    else:
        # print("The document is a patent document.")
        # sections = await patent_summary_workflow(chunked_data, provider)
        lines = data.split("\n")
        print("The research lines are :", lines)
        print("The length of the research lines are :", len(lines))

        sentences = []
        for i, line in enumerate(lines):
            print(f"\033[91mThe line {i+1} is - {line}\033[0m")
            sentences.extend(line.split('.'))

        print("The sentences are :", sentences)
        print("The number of sentences are :", len(sentences))

    return sentences
