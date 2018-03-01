#!/bin/sh

#  Script.sh
#  
#
#  Created by Alexander  Tarancon  on 3/1/18.
#

echo Train!

opencv_traincascade -data outputDirectory -vec cropped.vec -bg bg.txt -numPos 1000 -numNeg 600 -numStages 10 -precalcValBufSize 2048   - precalcIdxBufSize 2048 -featureType HAAR  -w 20 -h 20


