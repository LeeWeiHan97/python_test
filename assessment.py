import requests
import json

# Question 1
def get_ordered_posts():
    # contains the post id as key and number of comments as value
    postid_comment_no_dict = {}

    # get list of comments from api
    comment_list = requests.get("https://jsonplaceholder.typicode.com/comments").json()
    for comment in comment_list:
        post_id = comment["postId"]
        
        if post_id not in postid_comment_no_dict:
            postid_comment_no_dict.update({post_id:1})

        else:
            postid_comment_no_dict[post_id] += 1

    # sort the dictionary and return post ids based on number of comments
    sorted_dict = sorted(postid_comment_no_dict.items(), key=lambda x: x[1], reverse=True)

    post_list = requests.get("https://jsonplaceholder.typicode.com/posts").json()

    response = []

    for post_id, comment_no in sorted_dict:
        for post in post_list:
            if post_id == post["id"]:
                response.append({
                    "post_id": post_id,
                    "post_title": post["title"],
                    "post_body": post["body"],
                    "total_number_of_comments": comment_no
                })

    # returns response
    return json.dumps(response)


# Question 2
# Made filter function for id, name, and body
def filter_comments(id, search):
    comment_list = requests.get("https://jsonplaceholder.typicode.com/comments").json()
    filtered_list = []

    # Check if user searched for post id
    if id and isinstance(id, int):
        for comment in comment_list:
            if id == comment["postId"]:
                filtered_list.append(comment)

        # return list earlier since searched id did not yield any matching results
        if len(filtered_list) == 0:
            return filtered_list

    else:
        filtered_list = comment_list

    # Check if user search text are contained in name or body
    for comment in filtered_list.copy():
        if search not in comment["name"] and search not in comment["body"]:
            filtered_list.remove(comment)

    return filtered_list


# executing code
get_ordered_posts()
filter_comments(1, "est")
