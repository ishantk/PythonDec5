# Regular Expressions
import re

quote = "Search the candle rather than cursing the darkness"
result = re.match("Search", quote)
print(result)
print(result.start())
print(result.end())

print()

result = re.search("the", quote)
print(result)

print()

result = re.findall("the", quote)
print(result)

result = re.split("the", quote)
print(result)

result = re.sub("the", "a", quote)
print(result)

print()
print(">>>>>>>>><<<<<<<")
print()

newQuote = "Work Hard and Get Luckier"
result = re.findall(".", newQuote)
print(result)

result = re.findall("\w", newQuote)
print(result)

result = re.findall("\w*", newQuote)
print(result)

result = re.findall("\w+", newQuote)
print(result)
