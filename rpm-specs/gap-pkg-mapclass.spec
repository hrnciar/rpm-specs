%global pkgname mapclass
%global upname  MapClass

Name:           gap-pkg-%{pkgname}
Version:        1.4.4
Release:        2%{?dist}
Summary:        Calculate mapping class group orbits for a finite group

License:        GPLv2+
URL:            https://gap-packages.github.io/%{upname}/
Source0:        https://github.com/gap-packages/%{upname}/releases/download/v%{version}/%{upname}-%{version}.tar.gz
# The LICENSE file was added after the most recent release
Source1:        https://raw.githubusercontent.com/gap-packages/MapClass/master/LICENSE
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  GAPDoc-latex

Requires:       gap-core

%description
The MapClass package calculates the mapping class group orbits for a
given finite group.

%package doc
Summary:        MapClass documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{upname}-%{version}
cp -p %{SOURCE1} .

%build
# Build the documentation
mkdir -p ../pkg
ln -s ../%{upname}-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{upname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -fr %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/scripts
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/{LICENSE,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README.md
%license LICENSE
%{_gap_dir}/pkg/%{upname}-%{version}/
%exclude %{_gap_dir}/pkg/%{upname}-%{version}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{upname}-%{version}/doc/
%{_gap_dir}/pkg/%{upname}-%{version}/doc/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 16 2019 Jerry James <loganjerry@gmail.com> - 1.4.4-1
- Initial RPM
