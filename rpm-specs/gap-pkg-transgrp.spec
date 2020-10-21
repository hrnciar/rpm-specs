%global pkgname transgrp

Name:           gap-pkg-%{pkgname}
Version:        3.0
Release:        1%{?dist}
Summary:        Transitive groups library
BuildArch:      noarch

License:        GPLv2 or GPLv3
URL:            https://www.gap-system.org/Packages/%{pkgname}.html
Source0:        https://www.math.colostate.edu/~hulpke/%{pkgname}/%{pkgname}%{version}.tar.gz
Source1:        https://www.math.colostate.edu/~hulpke/%{pkgname}/trans32.tgz

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex
BuildRequires:  parallel
BuildRequires:  procps

Requires:       gap-core
Requires:       %{name}-data = %{version}-%{release}

%description
A library of transitive groups.  This package contains the code for
accessing the library.  The actual data is in the data and data32
subpackages.

%package data
Summary:        Data files for groups of degree other than 32
License:        Artistic 2.0
Requires:       %{name} = %{version}-%{release}

%description data
This package contains a library of transitive groups of degree other
than 32.  Groups of degree 15-30 are due to Alexander Hulpke.  Groups
of degree 34-47 are due to Derek Holt.  Not all degrees greater than 30
are yet available.

%package data32
Summary:        Library of transitive groups of degree 32
License:        Artistic 2.0
Requires:       %{name} = %{version}-%{release}

%description data32
This package contains a library of transitive groups of degree 32, due
to John Cannon and Derek Holt.

%package doc
Summary:        Transitive groups library documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%setup -q -n %{pkgname}
%setup -q -T -D -a 1 -n %{pkgname}

# Fix the test options
sed -i 's/\(ignoreComments.*)\)/testOptions:=rec(\1)/' tst/testall.g

%build
# Compress large group files
parallel %{?_smp_mflags} --no-notice gzip --best ::: dat32/*.grp data/*.grp

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{LICENSE,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/._manual.pdf

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/data/
%exclude %{_gap_dir}/pkg/%{pkgname}/dat32/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}/htm/

%files data
%{_gap_dir}/pkg/%{pkgname}/data/

%files data32
%{_gap_dir}/pkg/%{pkgname}/dat32/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}/htm/
%{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/htm/

%changelog
* Sat Aug  1 2020 Jerry James <loganjerry@gmail.com> - 3.0-1
- Version 3.0

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Feb 25 2020 Jerry James <loganjerry@gmail.com> - 2.0.5-1
- Version 2.0.5

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 13 2019 Jerry James <loganjerry@gmail.com> - 2.0.4-2
- Remove hidden file

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 2.0.4-1
- Initial RPM
