from flask import Flask, render_template, request, jsonify
from googleapiclient.discovery import build

app = Flask(__name__, static_folder='static')

# Substitua 'SUA_CHAVE_DE_API' pela sua chave de API do YouTube Data API
API_KEY = 'AIzaSyCq9TBlGmnbczHSGMdkblbUDiF7odAcMXU'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_video_details')
def get_video_details():
    video_id = request.args.get('video_id')

    youtube = build('youtube', 'v3', developerKey=API_KEY)
    video_request = youtube.videos().list(
        part='snippet,statistics,contentDetails',  # Adicionando 'contentDetails' para obter informações sobre a duração do vídeo
        id=video_id
    )

    try:
        response = video_request.execute()

        if 'items' in response and len(response['items']) > 0:
            video_snippet = response['items'][0]['snippet']
            video_statistics = response['items'][0]['statistics']
            video_content_details = response['items'][0]['contentDetails']

            return jsonify({
                'title': video_snippet.get('title', 'N/A'),
                'channelTitle': video_snippet.get('channelTitle', 'N/A'),
                'description': video_snippet.get('description', 'N/A'),
                'publishedAt': video_snippet.get('publishedAt', 'N/A'),
                'tags': video_snippet.get('tags', []),
                'views': video_statistics.get('viewCount', 'N/A'),
                'likes': video_statistics.get('likeCount', 'N/A'),
                'dislikes': video_statistics.get('dislikeCount', 'N/A'),
                'comments': video_statistics.get('commentCount', 'N/A'),
                'videoUrl': f"https://www.youtube.com/watch?v={video_id}",
                'thumbnails': video_snippet.get('thumbnails', []),
                'duration': video_content_details.get('duration', 'N/A')
                # Adicione outras informações desejadas aqui
            })
        else:
            return jsonify({'error': 'Vídeo não encontrado ou erro na solicitação.'}), 404

    except Exception as e:
        return jsonify({'error': 'Erro na solicitação à API do YouTube: ' + str(e)}), 500



if __name__ == "__main__":
    app.run(debug=True)