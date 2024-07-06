from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig, pipeline
import torch
import os


#ADD YOUR TOKEN HERE 

#UNCOMMENT THE BELOW LINE AND ADD YOUR 
# os.environ["HF_TOKEN"] = "YOUR_TOKEN_HERE"

class BasicBot:

    def __init__(self) -> None:
        model_id = "microsoft/Phi-3-mini-128k-instruct"
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        llama_quantization_config = BitsAndBytesConfig(load_in_4bit=True)

        model = AutoModelForCausalLM.from_pretrained(
            model_id,
            quantization_config=llama_quantization_config,
            device_map="auto",
            torch_dtype="auto",
            trust_remote_code=True
        )

        self.pipe = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer
        )
        self.conversation_history = [
            {"role": "system", "content": "Respond to the user query like a human. Don't think that you are AI. If user is greating then greet"}
        ]
        self.user_data = {}
        self.ask_questions = []

    def generate_response(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})

        generational_args = {
            "max_new_tokens": 500,
            "return_full_text": False,
            "temperature": 0.1,
            "do_sample": False
        }

        output = self.pipe(self.conversation_history, **generational_args)
        response = output[0]["generated_text"]

        self.conversation_history.append({"role": "system", "content": response})
        return response
    
    def handle_interaction(self, user_response):
        if len(self.ask_questions) == 0:
            response = self.generate_response(f"{user_response}") + " What's your name?"
            self.ask_questions.append("What's your name?")

        elif "What's your email?" != self.ask_questions[-1] and "What's your email?" not in self.ask_questions:
            if self.ask_questions[-1] == "What's your name?":
                self.user_data["name"] = user_response
            response = "What is your email?"
            self.ask_questions.append("What's your email?")

        elif "What's your company?" != self.ask_questions[-1] and "What's your company?" not in self.ask_questions:
            if self.ask_questions[-1] == "What's your email?":
                self.user_data["email"] = user_response
            response = "What is your company?"
            self.ask_questions.append("What's your company?")
        
        else:
            if self.ask_questions[-1] == "What's your company?" and "company" not in self.user_data:
                self.user_data["company"] = user_response
                return "Thank you for answering the questions. Is there anything else I can help you with today?"
            response = self.generate_response(f"generate response for user query {user_response}.")
            
        return response