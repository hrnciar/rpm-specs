Name:    We10X-icon-theme
Summary: Colorful icon theme inspired by Microsoft Windows 10 aesthetic
License: GPLv3

%global git_date    20200922
%global git_commit  9ab1efdd7002dbb04c504fd3f120d50298a07f59
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:8})

Version: 0
Release: 7.%{git_date}git%{git_commit_short}%{?dist}

URL: https://github.com/yeyushengfan258/%{name}
Source0: %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

BuildArch: noarch

Requires: hicolor-icon-theme

%description
We10X is a colorful icon theme inspired
by the aesthetic of Microsoft Windows 10.

Comes in a regular and dark variant.


%prep
%autosetup -n %{name}-%{git_commit}

# Remove spurious executable bits found on some files
chmod 644 ./AUTHORS ./COPYING
find links/ src/ -executable -type f -exec chmod -v -- a-x '{}' '+'

# Remove broken links
find links/ -follow -type l -printf 'deleted broken symlink "%p" -> "%l"\n' -delete

# Remove empty directories
for FILE in $(find ./ -name '.directory'); do
	DIR="$(dirname "${FILE}")"
	rm "${FILE}"
	rmdir "${DIR}" || true
done

# Do not call gtk-update-icon-cache during install
sed  \
	-e '/gtk-update-icon-cache/d'  \
	-i install.sh


%build
# Nothing to do here


%install
install -m 755 -d '%{buildroot}%{_datadir}/icons'
./install.sh --dest '%{buildroot}%{_datadir}/icons'

for VARIANT in '' '-dark'; do
	THEME="%{buildroot}%{_datadir}/icons/We10X${VARIANT}"
	touch "${THEME}/icon-theme.cache"

	rm "${THEME}/AUTHORS"
	rm "${THEME}/COPYING"
done


%transfiletriggerin -- %{_datadir}/icons/W10X
gtk-update-icon-cache --force %{_datadir}/icons/W10X &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/W10X-dark
gtk-update-icon-cache --force %{_datadir}/icons/W10X-dark &>/dev/null || :


%files
%doc AUTHORS
%license COPYING

# -- normal variant

%dir %{_datadir}/icons/We10X
%ghost %{_datadir}/icons/We10X/icon-theme.cache
%{_datadir}/icons/We10X/index.theme

%{_datadir}/icons/We10X/16
%{_datadir}/icons/We10X/16@2x
%{_datadir}/icons/We10X/22
%{_datadir}/icons/We10X/22@2x
%{_datadir}/icons/We10X/24
%{_datadir}/icons/We10X/24@2x
%{_datadir}/icons/We10X/32
%{_datadir}/icons/We10X/32@2x
%{_datadir}/icons/We10X/scalable
%{_datadir}/icons/We10X/scalable@2x
%{_datadir}/icons/We10X/symbolic

# -- dark variant

%dir %{_datadir}/icons/We10X-dark
%ghost %{_datadir}/icons/We10X-dark/icon-theme.cache
%{_datadir}/icons/We10X-dark/index.theme

%{_datadir}/icons/We10X-dark/16
%{_datadir}/icons/We10X-dark/16@2x
%{_datadir}/icons/We10X-dark/22
%{_datadir}/icons/We10X-dark/22@2x
%{_datadir}/icons/We10X-dark/24
%{_datadir}/icons/We10X-dark/24@2x
%{_datadir}/icons/We10X-dark/32
%{_datadir}/icons/We10X-dark/32@2x
%{_datadir}/icons/We10X-dark/scalable
%{_datadir}/icons/We10X-dark/scalable@2x
%{_datadir}/icons/We10X-dark/symbolic


%changelog
* Thu Sep 24 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-7.20200922git9ab1efdd
- Update to latest upstream git snapshot

* Thu Sep 10 2020 Artur Frenszek-Iwicki <fedora@svgames.pl> - 0-6.20200910git9ba7a59b
- Update to latest upstream git snapshot

* Fri Aug 28 2020 Artur Iwicki <fedora@svgames.pl> - 0-5.20200824git3391e427
- Update to latest upstream snapshot
- Don't edit install.sh to preserve file timestamps (fixed upstream)

* Thu Aug 20 2020 Artur Iwicki <fedora@svgames.pl> - 0-4.20200818git3010fa4a
- Update to latest upstream git snapshot
- Remove broken symlinks before install
- Remove empty directories before install

* Tue Jun 23 2020 Artur Iwicki <fedora@svgames.pl> - 0-3.20200621gitdd69e31a
- Update to latest upstream git snapshot

* Sun May 24 2020 Artur Iwicki <fedora@svgames.pl> - 0-2.20200522git1e951299
- Update to latest upstream git snapshot

* Tue May 05 2020 Artur Iwicki <fedora@svgames.pl> - 0-1.20200504git4b95b047
- Initial packaging
