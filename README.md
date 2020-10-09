# Download Youtube Video 

This repository is created to download youtube video by uploading a text file containing tags. This project is created in djnago and some of the open source repositories has been used which i will state below. Also, i will provide instructions to run the project which use docker. So make sure you have docker installed in your system.

Also, i will suggest you to use vitual environment to run this project on your system.

## Running Locally

```bash
git clone https://github.com/rijvanmohd/download-youtube-videos.git
```

```bash
docker build -t assign-docker -f Dockerfile .
```

```bash
docker run -it -p 5000:5000 assign-docker
```

Head over to 0.0.0.0:5000.

## Sample Text File Contents
Accident
Fight
New Song

Must be seperated by new line

# Open Source Repositories Used

https://github.com/HermanFassett/youtube-scrape

https://pypi.org/project/pytube/
