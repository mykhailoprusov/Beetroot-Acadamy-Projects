import requests
import json
import threading

def handle_request():
    try:
        r = requests.get('https://api.pushshift.io/reddit/comment/search/',timeout=60)
        print(r.text)

    except TimeoutError:
        pass


    if r.status_code == requests.codes.not_found:
        print('Not Found')

    info = r.json()
    comment_info = info['data']

    with open("comments.json") as file:

        data = file.read()
        old_data = json.loads(data)
        old_data.append(comment_info)

    with open("comments0.json","w") as file2:

        formatted = json.dumps(old_data)
        file2.write(formatted)


if __name__ == '__main__':

    thread1 = threading.Thread(target=handle_request)
    thread1.start()
    thread1.join()
