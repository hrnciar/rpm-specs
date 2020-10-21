%global pkgname smallsemi

Name:           gap-pkg-%{pkgname}
Version:        0.6.12
Release:        3%{?dist}
Summary:        GAP library of small semigroups

License:        GPLv3+
URL:            https://gap-packages.github.io/%{pkgname}/
Source0:        https://github.com/gap-packages/smallsemi/releases/download/v%{version}/%{pkgname}-%{version}.tar.gz
# Fix documentation failure due to not processing the bibliography file
Patch0:         %{name}-bib.patch

BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core

%description
The Smallsemi package is a data library of semigroups of small size.  It
provides all semigroups with at most 8 elements as well as information
of various kinds about these objects.

%package doc
Summary:        Small semigroups documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -p0 -n %{pkgname}-%{version}

%build
export LC_ALL=C.UTF-8
gap < makedoc.g

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname}-%{version} %{buildroot}%{_gap_dir}/pkg/%{pkgname}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/{CHANGELOG,LICENSE,README}
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}

%check
export LC_ALL=C.UTF-8
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc CHANGELOG README
%license LICENSE
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/doc/

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Jerry James <loganjerry@gmail.com> - 0.6.12-1
- New upstream version (bz 1744687)
- New URLs
- Drop -test patch, no longer needed
- Add -bib patch to fix documentation generation

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 0.6.11-6
- Rebuild for gap 4.10.0
- Add -test patch
- Add -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Jerry James <loganjerry@gmail.com> - 0.6.11-1
- New upstream version (bz 1445743)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 0.6.10-1
- New upstream version

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 12 2015 Jerry James <loganjerry@gmail.com> - 0.6.8-1
- Initial RPM
