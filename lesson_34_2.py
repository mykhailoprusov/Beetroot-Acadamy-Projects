import requests
import asyncio
import json

REQUESTS = ["football","OPBR","meirl","CoffeeGoneWild"]

async def handle_request(username):
    try:
        r = requests.get('https://api.pushshift.io/reddit/comment/search/',params={"subreddit":username},timeout=60)
        print(r.text)

    except requests.ReadTimeout:
        pass


    if r.status_code == requests.codes.not_found:
        print('Not Found')

    info = r.json()
    comment_info = info['data']


    with open("comments_new.json") as file:

        data = file.read()
        old_data = json.loads(data)
        old_data.append(comment_info)

    with open("comments_new.json","w") as file2:

        formatted = json.dumps(old_data)
        file2.write(formatted)


async def main():
    task1= asyncio.create_task(handle_request(username=REQUESTS[0]))
    task2= asyncio.create_task(handle_request(username=REQUESTS[1]))
    task3= asyncio.create_task(handle_request(username=REQUESTS[2]))
    task4= asyncio.create_task(handle_request(username=REQUESTS[3]))

    await asyncio.gather(task1,task2,task3,task4)

asyncio.run(main())


