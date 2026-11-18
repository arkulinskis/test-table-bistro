# The whole website is one file: theme/assets/index.html (edit it under Assets in the Anvil editor).
# This loads that file and shows it as the page, so the address stays the app's main URL and
# pasted <script> snippets (like PlanPlate's widgets) run exactly as they would on a normal website.
import anvil.server
from anvil.js import window

page = anvil.server.get_app_origin() + "/_/theme/index.html"
try:
  html = window.fetch(page, {"cache": "no-store"}).text()
  window.document.open()
  window.document.write(html)
  window.document.close()
except Exception:
  window.location.replace(page)
