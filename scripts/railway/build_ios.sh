#!/usr/bin/env bash
# Builds a91453/railway-game-ios for the iOS Simulator the way its own CI does
# (ios-build.yml: Debug, ad hoc signed so the app group entitlement stays),
# then copies the .app to build/RailwayGame.app for scripts/build/ios.sh.
# Runs from the app checkout (app_dir "."). Use with:
#   ios_build='bash "$GITHUB_WORKSPACE/scripts/railway/build_ios.sh"'  ios_app_path=build/RailwayGame.app
set -euo pipefail
DD="${RUNNER_TEMP:-/tmp}/railway-dd"
xcodebuild build \
  -project RailwayGameApp/RailwayGame.xcodeproj \
  -scheme RailwayGame \
  -configuration Debug \
  -sdk iphonesimulator \
  -destination 'generic/platform=iOS Simulator' \
  -derivedDataPath "$DD" \
  EXCLUDED_ARCHS=x86_64 ONLY_ACTIVE_ARCH=YES \
  CODE_SIGN_IDENTITY=-
APP=$(find "$DD/Build/Products" -maxdepth 2 -path '*iphonesimulator/*.app' -not -name '*Tests*' | head -1)
[ -n "$APP" ] || { echo "no Simulator .app built" >&2; exit 1; }
mkdir -p build && rm -rf build/RailwayGame.app && cp -R "$APP" build/RailwayGame.app
echo "built $(basename "$APP")"
