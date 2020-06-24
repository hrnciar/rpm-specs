%global pkgname toric
%global upname  Toric

Name:           gap-pkg-%{pkgname}
Version:        1.9.5
Release:        2%{?dist}
Summary:        Computations with toric varieties in GAP

License:        MIT
URL:            https://gap-packages.github.io/toric/
Source0:        https://github.com/gap-packages/toric/releases/download/v%{version}/%{upname}-%{version}.tar.gz
# Fix a misplaced comma and other problems in a BibTeX entry
# https://github.com/gap-packages/toric/pull/12
Patch0:         0001-Fix-problems-with-the-Gua05-BibTeX-entry.patch

BuildArch:      noarch
BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
Toric implements some computations related to toric varieties and
combinatorial geometry in GAP.  Affine toric varieties can be created
and related information about them can be calculated.

%package doc
Summary:        Toric documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p1 -n %{upname}-%{version}

# Linux filesystems are case-sensitive
mv doc/toric.xml doc/Toric.xml

%build
gap makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{upname}-%{version} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/{CHANGES,LICENSE,README.md}
rm -f %{buildroot}%{_gap_dir}/pkg/%{upname}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGES README.md
%license LICENSE
%{_gap_dir}/pkg/%{upname}-%{version}/
%exclude %{_gap_dir}/pkg/%{upname}-%{version}/doc

%files doc
%docdir %{_gap_dir}/pkg/%{upname}-%{version}/doc/
%{_gap_dir}/pkg/%{upname}-%{version}/doc/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 15 2019 Jerry James <loganjerry@gmail.com> - 1.9.5-1
- New upstream version
- Add patch to fix BibTeX problems

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.9.4-4
- Rebuild for gap 4.10.0
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb  6 2018 Jerry James <loganjerry@gmail.com> - 1.9.4-1
- Initial RPM
