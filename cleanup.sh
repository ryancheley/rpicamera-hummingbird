# cd into directory
cd /home/pi/Documents/python_projects/

# Count the number of h264 files to be removed

echo "$(ls *.jpg | wc -l) jpg files will be removed" >> log.txt

# Next we remove the video files locally
echo "removing jpg files" >> log.txt
rm *.jpg
echo "removed jpg files: $(date)" >> log.txt

rm *.mp4
echo "removed mp4 file: $(date)" >> log.txt
