# cd into directory
cd /home/pi/Documents/python_projects/

# Count the number of h264 files to be removed

echo "removed $(ls *.h264 | wc -l) h264 files" >> log.txt

# Next we remove the video files locally
echo "removing h264 files" >> log.txt
rm *.h264
echo "removed h264 files: $(date)" >> log.txt

rm create_mp4.sh
echo "removed create_mp4.sh" >> log.txt

rm *.mp4
echo "removed mp4 file: $(date)" >> log.txt
