import os
import argparse
import json
import sys
from dotenv import load_dotenv
from openai import OpenAI
from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

if api_key == None:
    raise RuntimeError("environment variable wasn't found")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true",
                    help="Enable verbose output")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

max_iters = 20
success = False

for _ in range(max_iters):

    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    usage = response.usage

    if usage == None:
        raise RuntimeError("There is no usage")

    verbose_flag = args.verbose

    if verbose_flag:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {usage.prompt_tokens}")
        print(f"Response tokens: {usage.completion_tokens}")

    message = response.choices[0].message
    messages.append(message)

    result_message = {}
    if message.tool_calls:
        for function_call_part in message.tool_calls:
            result_message = call_function(function_call_part, verbose_flag)
            messages.append(result_message)

            if not result_message.get("content"):
                print("Error: no content on the message")

            if verbose_flag:
                print(f"-> {result_message['content']}")
    else:
        success = True
        print("Final response:")
        print(message.content)
        break

if not success:
    sys.exit(1)
