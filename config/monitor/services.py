# 🔥 Scan Content (WITH FIXED SUPPRESSION)
from .models import Keyword, ContentItem, Flag

def run_scan():
    keywords = Keyword.objects.all()
    contents = ContentItem.objects.all()

    created_flags = []

    for keyword in keywords:
        for content in contents:

            title = content.title.lower()
            body = content.body.lower()
            key = keyword.name.lower()

            score = 0

            # Matching logic
            if key == title:
                score = 100
            elif key in title:
                score = 70
            elif key in body:
                score = 40

            if score > 0:
                existing_flag = Flag.objects.filter(
                    keyword=keyword,
                    content_item=content
                ).first()

                # 🔥 SUPPRESSION LOGIC
                if existing_flag:
                    if existing_flag.status == 'irrelevant':
                        if existing_flag.reviewed_at and content.last_updated <= existing_flag.reviewed_at:
                            continue  # ⛔ Completely skip

                # ✅ Only create NEW flag
                if not existing_flag:
                    flag = Flag.objects.create(
                        keyword=keyword,
                        content_item=content,
                        score=score
                    )
                    created_flags.append(flag)

    