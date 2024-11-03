from flask import Flask, jsonify, request, abort
import json
import uuid


app = Flask(__name__)

with open("output.json", 'r', encoding='utf-8') as file:
  books = json.load(file)

for book in books:
  book['id'] = str(uuid.uuid4())

@app.route('/api/books', methods=["GET"])
def get_books():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_books = books[start:end]
    response = {
      'page': page,
      'per_page': per_page,
      'total': len(books),
      'total_pages': (len(books) + per_page - 1) // per_page,
      'books': paginated_books,
    }
    return jsonify(response)


@app.route("/api/books/<id>", methods=["GET"])
def get_book(id): 
  book = next((book for book in books if book['id'] == id), None)
  if book is None:
    abort(404, "Book Not Found!")
  return jsonify(book)



if __name__ == '__main__':
  app.run(debug=True)