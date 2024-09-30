class PrintHelloWorld:

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {"multiline": False, "default": "Hello World"}),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "print_text"
    OUTPUT_NODE = False
    CATEGORY = "Tutorial Nodes"

    def print_text(self, text):
        print(f"Nice, {text}!")
        return {}
