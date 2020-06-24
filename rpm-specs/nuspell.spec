Name:		nuspell
Version:	3.1.1
Release:	3%{?dist}
Summary:	C++ spelling checking library and command-line tool
License:	LGPLv3+
URL:		https://nuspell.github.io
Source0:	https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	boost-locale
BuildRequires:	clang
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	git
BuildRequires:	libicu-devel
BuildRequires:	rdkit-devel
BuildRequires:	rubygem-ronn
BuildRequires:	catch-devel
Requires:		hunspell-en-US

%description
Nuspell is a fast and safe spelling checker software program. It is designed \
for languages with rich morphology and complex word compounding. Nuspell is \
written in modern C++ and it supports Hunspell dictionaries.

%package devel
Summary:	Development tools for %{name}
Requires:	libicu-devel
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains the header files and developer docs for \
%{name}.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake . -DBUILD_SHARED_LIBS=1 -DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_PREFIX=%{_prefix}
%make_build

%install
%make_install

%check
ctest

%files
%{_mandir}/man1/%{name}*
%{_bindir}/%{name}
%{_libdir}/*.so.3*
%license COPYING COPYING.LESSER
%doc AUTHORS CHANGELOG.md README.md

%files devel
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.so

%doc %{_docdir}/nuspell/

%changelog
* Sat May 30 2020 Jonathan Wakely <jwakely@redhat.com> - 3.1.1-3
- Rebuilt for Boost 1.73

* Wed May 20 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.1.1-2
- added tests

* Fri May 15 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.1.1-1
- Updated description and summary
- New release 3.1.1

* Mon Apr 27 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.1.0-1
- New release

* Fri Apr 3 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-5
- Added license files and doc files 

* Thu Mar 26 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-4
- renamed archive name 
- replaced cmake with %%cmake and make with %%make_build macro

* Mon Mar 02 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-3
- Update URL link
- Updated description
- Modified man page files macro

* Thu Feb 27 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-2
- Updated files to _libdir/cmake/nuspell/ instead of *.cmake files

* Tue Feb 25 2020 Vishal Vijayraghavan <vishalvvr@fedoraproject.org> - 3.0.0-1
- First release
