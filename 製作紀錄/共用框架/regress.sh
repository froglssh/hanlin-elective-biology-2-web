#!/bin/bash
S=/tmp/claude-0/-home-user-hanlin-elective-biology-2-web/1dfeb973-4bf6-5145-8c8d-a58fc539f383/scratchpad
(cd $S/w && python3 build.py >/dev/null) ; (cd $S/w2 && python3 build.py >/dev/null)
for u in "$@"; do (cd $S/units/$u && python3 unit.py >/dev/null 2>&1; python3 unit.py build 2>&1 | grep -E "錯誤|Error") ; done
cd /home/user/hanlin-elective-biology-2-web
for H in CH*/教學網頁/*_優化版.html; do echo "== ${H%%/*}"; node $S/fw/t_layout.cjs "$PWD/$H" | grep -v -E '^(390|360)x[0-9]+ Q.*"x":false'; node $S/fw/t_func.cjs "$PWD/$H"; done
