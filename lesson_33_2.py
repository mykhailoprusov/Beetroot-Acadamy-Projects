import requests
import multiprocessing
import json

REQUESTS = ["football","OPBR","meirl","CoffeeGoneWild"]

def handle_request(username):
    try:
        r = requests.get('https://api.pushshift.io/reddit/comment/search/',params={"subreddit":username},timeout=60)
        print(r.text)

    except requests.ReadTimeout:
        pass


    if r.status_code == requests.codes.not_found:
        print('Not Found')

    info = r.json()
    comment_info = info['data']

    lock = multiprocessing.Lock()

    lock.acquire()
    with open("comments111.json") as file:

        data = file.read()
        old_data = json.loads(data)
        old_data.append(comment_info)

    with open("comments111.json","w") as file2:

        formatted = json.dumps(old_data)
        file2.write(formatted)
    lock.release()

if __name__ == '__main__':

    processes = []
    for i in REQUESTS:

        process = multiprocessing.Process(target=handle_request, args=(i,))
        process.start()
        processes.append(process)

    for i in processes:
        i.join()