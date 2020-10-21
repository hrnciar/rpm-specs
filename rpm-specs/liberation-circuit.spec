Name: liberation-circuit
Summary: Real-time strategy game with programmable units
License: GPLv3

URL: https://linleyh.itch.io/liberation-circuit

%global git_date 20200131
%global git_commit_long f930e6e1aeb74d8962c96c66b3a342485a422e23
%global git_commit_short %(c="%{git_commit_long}"; echo "${c:0:8}")

Version: 1.3
Release: 6.%{git_date}git%{git_commit_short}%{?dist}

%global repo_url https://github.com/linleyh/%{name}
Source0: %{repo_url}/archive/%{git_commit_long}/%{name}-%{git_commit_long}.tar.gz

# The upstream CMakeLists assume that the game is compiled for the monolith
# version of Allegro and don't work properly with the split "base + addons"
# version that Fedora uses, so they need to be tweaked a bit
Patch0: libcirc--CMakeLists-nonmonolith-Allegro.patch

BuildRequires: allegro5-devel
BuildRequires: allegro5-addon-acodec-devel
BuildRequires: allegro5-addon-audio-devel
BuildRequires: allegro5-addon-dialog-devel
BuildRequires: allegro5-addon-image-devel
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: mesa-libGL-devel

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

Requires: hicolor-icon-theme
Requires: %{name}-data = %{version}-%{release}


%description
Escape from a hostile computer system! Harvest data to create an armada
of battle-processes to aid your escape. Take command directly and play the game
as an RTS, or use the game's built-in editor and compiler to write
your own unit AI in a simplified version of C.


%package data
Summary: Data files required to play Liberation Circuit
BuildArch: noarch


%description data
This package contains assets, such as graphics and sound effects,
required to play Liberation Circuit.


%prep
%autosetup -p1 -n %{name}-%{git_commit_long}


%build
%cmake ./
%cmake_build

cat > bin/%{name}-wrapper << EOF
#!%{_bindir}/sh
cd %{_datadir}/%{name}
%{_libexecdir}/%{name} "\$@"
EOF


%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 bin/%{name}-wrapper  %{buildroot}%{_bindir}/%{name}

install -m 755 -d %{buildroot}%{_libexecdir}/
install -m 755 bin/%{name}  %{buildroot}%{_libexecdir}/%{name}

install -m 755 -d %{buildroot}%{_datadir}/%{name}
for FILE in data proc story init.txt; do
  cp -a "bin/${FILE}" "%{buildroot}%{_datadir}/%{name}/${FILE}"
done

install -m 755 -d %{buildroot}%{_datadir}/applications
desktop-file-install linux-packaging/%{name}.desktop \
  --dir=%{buildroot}%{_datadir}/applications/

install -m 755 -d %{buildroot}%{_metainfodir}
cp -a linux-packaging/%{name}.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml

for ICONSIZE in 16 32 256; do
  ICONDIR="%{buildroot}%{_datadir}/icons/hicolor/${ICONSIZE}x${ICONSIZE}/apps"
  install -m 755 -d "${ICONDIR}"
  cp -a "linux-packaging/icon-${ICONSIZE}px.png" "${ICONDIR}/%{name}.png"
done


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml


%files
%doc bin/Manual.html
%license LICENSE.md
%{_bindir}/%{name}
%{_libexecdir}/%{name}
%{_datadir}/applications/%{name}.*
%{_metainfodir}/%{name}.*
%{_datadir}/icons/hicolor/**/apps/%{name}.png

%files data
%license bin/licence.txt
%{_datadir}/%{name}


%changelog
* Wed Jul 29 2020 Artur Iwicki <fedora@svgames.pl> - 1.3-6.20200131gitf930e6e1
- Update to latest upstream snapshot
- Drop Patch1 (build failures due to symbol redefinitions - merged upstream)
- Update spec to work with CMake out-of-source builds

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-5.20191015git4ff5a114
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Artur Iwicki <fedora@svgames.pl> - 1.3.4-20191015git4ff5a114
- Fix build failures due to redefined variables
- Update to latest upstream git snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3.20190824git29bc0ce0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 24 2019 Artur Iwicki <fedora@svgames.pl> - 1.3.2-20190824git29bc0ce0
- Update to latest upstream snapshot
- Drop Source1 (linux-packaging.zip - merged upsteam)
- Drop Patch0 (format string security - merged upstream)
- Add a patch file for CMakeLists instead of editing them with sed in %%prep
- Pass arguments to the executable in the wrapper script

* Fri Aug 16 2019 Artur Iwicki <fedora@svgames.pl> - 1.3-1.20181105.git.dc2b5b08
- Initial packaging

