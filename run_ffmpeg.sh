echo "Convert jpgs to mp4 started at $(date)" >> log.txt
ffmpeg -framerate 10 -pattern_type glob -i '*.jpg' -c:v libx264 -pix_fmt yuv420p out.mp4
echo "mp4 succesfully created completed at $(date)" >> log.txt
