a = 'div*2'
tag, count = a.split('*') 
count = int(count)
result = f"<{tag}></{tag}>" * count
print(result)