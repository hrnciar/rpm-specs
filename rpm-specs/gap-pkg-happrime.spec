%global pkgname happrime

# There has been no release since the import into github, so we take a
# checkout.
%global gitdate     20190208
%global commit      edfbd4188f9aecb3c74e38041fd7173e6fc51067
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           gap-pkg-%{pkgname}
Version:        0.6
Release:        4.%{gitdate}.%{shortcommit}%{?dist}
Summary:        HAP extension for small prime power groups

License:        GPLv2+
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/%{pkgname}/archive/%{commit}/%{pkgname}-%{shortcommit}.tar.gz
# Hap and this package both declare a MakeHAPprimeDoc function.  We need the
# version defined by this package, so we patch out the Hap version.  However,
# this package tries to defer to Hap, but does so incorrectly.  The declaration
# and implementation, in happrime.gd and happrime.gi respectively, both check
# that the name MakeHAPprimeDoc is not globally bound before declaring or
# implementing.  GAP reads the declaration, which binds the name, then sees the
# name is bound, so skips the implementation, leaving us with a bound name with
# no definition.  Since we already patched Hap to remove the competing
# declaration, patch this package to remove the incorrect checks.
Patch0:         %{name}-hap.patch
# Fix some broken references in the documentation
Patch1:         %{name}-doc.patch
# Fix a broken comment that causes a spurious test failure
Patch2:         %{name}-test.patch

BuildArch:      noarch
BuildRequires:  asymptote
BuildRequires:  gap-devel
BuildRequires:  GAPDoc-doc
BuildRequires:  gap-pkg-congruence
BuildRequires:  gap-pkg-edim
BuildRequires:  gap-pkg-hap-doc
BuildRequires:  gap-pkg-lpres
BuildRequires:  gap-pkg-nq
BuildRequires:  gap-pkg-polymaking
BuildRequires:  gap-pkg-singular
BuildRequires:  gap-pkg-smallgrp-doc

Requires:       gap-pkg-hap
Requires:       gap-pkg-singular

%description
This package contains an extension for the HAP package which provides
further operations for (co)homological algebra with finite p-groups.

%package doc
Summary:        HAPprime documentation
Requires:       %{name} = %{version}-%{release}
Requires:       GAPDoc-doc
Requires:       gap-pkg-hap-doc
Requires:       gap-pkg-smallgrp-doc

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{commit}

# Fix tests that fail due to whitespace differences
sed -i 's/Test(\(.*\))/Test(\1, rec( compareFunction := "uptowhitespace" ))/' \
    tst/testall.g

%build
# Build the documentation
export LC_ALL=C.UTF-8
mkdir ../pkg
ln -s ../%{pkgname}-%{commit} ../pkg/%{pkgname}
# First run to create the manual.six files; expect broken reference warnings
gap -l "$PWD/..;%{_gap_dir}" << EOF
LoadPackage( "happrime" );
MakeHAPprimeDoc( "internal" );
EOF
# Second run to fix up the links between the manuals
gap -l "$PWD/..;%{_gap_dir}" << EOF
LoadPackage( "happrime" );
MakeHAPprimeDoc( "internal" );
EOF
rm -fr ../pkg

# Remove the build directory from the HTML links
sed -i "s,$PWD/../pkg/happrime/doc,..,g" doc/{datatypes,userguide}/*.html

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{commit} %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -fr %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{.gitignore,.*.yml,CHANGES,LICENCE,make_tarball,README,doc/includesourcedoc.sh}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README
%license LICENCE
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-4.20190208.edfbd41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-3.20190208.edfbd41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6-2.20190208.edfbd41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 0.6-1.20190208.edfbd41
- Initial RPM
