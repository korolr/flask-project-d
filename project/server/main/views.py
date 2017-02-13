# project/server/main/views.py


#################
#### imports ####
#################

from flask import render_template, Blueprint
from project.server.models import Post



################
#### config ####
################

main_blueprint = Blueprint('main', __name__,)


################
#### routes ####
################


@main_blueprint.route('/')
@main_blueprint.route('/index', methods = ['GET', 'POST'])
@main_blueprint.route('/index/<int:page>', methods = ['GET', 'POST'])
def home(page = 1):
    post = Post.query.paginate(page, 8, False)
    return render_template('main/home.html', posts=post)

@main_blueprint.route('/cat/', methods = ['GET', 'POST'])
def cat():
    post = Post.query.filter_by(category=2)
    print(post)
    return render_template('main/home.html', posts=post)

@main_blueprint.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return render_template('main/post.html', post=Post.query.get(post_id))


@main_blueprint.route("/about/")
def about():
    return render_template("main/about.html")
