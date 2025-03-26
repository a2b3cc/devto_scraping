# source/scraping/core/utils.py

import re


def extract_article_metadata(article):
    """"
    Extracts metadata from a DEV.to article element.

    Args:
        article: a playwright element handle for the article.

    Returns:
        dictionary: date, title, href, tags, read_time, reactions_count, comments_count
    """
    # Title and URL
    title_link = article.query_selector("h3.crayons-story__title a")
    title = title_link.inner_text().strip() if title_link else None
    href = title_link.get_attribute("href") if title_link else None
    if href and href.startswith("/"):
        href = "https://dev.to" + href

    # Publication date
    time_el = article.query_selector("a.crayons-story__tertiary time")
    date = time_el.inner_text().strip() if time_el else None

    # Tags
    tag_el = article.query_selector_all("div.crayons-story__tags a")
    tags = [tag.inner_text().strip()[2:] for tag in tag_el] if tag_el else []

    # Time to read (-1 if not found)
    read_time_el = article.query_selector("div.crayons-story__save small.crayons-story__tertiary")
    read_time = int(read_time_el.inner_text().strip().split()[0]) if read_time_el else -1

    # Reactions count
    reactions_el = article.query_selector(
        "div.multiple_reactions_aggregate span.aggregate_reactions_counter")
    reaction_count = int(reactions_el.inner_text().strip().split()[0]) if reactions_el else 0

    # Comment count
    comments_el = article.query_selector("a[href*='#comments']")
    comments_text = comments_el.inner_text().strip() if comments_el else "0"
    match = re.search(r'\d+', comments_text)
    comments_count = int(match.group()) if match else 0

    return {
        "date": date,
        "title": title,
        "href": href,
        "tags": tags,
        "read_time": read_time,
        "reaction_count": reaction_count,
        "comments_count": comments_count,
    }


def scrape_comments(article_url, context):
    """
    Opens the article URL using the provided browser context.
    Returns:
        list: a list of the comments for the article.
    """
    comments = []
    article_page = context.new_page()
    article_page.goto(article_url, timeout=60000)
    article_page.wait_for_load_state("networkidle")
    article_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    try:
        article_page.wait_for_selector("#comments-container", timeout=5000)
    except:
        pass
    # Use a simple selector to grab <p> tags inside the comments container.
    comment_elements = article_page.query_selector_all("#comments-container .comments p")
    comments = [c.inner_text().strip() for c in comment_elements]
    article_page.close()
    return comments
