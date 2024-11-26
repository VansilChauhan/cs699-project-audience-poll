from io import BytesIO
import base64
import matplotlib.pyplot as plt
import pandas as pd
from app import poll_service as ps

def create_poll_vote_dist_plot(options):
    data = []
    for option in options:
        row = {'Option':option.text, 'Votes':ps.get_vote_counts_for_poll(option_id=option.id)}
        data.append(row)
    df = pd.DataFrame(data)
    plt.bar(df['Option'], df['Votes'], label=df['Option'], width=0.5)
    plt.xlabel("Options")
    plt.ylabel("Votes")
    plt.title("Option Vote Distribution")
    buff = BytesIO()
    plt.savefig(buff, format="png")
    plt.close()
    plot_img = base64.b64encode(buff.getvalue()).decode()
    return plot_img

def create_votes_gender_distribution(option):
    data = []
    for gender in ps.get_all_unique_genders():
        votes = ps.vote_count_by_user_gender(option=option, gender=gender)
        row = {'Gender':gender, 'Votes':votes}
        data.append(row)
    df = pd.DataFrame(data)
    plt.bar(df['Gender'], df['Votes'], label=df['Gender'], width=0.5)
    plt.title(f"{option.text} votes")
    buff = BytesIO()
    plt.savefig(buff, format="png")
    plt.close()
    plot_img = base64.b64encode(buff.getvalue()).decode()
    return plot_img