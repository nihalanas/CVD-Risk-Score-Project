from transformers import pipeline

# Initialize the pipeline for LLM inference (replace "llama-base" with your model name)
generator = pipeline("text-generation", model="llama-base")

def phase_2(prompt):
  """
  This function takes a prompt as input and feeds it to Llama2, returning the model's output.

  Args:
      prompt: The text prompt for Llama2.

  Returns:
      The generated text by Llama2 based on the prompt.
  """
  # Generate text using the prompt
  response = generator(prompt, max_length=1024, return_dict=True)  # Adjust max_length as needed
  output_text = response[0]['generated_text']
  
  # Phase 3 likely expects plain text, remove special tokens
  output_text = output_text.strip()[len("[MASK]"):]  # Assuming "[MASK]" is the start token

  return output_text

# Example usage
my_prompt = "Write a poem about a cat"
phase_2_output = phase_2(my_prompt)
print(phase_2_output)

# Send the phase_2_output to your phase 3 function
#phase_3(phase_2_output)
