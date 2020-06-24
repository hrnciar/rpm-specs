%bcond_with copr
%bcond_with snapshot

%global archive_suffix tar.gz
%global commit 623777f
%global date 20191012

%if %{without snapshot} && %{without copr}
%global gittag v1.2.0-test2-fedora
%global pkgversion %(echo %{gittag} | sed -e 's/^v//' -e 's/-/./g')
%global github_owner pemensik
%else
# Use direct commits
%global github_owner raceintospace
#%%global snapinfo %%{date}git%%{commit}
%global snapinfo test1.g0b4a6ba
%if %{with copr}
# Use fixed archive name, make srpm from current repository
%global pkgversion git
%else
%global pkgversion git%{commit}
%endif
%endif

# Since gcc build is broken, use clang by default
%bcond_without clang

Name:		raceintospace
Version:	1.2.0
Release:	2%{?snapinfo:.%{snapinfo}}%{?dist}
Summary:	Race into Space game

License:	GPLv2+
#URL:		https://github.com/raceintospace/raceintospace
URL:		http://www.raceintospace.org/

#Source0:	https://github.com/%%{github_owner}/%%{name}/archive/%%{gittag}/%%{name}-%%{pkgversion}.%%{archive_suffix}
Source0:	raceintospace-1.2.0.test2.fedora.tar.gz

BuildRequires:	cmake
BuildRequires:	SDL-devel protobuf-devel boost-devel
BuildRequires:	libogg-devel libvorbis-devel libtheora-devel jsoncpp-devel
BuildRequires:	physfs-devel libpng-devel
BuildRequires:	desktop-file-utils
BuildRequires:	libappstream-glib
BuildRequires:	pandoc
%if %{with clang}
BuildRequires:	clang
%else
BuildRequires:	gcc-c++
%endif
Requires:	%{name}-data = %{version}-%{release}

%description
Relive the 1960s Space Race - be the first country to land a man on the Moon!

Race into Space is the free software version of Interplay's
Buzz Aldrin's Race into Space. This is the reworked version following
the source release for the computer version of the Liftoff! board game
by Fritz Bronner. This was developed by Strategic Visions
and published by Interplay as a disk-based game in 1992 and a CD-ROM in 1994.

%package data
BuildArch:	noarch
Summary:	Race into Space game data

%description data
Race into Space is the free software version of Interplay's
Buzz Aldrin's Race into Space. This is the reworked version following
the source release for the computer version of the Liftoff! board game
by Fritz Bronner. This was developed by Strategic Visions
and published by Interplay as a disk-based game in 1992 and a CD-ROM in 1994.

Contains platform independent game data.

%package doc
BuildArch:	noarch
Summary:	Race into Space game manual

%description doc
Race into Space is the free software version of Interplay's
Buzz Aldrin's Race into Space. This is the reworked version following
the source release for the computer version of the Liftoff! board game
by Fritz Bronner. This was developed by Strategic Visions
and published by Interplay as a disk-based game in 1992 and a CD-ROM in 1994.

Contains game manual

%prep
%if %{with clang}
export CC=clang CXX=clang++
# Clang does not support this option
export CFLAGS=`echo '%optflags' | sed -e 's/ -fstack-clash-protection//'`
export CXXFLAGS="$CFLAGS"
%endif
%autosetup -p1 -n %{name}-%{pkgversion}
mkdir build
pushd build
%cmake -DBUILD_PHYSFS=OFF ..
popd

%build
pushd build
%make_build
popd
pushd doc/manual
pandoc -o manual.html manual.md
popd

%install
pushd build
%make_install
popd
install -d %{buildroot}%{_metainfodir}
install -m 0644 doc/raceintospace.appdata.xml %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.appdata.xml

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/raceintospace
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.*
%{_metainfodir}/%{name}.*

%files data
%{_datadir}/%{name}

%files doc
%doc doc/manual

%changelog
* Sun May 31 2020 Petr Menšík <pihhan@gmail.com> - 1.2test1.fedora.2.g0b4a6ba-2
- Development snapshot (0b4a6ba8)

* Sat May 30 2020 Björn Esser <besser82@fedoraproject.org> - 1.1.0-5
- Rebuild (jsoncpp)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 14 2019 Björn Esser <besser82@fedoraproject.org> - 1.1.0-3
- Rebuild (jsoncpp)

* Sat Oct 12 2019 Petr Menšík <pemensik@redhat.com> - 1.1.0-2
- Fix review comment #2 issues
- Fix appcheck, test installed files

* Fri Jul 19 2019 Petr Menšík <pemensik@redhat.com> - 1.1.0-1.20190719gitbf6c86a
- Initial version


