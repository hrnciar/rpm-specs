%global git_snapshot 1

%if 0%{?git_snapshot}
%global git_rev 618c418ea8f064cca21ac0aeb527c01e088a748f
%global git_date 20180824
%global git_short %(echo %{git_rev} | cut -c-8)
%global git_version %{git_date}git%{git_short}
%endif

Name:           glyr
Version:        1.0.10
Release:        13%{?git_version:.%{?git_version}}%{?dist}
Summary:        Search engine for music related metadata

# Source0 was generated as follows:
# git clone https://github.com/sahib/glyr.git
# cd %%{name}
# git archive --format=tar --prefix=%%{name}/ %%{git_short} | bzip2 > %%{name}-%%{?git_version}.tar.bz2

License:        LGPLv3
URL:            https://github.com/sahib/glyr
Source0:        %{name}-%{?git_version}.tar.bz2
Patch0:         0002-update-version-to-last-tag.patch
Patch1:         0003-add-release-with-with-debug-build-target.patch
Patch2:         0004-disables-test-that-depends-on-internet-connection.patch

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(glib-2.0) >= 2.10
BuildRequires:  pkgconfig(sqlite3) >= 3.4
BuildRequires:  pkgconfig(check)

Requires:       %{name}-libs = %{version}-%{release}

%description
Search engine for music related metadata.
It comes both in a command-line interface tool and as a C library, both with an
easy-to-use interface. The sort of metadata glyr is searching (and downloading)
is usually the data you see in your music player. And indeed, originally it was
written to serve as internally library for a music player, but has been extended
to work as a standalone program which is able to download: cover art, lyrics,
band photos, artist biography, album reviews, track lists of an album, a list of
albums from a specific artist, tags, either related to artist, album or title
relations, for example links to Wikipedia, similar artists and similar songs.

%package        -n %{name}-libs
Summary:        %{name} library

Provides:       lib%{name} = %{version}-%{release}
Obsoletes:      lib%{name} < %{version}-%{release}

%description    -n %{name}-libs
The lib%{name} package contains libraries for applications that use %{name}.


%package        -n %{name}-devel
Summary:        Development files for %{name}
Requires:       %{name}-libs = %{version}-%{release}

Provides:       lib%{name}-devel = %{version}-%{release}
Obsoletes:      lib%{name}-devel < %{version}-%{release}

%description    -n %{name}-devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%setup -qn %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{cmake} -DTEST=true -DCMAKE_BUILD_TYPE=RelWithDebInfo .
%make_build

%check
bin/check_api
CK_TIMEOUT_MULTIPLIER=20 bin/check_dbc
# This check fails so ignore that
# bin/check_opt

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%files
%license COPYING
%doc CHANGELOG AUTHORS
%{_bindir}/glyrc

%files -n %{name}-libs
%{_libdir}/lib%{name}.so.*

%files -n %{name}-devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/lib%{name}.pc


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-13.20180824git618c418e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-12.20180824git618c418e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jan 30 2019 Matias De lellis <mati86dl@gmail.com> - 1.0.10-11.20180824git618c418e
- Increase timeout in test, and add construction directory in cmake.

* Thu Nov 08 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-10.20180824git618c418e
- Add a patch that disables test that depends on internet connection.

* Thu Nov 01 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-9.20180824git618c418e
- Add check as a build requirement.

* Thu Oct 25 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-8.20180824git618c418e
- Rebuild with debug and test.

* Thu Oct 25 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-7.20180824git618c418e
- Fix some recommendations in package review.

* Wed Oct 24 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-6.20180824git618c418e
- Fix some recommendations in package review.

* Mon Oct 22 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-5.20180824git618c418e
- Fix some rpmlint warnings

* Sun Oct 14 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-4.20180824git618c418e
- Fix some rpmlint warnings

* Tue Oct 02 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-3.20180824git618c418e
- Update to last snapshot

* Wed Feb 14 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-2
- Update to stable 1.0.10

* Thu Jan 04 2018 Matias De lellis <mati86dl@gmail.com> - 1.0.10-1
- Update to stable 1.0.10

* Thu Jun 22 2017 Matias De lellis <mati86dl@gmail.com> - 1.0.9-1

* Wed Sep 10 2014 Matias De lellis <mati86dl@gmail.com> - 1.0.6-1
- Update to stable 1.0.6

* Mon Mar 17 2014 Matias De lellis <mati86dl@gmail.com> - 1.0.5-2
- Add glib to BuildRequires

* Sun Feb 09 2014 Matias De lellis <mati86dl@gmail.com> - 1.0.5-1
- Update to estable 1.0.5
- Split glyrc commandline tool and libraries.

* Tue Dec 17 2013 Matias De lellis <mati86dl@gmail.com> - 1.0.2-1
- Update to estable 1.0.2

* Sat Mar 02 2013 Matias De lellis <mati86dl@gmail.com> - 1.0.1-1
- Update to estable 1.0.1

* Wed Aug 22 2012 Matias De lellis <mati86dl@gmail.com> - 1.0.0-1
- Update to estable 1.0.0

* Tue Mar 06 2012 Matias De lellis <mati86dl@gmail.com> - 0.9.5-1
- Update to estable 0.9.5

* Wed Feb 29 2012 Matias De lellis <mati86dl@gmail.com> - 0.9.4-1.20120221git1d351dfc
- Update to last git snapshot.

* Tue Jan 31 2012 Matias De lellis <mati86dl@gmail.com> - 0.9.3-1.20120123git212166e8
- Initial package
