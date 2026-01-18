from flask import Flask, request, jsonify
from graph_builder import run_rag_pipeline

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Multi-Agent RAG Flask API Running"}

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")

    if not question:
        return jsonify({"error": "Missing question"}), 400

    try:
        answer = run_rag_pipeline(question)
        return jsonify({"question": question, "answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
