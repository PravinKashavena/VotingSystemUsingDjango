# views.py
from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

def home(request):
    return render(request, 'home.html')

def count_party_members(request):
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='12345',
            database='pythondb1'
        )

        cursor = conn.cursor()

        # Assuming you have a table named 'voters' with a column 'party' storing the party names
        cursor.execute("SELECT party, COUNT(*) FROM voters GROUP BY party")
        party_counts = cursor.fetchall()
        print(party_counts)

        conn.close()

        return render(request, 'party_count.html', {'party_counts': party_counts})

    except mysql.connector.Error as error:
        return HttpResponse(f"Error: {error}")

def add_voter(request):
    if request.method == 'POST':
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='12345',
                database='pythondb1'
            )

            cursor = conn.cursor()

            voter_name = request.POST.get('voter_name')
            voter_id = request.POST.get('voter_id')
            party_name = request.POST.get('party_name')

            # Assuming you have a table named 'voters' with columns 'name', 'voter_id', and 'party'
            cursor.execute("INSERT INTO voters (name, voter_id, party) VALUES (%s, %s, %s)", (voter_name, voter_id, party_name))
            conn.commit()

            conn.close()

            return render(request, 'success.html')

        except mysql.connector.Error as error:
            return HttpResponse(f"Error: {error}")

    return render(request, 'vote_form.html')
