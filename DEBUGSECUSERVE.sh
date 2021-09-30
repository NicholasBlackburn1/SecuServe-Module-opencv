
echo "Starting SecuServe Security System UwU💗 in debug"

sudo OPENBLAS_CORETYPE=ARMV8 python3  -m cProfile -o debug.out $(readlink -f videoprocessingsrc/__main__.py)
 