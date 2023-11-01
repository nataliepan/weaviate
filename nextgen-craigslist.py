import io
import os
import streamlit as st
import weaviate
from PIL import Image
import base64

# Connect to Weaviate
weaviate_client = weaviate.Client(url="http://localhost:8080")

def set_bg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"webp"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

# Helper function to convert a file to base64 representation
def toBase64(path):
    with open(path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')
    
def text_to_media(query):
    # Search for media with the given query
    response = weaviate_client.query.get("Craigslist", "name path desc url mediaType").with_near_text({"concepts": query}).with_limit(10).with_additional('distance').do()
    result = response["data"]["Get"]["Craigslist"]
    final_results = []

    for r in result:
        print(f"{r['_additional']['distance']},{r['desc']}")
        if r['_additional']['distance'] <= 0.75:
            final_results.append(r)

    return final_results

def image_search(image_path):
    # Search for images that are similar to the provided image of test-meerkat, test-dog, test-cat
    response = weaviate_client.query.get("Craigslist", "name path desc url mediaType").with_near_image({"image": image_path}).with_limit(10).with_additional('distance').do()
    result = response["data"]["Get"]["Craigslist"]
    final_results = []

    for r in result:
        print(f"{r['_additional']['distance']}")
        if r['_additional']['distance'] <= 0.75:
            final_results.append(r)

    return final_results

def main():
    st.title("Nextgen Craigslist Powered by GAI")

    # Set background image
    set_bg('bg.webp')

    # Image Upload
    st.subheader("Upload an Image:")
    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    query = st.text_input("Or enter a text query:")

    if st.button("Search"):
        if uploaded_image:
            path = os.path.join('.', uploaded_image.name)
            # image = toBase64(path)
            # image = Image.open(uploaded_image)
            # image_bytes = io.BytesIO()
            # image.save(image_bytes, format="JPEG")
            # image_data = image_bytes.getvalue()

            # Perform image-based search
            # You need to implement this part using your specific Weaviate capabilities
            # Here, I assume that you have a separate function for image-based search
            # Replace the 'image_search' function with your own implementation
            # print(type(image), image)
            results = image_search(path)
        elif query:
            results = text_to_media(query)
        else:
            st.markdown("Please upload an image or enter a text query.")

        if results:
            st.markdown(f"Found {len(results)} results:")
            for result in results:
                st.image(result["path"])
                st.write(result["name"])
                st.write(result["desc"])
        else:
            st.markdown("No results found.")

if __name__ == "__main__":
    main()
