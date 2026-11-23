"""Creates the wanted simulator and prints UDID=... and DEVICE=... (for $GITHUB_ENV).
Usage: python3 scripts/ios/create_sim.py "<model>" <iOS major>
Falls back to the closest model of the same family / newest runtime, and says so."""
import json, subprocess, sys


def simctl(*a):
    return subprocess.run(["xcrun", "simctl", *a], capture_output=True, text=True, check=True).stdout


wanted, major = sys.argv[1], sys.argv[2]
d = json.loads(simctl("list", "-j", "devicetypes", "runtimes"))
rts = sorted((r for r in d["runtimes"] if r.get("isAvailable") and ".SimRuntime.iOS" in r["identifier"]),
             key=lambda r: [int(x) for x in r["version"].split(".")])
if not rts:
    sys.exit("No iOS runtime on this Mac")
# Newest runtime of that major that has the wanted model, else one that has its
# family: a runtime can hold only a few devices (Xcode 27's iOS 27.1 has one iPhone)
family = "iPad" if wanted.startswith("iPad") else "iPhone"
cands = list(reversed([r for r in rts if r["version"].split(".")[0] == str(major)] or rts))
def names(r):
    return {t["name"]: t for t in r.get("supportedDeviceTypes") or d["devicetypes"]}
rt = next((r for r in cands if wanted in names(r)), None) or next(
    (r for r in cands if any(n.startswith(family) for n in names(r))), cands[0])
types = names(rt)
model = wanted if wanted in types else [n for n in types if n.startswith(family)][-1]
if model != wanted:
    print(f"{wanted} not available for iOS {rt['version']}: using {model}", file=sys.stderr)
print("UDID=" + simctl("create", "Tester", types[model]["identifier"], rt["identifier"]).strip())
print(f"DEVICE={model}, iOS {rt['version']}")
