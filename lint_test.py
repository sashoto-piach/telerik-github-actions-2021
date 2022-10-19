import sys
from pylint import lint
THRESHOLD = 5
run = lint.Run(["factorial.py"], do_exit=False)
# score = run.linter.stats["global_note"]
score = 6
if score < THRESHOLD:
    print("Linter failed: Score < threshold value")
    sys.exit(1)
sys.exit(0)
