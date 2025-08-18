

import streamlit as st
import pandas as pd
import altair as alt

# Button to clear cache manually
if st.sidebar.button("🔄 Reload Data"):
    st.cache_data.clear()

@st.cache_data
def load_data():
    articles = pd.read_csv("bbc_full_combined.csv")
    subcats = pd.read_csv("bbc_combined_subcategories.csv")
    ner = pd.read_csv("NER_media_personalities.csv")
    april = pd.read_csv("April_events_summary.csv")
    return articles, subcats, ner, april

# Load data
articles, subcats, ner, april = load_data()

# --- Use dataframes separately, no merging ---
# Clean up filename columns for consistency
articles['filename'] = articles['filename'].astype(str).str.strip()
subcats['filename'] = subcats['filename'].astype(str).str.strip()
april['filename'] = april['filename'].astype(str).str.strip()

# --- Sidebar: Filters, Downloads, Feedback ---
st.sidebar.header("Filters")
selected_category = st.sidebar.selectbox("Category", articles['category'].dropna().unique().tolist())
search_term = st.sidebar.text_input("Search by filename")

filtered_articles = articles.copy()
if selected_category:
    filtered_articles = filtered_articles[filtered_articles['category'] == selected_category]
if search_term:
    term = search_term.lower()
    filtered_articles = filtered_articles[
        filtered_articles['text'].astype(str).str.lower().str.contains(term, na=False)
        | filtered_articles['filename'].astype(str).str.lower().str.contains(term, na=False)
        | filtered_articles['category'].astype(str).str.lower().str.contains(term, na=False)
    ]

st.sidebar.header("Download Results")
st.sidebar.download_button("Download Filtered Articles CSV", filtered_articles.to_csv(index=False), "filtered_articles.csv")
st.sidebar.download_button("Download NER Results CSV", ner.to_csv(index=False), "ner_results.csv")
st.sidebar.download_button("Download April Events CSV", april.to_csv(index=False), "april_events.csv")
st.sidebar.download_button("Download Subcategories CSV", subcats.to_csv(index=False), "subcategories.csv")
st.sidebar.download_button("Download Full Articles CSV", articles.to_csv(index=False), "full_articles.csv")


# --- Main Page Content (No Tabs) ---

st.title("BBC NEWS ARTICLE EXPLORER")
st.markdown("""


- Browse and filter BBC news articles by category and subcategory
- Explore named entity recognition (NER) results for media personalities
- Use the sidebar to filter articles and download results
- Search articles by filename or text content
- Download filtered results and full datasets
- View summaries of April events
""")

st.subheader("Category Overview")
cat_counts = articles['category'].value_counts().reset_index()
cat_counts.columns = ['Category', 'Count']
st.altair_chart(
    alt.Chart(cat_counts).mark_bar().encode(
        x='Count:Q',
        y=alt.Y('Category:N', sort='-x'),
        color=alt.value("#FFB07C")  # Peach color
    ),
    use_container_width=True
)

st.subheader("Filtered Articles")
st.dataframe(filtered_articles, use_container_width=True)

st.subheader("Subcategory Explorer")
subcat_list = ['All'] + subcats['subcategory'].dropna().unique().tolist()
selected_subcat_explorer = st.selectbox("Filter by Subcategory", subcat_list)
if selected_subcat_explorer == 'All':
    subcats_filtered = subcats
else:
    subcats_filtered = subcats[subcats['subcategory'] == selected_subcat_explorer]
st.dataframe(subcats_filtered, use_container_width=True)


# Add a bar chart for category counts in the filtered subcategories
if not subcats_filtered.empty:
    subcat_counts = subcats_filtered['category'].value_counts().reset_index()
    subcat_counts.columns = ['Category', 'Count']
    st.altair_chart(
        alt.Chart(subcat_counts).mark_bar().encode(
            x='Count:Q',
            y=alt.Y('Category:N', sort='-x'),
            color=alt.value("#08AB46")  # Peach color for consistency
        ),
        use_container_width=True
    )

# NER Explorer
st.subheader("NER Explorer")
selected_role = st.selectbox("Filter by Media Role", ['All'] + ner['media_personality'].dropna().unique().tolist())
if selected_role == 'All':
    ner_filtered = ner
else:
    ner_filtered = ner[ner['media_personality'] == selected_role]
st.dataframe(ner_filtered, use_container_width=True)

# Add a bar chart for media_personality counts
if not ner_filtered.empty:
    mp_counts = ner_filtered['media_personality'].value_counts().reset_index()
    mp_counts.columns = ['Media Personality', 'Count']
    st.altair_chart(
        alt.Chart(mp_counts).mark_bar().encode(
            x='Count:Q',
            y=alt.Y('Media Personality:N', sort='-x'),
            color=alt.value("#71DCEE")  # Peach color
        ),
        use_container_width=True
    )

# April Events Explorer
st.subheader("April Events Explorer")
april_cat_list = ['All'] + april['category'].dropna().unique().tolist()
selected_april_cat = st.selectbox("Filter by April Event Category", april_cat_list, key="april_event_cat")
if selected_april_cat == 'All':
    april_filtered = april
else:
    april_filtered = april[april['category'] == selected_april_cat]
st.dataframe(april_filtered, use_container_width=True)


# Add a bar chart for April events in the filtered categories
if not april_filtered.empty:
    april_counts = april_filtered['category'].value_counts().reset_index()
    april_counts.columns = ['Category', 'Count']
    st.altair_chart(
        alt.Chart(april_counts).mark_bar().encode(
            x='Count:Q',
            y=alt.Y('Category:N', sort='-x'),
            color=alt.value("#e15759")
        ),
        use_container_width=True
    )


# Footer
st.caption("Built with Streamlit by Udodirim Nwosu")
st.markdown("This app is part of the BBC NLP project.")
