from flask import Flask, request, render_template, redirect, flash, jsonify
from random import randint, choice, sample
from flask_debugtoolbar import DebugToolbarExtension
from Flask_Mail import Mail, Message


app = Flask(__name__)
mail = Mail(app)
app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)



@app.route('/')
def landing():
    html = """
    <html>
    <body>
        <h1>Hello!</h1>
            <p>This is the hello page</p>
            <a href='/hello'>Go to hello page</a>
    </body>
    """
    return html

@app.route("/email")
def send_email():
    msg = Message("Hello, World!",
                    sender="ethandeg1996@gmail.com",
                    recipients=["ethandeg1996@gmail.com"])
    msg.body = "Testing"
    msg.html = "<b>testing<b>"
    mail.send(msg)
    
    html = """
    <html>
    <body>
        <h1>Hello!</h1>
            <p>This is the hello page (check email?)</p>
            <a href='/hello'>Go to hello page</a>
    </body>
    """

    return html

# @app.route('/old-home-page')
# def redirect_to_home():
#     """redirects to new home page"""
#     return redirect('/')


# @app.route('/movies')
# def show_all_movies():
#     """Show list of all movies in fake db"""
#     return render_template('movies.html', movies=MOVIES)


# @app.route('/movies/new', methods=['POST'])
# def add_movie():
#     title = request.form['title']
#     # add to pretend db
#     if title in MOVIES:
#         flash("movie already exists!", 'error')
#     else:
#         MOVIES.add(title)
#         flash('Created Your Movie', 'success')
#     return redirect('/movies')


# @app.route('/movies/json')
# def get_movies_json():
#     json_obj = jsonify(list(MOVIES))
#     raise
#     return json_obj


# @app.route('/hello')
# def say_hello():
#     return render_template('hello.html')


# @app.route('/goodbye')
# def say_bye():
#     return "Goodbye!!"


# @app.route('/search')
# def search():
#     term = request.args["term"]
#     sort = request.args["sort"]
#     return f"<h1>Search Results For: {term}</h1><p> Sorting by: {sort}</p>"

# # @app.route('/post', methods=["POST"])
# # def post_demo():
# #     return "you made a post request"


# @app.route('/add-comment')
# def add_comment_form():
#     return """
#         <h1>Add Comment</h1>
#         <form method="POST">
#             <input type='text' placeholder='comment' name='comment'/>
#             <input type='text' placeholder='username' name='username'/>
#             <button>Submit</button>
#         </form>
#     """


# @app.route('/add-comment', methods=["POST"])
# def save_comment():
#     comment = request.form["comment"]
#     username = request.form["username"]
#     return f"""
#     <h1>Saved your comment</h1>
#     <ul>
#         <li>Username: {username}
#         <li>Comment: {comment}
#     </ul>
#     """


# @app.route('/r/<subreddit>')
# def show_subreddit(subreddit):
#     return f"<h1>Browsing {subreddit} Subreddit"


# @app.route("/r/<subreddit>/comments/<int:post_id>")
# def show_comments(subreddit, post_id):
#     return f"<h1>Viewing comments for post with id: {post_id} from the {subreddit} Subreddit"


# POSTS = {
#     1: "I like chicken tenders",
#     2: "I hate mayo!",
#     3: "Double rainbow all the way",
#     4: "Yolo OMG (kill me)"
# }


# @app.route('/posts/<int:id>')
# def find_post(id):
#     post = POSTS.get(id, "Post not found")
#     return f"<p>{post}</p>"


# @app.route('/lucky')
# def lucky_number():
#     num = randint(1, 10)
#     return render_template('lucky.html', lucky_num=num, msg='you are so lucky')


# COMPLIMENTS = ['cool', 'clever', 'tenacious', 'awesome', 'pythonic']


# @app.route('/form')
# def show_form():
#     return render_template('form.html')


# @app.route('/form2')
# def show_form_2():
#     return render_template('form_2.html')


# @app.route('/greet')
# def get_greeting():
#     username = request.args['username']
#     nice_thing = choice(COMPLIMENTS)
#     return render_template('greet.html', username=username, compliment=nice_thing)


# @app.route('/greet2')
# def get_greeting_2():
#     username = request.args['username']
#     wants_compliments = request.args.get('wants_compliments')
#     nice_things = sample(COMPLIMENTS, 3)
#     return render_template('greet_2.html', username=username, wants_compliments=wants_compliments, compliments=nice_things)


# @app.route('/spell/<word>')
# def spell_word(word):
#     return render_template('spell_word.html', word=word)
