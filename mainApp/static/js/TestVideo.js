navigator.getUserMedia(
        // Настройки
        {
            video: true
        },
        // Колбэк для успешной операции
        function(stream){
            // Создаём объект для видео потока и
            // запускаем его в HTLM элементе video.
            video.src = window.URL.createObjectURL(stream);
            // Воспроизводим видео.
            video.play();
        },
        // Колбэк для не успешной операции
        function(err){
            // Наиболее частые ошибки — PermissionDenied и DevicesNotFound.
            console.error(err);
        }
    );
    