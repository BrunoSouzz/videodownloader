from flask import Flask, render_template, request, send_file
from pytubefix import YouTube
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download():
    video_url = request.args.get('url')
    if not video_url:
        return "No URL provided", 400
    
    try:
        yt = YouTube(video_url)
        
        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
        
        output_path = "/tmp" if os.name != 'nt' else "downloads"
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            
        caminho_final = stream.download(output_path=output_path)
        
        return send_file(caminho_final, as_attachment=True, download_name=f"{yt.title}.mp4")
    
    except Exception as e:
        print(f"Erro no processamento: {e}")
        return f"Erro ao processar o vídeo: {str(e)}", 500
    
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)