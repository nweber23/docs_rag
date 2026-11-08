# Release process

Releases of the Acme CLI are cut from the `release/stable` branch, never directly from `main`.
A release happens every second Thursday. The release manager tags the commit with a
version such as `v2.14.0` and publishes the wheel to the internal package index.

## Hotfixes

A hotfix needs approval from two people: the release manager and one member of the
platform team. After approval the fix is cherry-picked onto `release/stable` and a patch
version is tagged, for example `v2.14.1`.

## Rollback

If a release breaks the nightly smoke tests, the release manager yanks the version from
the index within 30 minutes and re-tags the previous release as `latest`.
