FROM python:alpine
COPY Utils_file_utils.py .
COPY Score_utils_file_score.py .
COPY MemoryGame_memory_game.py .
COPY GuessGameguessgame2.py .
COPY CurrencyRouletteGamecurrencyroulettegame.py .
COPY app.py .
COPY e2e.py .
COPY main.py .
COPY Main_scores_file.py .
COPY Scores.txt .
RUN pip install flask
CMD python Main_scores_file.py
