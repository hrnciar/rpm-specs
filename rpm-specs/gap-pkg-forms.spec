%global pkgname  forms

Name:           gap-pkg-%{pkgname}
Version:        1.2.5
Release:        3%{?dist}
Summary:        Sesquilinear and quadratic forms

License:        GPLv2+
URL:            http://cage.ugent.be/geometry/forms.php
Source0:        http://cage.ugent.be/geometry/software/%{pkgname}/%{pkgname}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  gap-pkg-autodoc

Requires:       gap-core%{?_isa}

%description
This package provides:
- A way to create and use sesquilinear and quadratic forms on finite
  vector spaces.
- An operation which finds an isometry between two forms of the same type
- An operation which returns the forms left invariant by a matrix group.

%package doc
Summary:        Forms documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for gap-pkg-%{pkgname}.

%prep
%autosetup -n %{pkgname}

%build
mkdir -p ../pkg
ln -s ../%{pkgname} ../pkg
ln -s %{_gap_dir}/doc ../../doc
gap -l "$PWD/..;%{_gap_dir}" < makedoc.g
rm -fr ../../doc ../pkg

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{pkgname} %{buildroot}%{_gap_dir}/pkg
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{pkgname}/doc/*.{aux,bbl,blg,idx,ilg,ind,log,out,pnr,tex}

%check
gap -l "%{buildroot}%{_gap_dir};%{_gap_dir}" < tst/testall.g

%files
%doc README
%{_gap_dir}/pkg/%{pkgname}/
%exclude %{_gap_dir}/pkg/%{pkgname}/doc/
%exclude %{_gap_dir}/pkg/%{pkgname}/examples/

%files doc
%docdir %{_gap_dir}/pkg/%{pkgname}/doc/
%docdir %{_gap_dir}/pkg/%{pkgname}/examples/
%{_gap_dir}/pkg/%{pkgname}/doc/
%{_gap_dir}/pkg/%{pkgname}/examples/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Jul  6 2019 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Initial RPM
