# Brief: a new player's first session of a railway management game

Read AGENT_BRIEF.md and briefs/improve.md first: their tools, rules and report
files all apply. This brief only adds what is special about this app.

The app is a railway and city management game for iPhone and iPad. The player
buys real railway lines, runs trains on timetables, and grows the cities
around them. Most of the screen is a 3D map drawn by the GPU: the element list
of `screen.py` does not see what is on the map (trains, stations, tracks), only
the buttons and panels above it. Read the map from the screenshot itself, and
tap what you see there by its position.

- On an iPhone the game runs in landscape only. If the screenshot looks turned
  or the taps land in the wrong place, say so once in the report (it is a
  limit of the test setup, not of the game), then keep going as best you can.
- Pinch and two-finger gestures are not available: pan the map with a swipe,
  and use the game's own buttons to zoom, if it has them.
- The first launch may load for a while: wait (sleep 5, then look again) up
  to about a minute before calling it stuck.
- The budget is about 40 actions, not 30: a game's first session is longer.

What matters most to this team, beyond your persona's goal:
1. Text cut off, overlapping or too small at your text size; buttons hidden
   under the notch, the Dynamic Island or the home bar, or off the screen.
2. Touch targets that are hard to hit, and controls whose meaning is unclear.
3. Where a new player gets stuck or does not know what to do next.
4. Text left in another language than yours, or translations that read oddly.
5. Panels that cover the map so the player cannot see what they just did.

Write `report.md` and `findings.json` in English, but quote the app's own
text exactly as shown.
