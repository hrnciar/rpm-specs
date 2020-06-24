# Git submodules
%global name1 glad
%global commit1 7bedca283f2951003652efd137d316586d6bc350
%global shortcommit1 %(c=%{commit1}; echo ${c:0:7})
%global name2 imgui
%global commit2 1cb4a92159f9ee85520234d2e7c43180929a1e1d
%global shortcommit2 %(c=%{commit2}; echo ${c:0:7})
%global name3 utf8.h
%global commit3 3e9e3ec15c7bf129664ab2a113eb03b54ee0b584
%global shortcommit3 %(c=%{commit3}; echo ${c:0:7})

# Khronos spec tarball date
%global khgdate 20170718

Name:           openboardview
Version:        7.3
Release:        10%{?dist}
Summary:        Viewer for PCB layouts

# OBV, glad and imgui licensed under MIT, utf8.h - Unlicense
License:        MIT and Unlicense
URL:            http://openboardview.org
Source0:        https://github.com/OpenBoardView/OpenBoardView/archive/R%{version}/openboardview-%{version}.tar.gz
Source1:        https://github.com/Dav1dde/glad/archive/%{commit1}/%{name1}-%{shortcommit1}.tar.gz
Source2:        https://github.com/inflex/imgui/archive/%{commit2}/%{name2}-%{shortcommit2}.tar.gz
Source3:        https://github.com/sheredom/utf8.h/archive/%{commit3}/%{name3}-%{shortcommit3}.tar.gz
# Glad needs these. If it can't find them tries to connect to the Internet
# Generate tarball of Khronos spec with openboardview-gen-khg-spec-tarball.sh
Source4:        khg-spec-%{khgdate}.tar.xz

Source10:       openboardview-gen-khg-spec-tarball.sh
# https://github.com/OpenBoardView/OpenBoardView/issues/58
Source11:       openboardview.desktop
Source12:       openboardview.xml
Source13:       openboardview.appdata.xml

# https://github.com/OpenBoardView/OpenBoardView/issues/76
Patch0:         openboardview-7.3-Fix-ImGui-Text-usage.patch
# https://github.com/OpenBoardView/OpenBoardView/pull/89
Patch1:         openboardview-7.3-bvconv--Fix-it-so-that-it-produces-readable-files.patch
# https://github.com/OpenBoardView/OpenBoardView/commit/381cc682bc5091c23fa6beddb8595e8e3bc1868b
Patch2:         openboardview-7.3-Fix-build-with-GCC-4.8.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  fontconfig-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  gtk3-devel
BuildRequires:  SDL2-devel
BuildRequires:  sqlite-devel
# mdbtools needed by bvconv, OBV renders with OpenGL, uses gtk3 for some menus
Requires:       gtk3
Requires:       mdbtools
Requires:       mesa-dri-drivers
Requires:       mesa-libGL

# 136 errors, first error: expected unqualified-id before '__attribute__'
ExcludeArch:    ppc64le
# Same issue with ppc64 on EPEL7
%if 0%{?rhel}
ExcludeArch:    ppc64
%endif

%description
Software for viewing PCB/Laptop/Motherboard Layouts.

  * Dynamic part outline rendering, including complex connectors
  * Annotations, for leaving notes about parts, nets, pins or location
  * Configurable colour themes
  * Configurable DPI to facilitate usage on 4K monitors
  * Tablet usage with OSD controls
  * Slower CPU systems through adjustable features
  * Reads FZ (with key), BRD, BRD2, BDV and BV* formats
  * Combined search system finds parts, pins and nets all within single search

%prep
%setup -qn OpenBoardView-R%{version} -a1 -a2 -a3
rm -rf src/glad src/imgui src/utf8
mv -v %{name1}-%{commit1} src/%{name1}
mv -v %{name2}-%{commit2} src/%{name2}
mv -v %{name3}-%{commit3} src/utf8
%setup -qn OpenBoardView-R%{version} -D -T -a4

%patch0 -p1
%patch1 -p1
%patch2 -p1
# https://github.com/Dav1dde/glad/issues/99
sed -i 's|^cmake_minimum_required(VERSION 3.0)|cmake_minimum_required(VERSION 2.8)|' src/glad/CMakeLists.txt

# Replace with custom versioning since .git is not present in sources
sed -i 's/^set(OBV_BUILD "R\${GIT_REVISION} \${GIT_REPO}\/\${GIT_BRANCH}")/set(OBV_BUILD "%{version}-%{release}.%{_arch}")/' CMakeLists.txt


%build
%cmake .
%make_build


%install
install -d -m 0755 %{buildroot}%{_bindir}
install -p -m 0755 src/%{name}/%{name} %{buildroot}%{_bindir}
install -p -m 0755 utilities/bvconv.sh %{buildroot}%{_bindir}/bvconv

install -d -m 0755 %{buildroot}%{_datadir}/applications
desktop-file-install %{SOURCE11}

install -d -m 0755 %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
install -p -m 0644 asset/ofbv-app.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -d -m 0755 %{buildroot}%{_datadir}/mime/packages
install -p -m 0644 %{SOURCE12} %{buildroot}/%{_datadir}/mime/packages

install -d -m 0755 %{buildroot}%{_datadir}/appdata
install -p -m 0644 %{SOURCE13} %{buildroot}/%{_datadir}/appdata


%check
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%files
%{_bindir}/%{name}
%{_bindir}/bvconv
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml
%license LICENSE


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Remove post/postun/posttrans scriptlets

* Thu Sep 28 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 7.3-5
- Exclude ppc64 arches that fails to build

* Thu Sep 28 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 7.3-4
- Shorten the sources URLs
- Fix bvconv so that it produces readable file format by OBV
- Drop the F24 scriptlets
- Fix build with EPEL7

* Mon Jul 17 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com> 7.3-3
- Enable debugbuild
- Pull mesa-dri-drivers since it doesn't work without drivers
- Give up from make install, it is stripping the binary and incomplete
- Include a script that generates a tarball of KHG spec files
- Switch sources to official GH tarball and include git submodules
- Add AppStream metadata
- Improve summary and description
- Patch GCC7 build error with ImGui::Text

* Tue Mar 14 2017 Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Escape macro references in changelog
- Escape/replace macros in bash comments

* Sat Nov 12 2016 Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Remove workaround for %%license, since it probably doesn't work anyway

* Tue Nov  1 2016 Samuel Rakitničan <samuel.rakitnican@gmail.com>
- Fix versioning
- Use system sqlite3 library
- Add more supported file formats: asc, bdv, bvr and fz
- Include bvconv

* Sun Oct 30 2016 Samuel Rakitničan <samuel.rakitnican@gmail.com> 7.3-2
- Changed application name for metadata files according to upstream
  https://github.com/inflex/OpenBoardView/commit/2e70494
- Added Group tag
- Added %%license file
- Implemented Fedora Packaging Guidelines compilation method

* Sun Oct 30 2016 Samuel Rakitničan <samuel.rakitnican@gmail.com> 7.3-1
- New version

* Fri Oct 14 2016 Samuel Rakitničan <samuel.rakitnican@gmail.com> 7.2-2
- Implemented building from source

* Tue Oct 11 2016 Samuel Rakitničan <samuel.rakitnican@gmail.com> 7.2-1
- First Build
