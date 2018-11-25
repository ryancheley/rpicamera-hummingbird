# change to the directory with all of the files
cd /home/pi/Documents/python_projects/

# make the script that was just created executable
echo "Make the script executable" >> log.txt
chmod +x /home/pi/Documents/python_projects/create_mp4.sh

# run the script to create the mp4 file
/home/pi/Documents/python_projects/create_mp4.sh
echo "Run create_MP4 Shell Script: $(date)" >> log.txt

# upload video to YouTube.com
/home/pi/Documents/python_projects/upload.sh
echo "Uploaded Video to YouTube.com: $(date)" >> log.txt

# calculate video duration and save it
/home/pi/Documents/python_projects/mp4_duration.sh
echo "Duration saved" >> log.txt


