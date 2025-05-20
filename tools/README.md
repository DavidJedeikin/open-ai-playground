# Using tools

- When a model uses a function defined locally, it returns the arguments required to call the function.
- The flow is as follows - the model is called twice:
  - Initial request
  - Response with function call arguments
  - Call function with arguments
  - Return the result to the model
    - Response 1 & the result must be appended to the input messages
    - It's essential that the model know:
      - That it asked for a function call
      - The associated response
  - Print final response
