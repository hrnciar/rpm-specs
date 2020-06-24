%global upname  SmallGrp
%global pkgname smallgrp

Name:           gap-pkg-%{pkgname}
Version:        1.4.1
Release:        2%{?dist}
Summary:        Small groups library
BuildArch:      noarch

License:        Artistic 2.0
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/releases/download/v%{version}/%{upname}-%{version}.tar.gz

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc
BuildRequires:  parallel
BuildRequires:  procps

Requires:       gap-core

%description
The Small Groups library gives access to all groups of certain "small"
orders.  The groups are sorted by their orders and they are listed up to
isomorphism; that is, for each of the available orders a complete and
irredundant list of isomorphism type representatives of groups is given.

%package doc
Summary:        Small groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{upname}-%{version}

# Fix permissions
chmod a-x id9/idgrp9.g id10/idgrp10.g

%build
# Link to main GAP documentation.
ln -s %{_gap_dir}/doc ../../doc
mkdir ../pkg
ln -s ../%{upname}-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../../doc ../pkg

# Compress large group files
parallel %{?_smp_mflags} --no-notice gzip --best -f ::: id*/* small*/*

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{upname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -fr %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/{COPYRIGHT.md,LICENSE,README*,scripts}
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README README.md
%license COPYRIGHT.md LICENSE
%{_gap_dir}/pkg/%{upname}-%{version}/
%exclude %{_gap_dir}/pkg/%{upname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{upname}-%{version}/doc/
%{_gap_dir}/pkg/%{upname}-%{version}/doc/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Jerry James <loganjerry@gmail.com> - 1.4.1-1
- New upstream version
- Drop upstreamed -ref patch

* Sat Sep 21 2019 Jerry James <loganjerry@gmail.com> - 1.4-1
- New upstream version
- The -ref patch now fixes a different bad reference

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Jerry James <loganjerry@gmail.com> - 1.3-2
- Remove spurious executable bits

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.3-1
- Initial RPM
