%global pkgname  profiling

Name:           gap-pkg-%{pkgname}
Version:        2.3
Release:        1%{?dist}
Summary:        Line by line profiling and code coverage for GAP

# src/md5.{cc,h} is Public Domain.
# All other files are MIT.
License:        MIT and Public Domain
URL:            http://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Adapt to rapidjson 1.1.0
Patch0:         %{name}-rapidjson.patch

BuildRequires:  flamegraph
BuildRequires:  gcc-c++
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gap-pkg-io
BuildRequires:  libtool
BuildRequires:  pkgconfig(RapidJSON)

Requires:       flamegraph
Requires:       gap-pkg-io%{?_isa}

%description
This package provides line-by-line profiling of GAP, allowing both
discovering which lines of code take the most time, and which lines of
code are even executed.

The main function provided by this package is
OutputAnnotatedCodeCoverageFiles, which takes a previously generated
profile (using ProfileLineByLine or CoverageLineByLine, both provided by
the GAP library), and outputs human-readable HTML files.

There is also OutputFlameGraph, which outputs a graphical diagram
showing which functions took the most time during execution.

%package doc
Summary:        Profiling documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Do not use the bundled rapidjson
rm -fr src/rapidjson
sed -i.orig 's,"\(rapidjson/.*h\)",<\1>,' src/json_parse_rapidjson.h
fixtimestamp src/json_parse_rapidjson.h

# Do not use the bundled FlameGraph
rm -fr FlameGraph
sed -i.orig '/Flame/s,Filename.*],"/usr/bin/flamegraph.pl"],' gap/profiling.gi
fixtimestamp gap/profiling.gi

%build
export LC_ALL=C.UTF-8

# This is not an autoconf-generated configure script; do not use %%configure
./configure %{_gap_dir}
%make_build V=1

# Build the documentation
gap makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
cp -a bin data doc gap tst *.g %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/*/{.libs,*.la}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc AUTHORS HISTORY.md README
%license COPYRIGHT
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Fri Apr  3 2020 Jerry James <loganjerry@gmail.com> - 2.3-1
- Version 2.3

* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 2.2.1-5.20190319.7a582bd
- Drop aarch64 workaround

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 2.2.1-4.20190319.7a582bd
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3.20190319.7a582bd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2.20190319.7a582bd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul  6 2019 Jerry James <loganjerry@gmail.com> - 2.2.1-1.20190319.7a582bd
- Initial package
