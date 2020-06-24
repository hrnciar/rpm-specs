%global pkgname  datastructures

Name:           gap-pkg-%{pkgname}
Version:        0.2.5
Release:        4%{?dist}
Summary:        Standard data structures for GAP

License:        GPLv2+
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  gcc
BuildRequires:  libtool

Requires:       gap-core%{?_isa}

%description
The datastructures package aims at providing standard datastructures,
consolidating existing code and improving on it, in particular in view
of HPC-GAP.

The following data structures are provided:
- queues
- doubly linked lists
- heaps
- priority queues
- hashtables
- dictionaries

%package doc
Summary:        Data structures documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8

# This is NOT an autoconf-generated script.  Do NOT use %%configure.
./configure %{_gap_dir}
%make_build

# Build the documentation
mkdir -p ../pkg
ln -s ../%{pkgname}-%{version} ../pkg
ln -s %{_gap_dir}/doc ../../doc
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg ../../doc

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -p bin/%{_gap_arch}/.libs/datastructures.so \
   %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/bin/%{_gap_arch}
cp -a doc gap tst *.g  %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES.md README.md
%license COPYRIGHT.md LICENSE
%{_gap_dir}/pkg/%{pkgname}-%{version}/
%exclude %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}-%{version}/doc/
%{_gap_dir}/pkg/%{pkgname}-%{version}/doc/

%changelog
* Mon Mar 23 2020 Jerry James <loganjerry@gmail.com> - 0.2.5-4
- Drop aarch64 workaround

* Wed Mar 11 2020 Jerry James <loganjerry@gmail.com> - 0.2.5-3
- Rebuild for gap 4.11.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 11 2019 Jerry James <loganjerry@gmail.com> - 0.2.5-1
- Version 0.2.5
- Drop upstreamed -doc patch

* Mon Sep 16 2019 Jerry James <loganjerry@gmail.com> - 0.2.4-1
- Initial RPM
