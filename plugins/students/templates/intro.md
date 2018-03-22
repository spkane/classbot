{% if broadcast == True %}<!channel>
{% endif %}
**Important Pre-Class Setup Directions**: [{{ setup }}]({{ setup }})

**Day {{ day }} Follow Along Guide**: [{{ follow }}]({{ follow }})

**Slack Token**: `{{ token }}`
{% if classid == "dc1-1" or classid == "dc1-2" %}
**Please ensure** that you are in both the *#docker-discuss* and *#docker-practice* channels. Conversation will occur in *#docker-discuss*, but will we use the *#docker-practice* channel for class later in the day.
{% endif %}