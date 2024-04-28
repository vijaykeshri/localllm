from ollamaclient import chatResponse

def performOnFileContents(action,filename):

    prompt = "Find the "+action+" of the provided text: "
    textFromFile = _readFile(filename)
    response = chatResponse('user',prompt + textFromFile)
    if 'message' in response and 'content' in response['message']:
        return response['message']['content'].strip()
    else:
        return 'Failed to perform requested operation'

def _readFile(filename):
    fileConents = ""
    try:
        with open(filename, 'r', encoding="utf8") as file:
            fileConents = file.read()
    except FileNotFoundError:
        print(f"File '{filename}' is not availble at provided path.")
    return fileConents

def main():
    output = performOnFileContents('story.txt')
    print(output)

if __name__ == "__main__":
    main()

# streamlit --- file upload, select action to perform on file