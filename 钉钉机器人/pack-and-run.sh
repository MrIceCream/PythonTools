rm -rf build && \
rm -rf dist && \
rm -rf yzk-dingtalk-bot yzk-dingtalk-bot.spec && \
sleep 2 && \
pyinstaller --onefile yzk-dingtalk-bot.py && \
mv dist/yzk-dingtalk-bot ./ && 
bash -c "nohup ./yzk-dingtalk-bot >/dev/null 2>&1 &" && \
echo "nohup success"
exit