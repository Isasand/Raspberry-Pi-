raspistill -v -o newpic.jpg
convert newpic.jpg newpic.rgba
answer=`cmp oldpic.rgba newpic.rgba 2>&1`
echo $answer
if [[ "$answer" == "cmp: oldpic.rgba: No such file or directory" ]]; then
        mv newpic.rgba oldpic.rgba
fi
if [[ "$answer" == *"differ"* ]]; then
        mv newpic.rgba oldpic.rgba
        echo "send to clooud mf"
fi









