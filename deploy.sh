#!/bin/bash

source venv/bin/activate
python main.py << end-of-script
Y
end-of-script
deactivate
\cp -rv output/* ../carlocarfora.github.io/
cd ..
cd carlocarfora.github.io
