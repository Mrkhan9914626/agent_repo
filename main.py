from openai import OpenAI

client = OpenAI()

# Create an assistant
assistant = client.beta.assistants.create(
    name="Helpful assistant",
    instructions="You are a helpful assistant. You can help users with their general queries.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4-1106-preview"
)

# Create a thread
thread = client.beta.threads.create()

# Add a message to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I need help with a general query."
)

# Run the assistant
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="Please address the user as Mujeeb ur Rehman."
)

print(run)