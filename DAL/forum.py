import json
from models.forum import Thread, Comment
from models.projects import Project
from models.users import User


# GET
def get_projects_threads_comments(project_id):
    threads = Thread.objects(projectId=project_id)

    result = []
    for thread in threads:
        thread_comments = []
        for comment in thread.comments:
            thread_comments.append(comment.to_json())
        thread.comments = thread_comments.copy()
        result.append(thread.to_json())

    return json.dumps(result)


# POST
def add_new_thread(thread_data):
    thread = Thread(
        projectId=Project.objects(id=thread_data['project_id']).first(),
        userId=User.objects(id=thread_data['user_id']).first(),
        topic=thread_data['topic'],
        body=thread_data['body'],
        comments=[]
    )
    thread.save()
    return thread.reload().to_json()


def add_new_comment(comment_data):
    thread_comments = Thread.objects(id=comment_data['thread_id']).first()['comments']

    comment = Comment(
        userId=User.objects(id=comment_data['user_id']).first(),
        text=comment_data['text'],
    )
    thread_comments.append(comment)
    thread_comments.save()

    return comment.to_json()
