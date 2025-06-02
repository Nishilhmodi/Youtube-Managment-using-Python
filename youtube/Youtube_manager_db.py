import sqlite3

conn = sqlite3.connect('Youtube_videos.db')
cursor = conn.cursor()

cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("The Database is Empty.")
        return
    else:
        for row in rows:
            print(f"[ID: {row[0]}, Name: {row[1]}, Time: {row[2]}]")

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print(f"Video '{name}' added successfully.")

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()
    print(f"Video ID {video_id} updated successfully.")

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    print(f"Video ID {video_id} deleted successfully.")

def main():
    while True:
        print("\nYoutube manager app with DB")
        print("1. List video")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = int(input("Enter video ID to update: "))
            name = input("Enter new video name: ")
            time = input("Enter new video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = int(input("Enter video ID to delete: "))
            delete_video(video_id)
        elif choice == '5':
            print("Exiting the app.")
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()