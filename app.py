from agent import run_agent

print("===== Startup Research Assistant Agent =====\n")

query = input("Enter your request:\n")

result = run_agent(query)

print("\n===== RESULT =====\n")

print(result)