import json

with open('carlo.json', 'r') as f:
	ghost_json = json.load(f)

all_posts = ghost_json['db'][0]['data']['posts']

for post in all_posts:
	post_md = (post['markdown'])
	title = post['title']
	date = post['published_at'][:10]
	
	file_name = "".join([date, "_", title])
	file_name = file_name.replace(" ", "-")
	file_name = file_name.replace(",", "")
	file_name = file_name.replace("+", "")
	file_name = file_name.replace("--", "-")
	file_name = file_name.replace(":", "")
	file_name = file_name.replace("/", "-")
	file_name = file_name.replace("...", "-")
	file_name = file_name.replace("--", "-")
	file_name = file_name.replace("!", "")
	file_name = file_name.replace(".", "")
	file_name = file_name + ".md"
	
	with open(("posts/" + file_name), mode="w", encoding="utf-8") as md:
		md.write(post_md)
	
