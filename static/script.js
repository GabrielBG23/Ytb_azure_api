function getVideoDetails() {
    const videoId = document.getElementById('videoId').value;

    fetch(`/get_video_details?video_id=${videoId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('title').innerHTML = `<strong>Título:</strong> ${data.title}`;
            document.getElementById('channel').innerHTML = `<strong>Canal:</strong> ${data.channelTitle}`;
            document.getElementById('description').innerHTML = `<strong>Descrição:</strong> ${data.description}`;
            document.getElementById('publishedAt').innerHTML = `<strong>Data de Publicação:</strong> ${data.publishedAt}`;
            document.getElementById('tags').innerHTML = `<strong>Tags:</strong> ${data.tags.join(', ')}`;
            document.getElementById('views').innerHTML = `<strong>Visualizações:</strong> ${data.views}`;
            document.getElementById('likes').innerHTML = `<strong>Likes:</strong> ${data.likes}`;
            document.getElementById('dislikes').innerHTML = `<strong>Dislikes:</strong> ${data.dislikes}`;
            document.getElementById('comments').innerHTML = `<strong>Comentários:</strong> ${data.comments}`;
            document.getElementById('videoUrl').innerHTML = `<strong>URL do Vídeo:</strong> ${data.videoUrl}`;
            document.getElementById('duration').innerHTML = `<strong>Duração:</strong> ${data.duration}`;

            const videoPlayer = document.getElementById('videoPlayer');
            const videoLink = `https://www.youtube.com/embed/${videoId}`;
            videoPlayer.innerHTML = `
                <iframe width="1280" height="500" src="${videoLink}"
                title="YouTube video player" frameborder="0" allow="accelerometer; autoplay;
                clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            `;

            document.querySelector('.container').classList.add('show');
        })
        .catch(error => console.error('Erro:', error));
}
