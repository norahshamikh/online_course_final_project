# Как загрузить проект на GitHub

1. Распакуйте архив и откройте папку проекта в терминале.
2. Создайте на GitHub публичный репозиторий `emotion-detector` без автоматического README.
3. Выполните команды:

```powershell
git init
git add .
git commit -m "Complete Emotion Detector final project"
git branch -M main
git remote add origin https://github.com/Eugene8Lost/emotion-detector.git
git push -u origin main
```