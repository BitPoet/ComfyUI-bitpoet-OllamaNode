from .ollama_llm_node import BitPoetOllamaLLMNode

NODE_CLASS_MAPPINGS = {
    "BitPoetOllamaLLMNode": BitPoetOllamaLLMNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BitPoetOllamaLLMNode": "Ollama LLM"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']