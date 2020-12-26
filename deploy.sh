#!/bin/bash

source ~/venv/staticfolio/bin/activate 
python main.py << end-of-script
Y
end-of-script
deactivate
echo "*** END OF SCRIPT***"
cp -rv output/* ../carlocarfora.github.io/
echo "*** END OF COPY ***"
cd ../carlocarfora.github.io
